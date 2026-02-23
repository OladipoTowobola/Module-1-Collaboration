<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render
=======
from django.shortcuts import render
>>>>>>> de1d1c1ad6305bb82b2bcd3cf6306cb9a3962033
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

<<<<<<< HEAD
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

=======
>>>>>>> de1d1c1ad6305bb82b2bcd3cf6306cb9a3962033
