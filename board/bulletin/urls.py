from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('',PostListView.as_view(), name='home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='detail'),
    path('post/<str:username>',UserPostListView.as_view(), name='userpost'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='delete'),
    path('post/create/',PostCreateView.as_view(), name='create'),
]

# urlpattern for ListView => <appname>/<model>_<viewtype>.html