from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.views import View

from post.models import Post
from post.forms import PostForm


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts, "form": PostForm}
        return render(
            request, template_name="post_list.html", context=context
        )

class PostCreateView(View):
    def get(self, request):
        context = {"form": PostForm}
        return render(
            request, template_name="post_create.html", context=context
        )

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            author_name = form.cleaned_data["author_name"]

            post = Post.objects.create(
                title=title, body=body, author_name=author_name
            )
            context = {"post": post}
            return render(
                request, template_name="post_detail.html", context=context
            )
    
        return redirect("posts")

class PostDetailView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        context = {"post": post}
        return render(
            request, template_name="post_detail.html", context=context
        )

class PostLikeView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.points = F("points") + 1 # post.points = F()
        post.save()
        post.refresh_from_db()
        return render(
            request, template_name="post_detail.html", context={"post": post}
        )