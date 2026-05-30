from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from post.models import Post

def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, template_name="post_list.html", context=context)
    elif request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        author_name = request.POST.get("author_name")

        if not (type(title) is str and 0 < len(title) <= 128):
            return HttpResponseBadRequest("Invalid title")
        if not (type(body) is str and 0 < len(body) <= 1024):
            return HttpResponseBadRequest("Invalid body")
        if not (type(author_name) is str and 0 < len(author_name) <= 32):
            return HttpResponseBadRequest("Invalid author_name")

        post = Post.objects.create(title=title, body=body, author_name=author_name)
        context = {"post": post}
        return render(request, template_name="post_detail.html", context=context)

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, template_name="post_detail.html", context=context)