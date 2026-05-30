from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post
from post.forms import PostForm

def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {"posts": posts, "form": PostForm}
        return render(
            request, template_name="post_list.html", context=context
        )
    elif request.method == "POST":
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

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(
        request, template_name="post_detail.html", context=context
    )