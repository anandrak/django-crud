from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
def home(request):
    context = { 'posts' : Post.objects.all() }
    return render(request, 'bulletin/home.html', context)

# urlpattern for ListView => <appname>/<model>_<viewtype>.html
class PostListView(ListView):
    model = Post
    template_name = 'bulletin/home.html'
    context_object_name = 'posts'
    ordering = ['date']
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'bulletin/detail.html'
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'bulletin/create.html'
    fields = ['title', 'content']

    #check the author from the former class with super() ->inherits current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'bulletin/create.html'

    #check the author from the former class with super() ->inherits current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'bulletin/delete.html'
    context_object_name = 'posts'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
