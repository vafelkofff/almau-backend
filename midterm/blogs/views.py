from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def blogs_handler(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data)
        blogs = Blog.objects.all()

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)


# def get_blog(pk):
#     try:
#         category = Blog.objects.get(id=pk)
#         return {
#             'blog': blog,
#             'status': 200
#         }
#     except Blog.DoesNotExist as e:
#         return {
#             'blog': None,
#             'status': 404
#         }
def get_blog(pk):
    try:
        blog = Blog.objects.get(id=pk)
        return {
            'blog': blog,
            'status': 200
        }
    except Blog.DoesNotExist as e:
        return {
            'blog': None,
            'status': 404
        }

@csrf_exempt
def blog_handler(request, pk):
    result = get_blog(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Category not found'}, status=404)

    blog = result['blog']

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = BlogSerializer(data=data, instance=blog)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, 400)
    if request.method == 'DELETE':
        blog = Blog.objects.get(id=pk)
        blog.delete()
        serializer = BlogSerializer(blog)
        return JsonResponse({'message': 'Category successfully deleted'}, status=200)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)