from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View
from src.models import Post


class PostManager1(View):

    def get(self, request, slug ):
        return render(request,
                      'src/templates/post.html',
                      {'post': get_object_or_404(Post, slug=slug)}
                      )


class PostManager(View):

    def get(self, request):
        list_of_post_objs = Post.objects.order_by('-created_at')
        return render(request,
                      'src/templates/index.html',
                      {'posts':list_of_post_objs}
                      )
