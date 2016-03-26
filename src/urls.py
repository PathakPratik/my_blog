from django.conf.urls import url
from src.views import PostManager

urlpatterns = [
    url(r'posts',PostManager.as_view(), name='posts')
]