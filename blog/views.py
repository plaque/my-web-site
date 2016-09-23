from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Timeline
from rest_framework import generics
from blog.serializers import PostSerializer


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def timeline(request):
    timelines = Timeline.objects.all().order_by('date')
    return render(request, 'blog/timeline_date.html', {'timelines': timelines})


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer