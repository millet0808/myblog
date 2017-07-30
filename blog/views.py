from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Post


# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})


def post_create(request):
    if request.method == "POST":
        new_title = request.POST.get('title')
        new_text = request.POST.get('text')
        new_post = Post(title=new_title, text=new_text)

        new_post.save()

        new_post.publish()
        return redirect('post_list')

    return render(request, 'blog/post_create.html', {})
