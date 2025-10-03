from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать в мой блог!</h1>")

def post_list_view(request):
    posts = Post.objects.all()
    html = "<h1>Все посты</h1><ul>"
    for post in posts:
        html += f"<li><strong>{post.title}</strong>: {post.content[:50]}...</li>"
    html += "</ul>"
    return HttpResponse(html)

def post_detail_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        html = f"<h1>{post.title}</h1><p>{post.content}</p>"
        return HttpResponse(html)
    except Post.DoesNotExist:
        return HttpResponse("<h1>Пост не найден</h1>", status=404)