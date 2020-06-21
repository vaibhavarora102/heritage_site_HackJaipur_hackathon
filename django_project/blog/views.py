from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Post2, Take_Img
from django.http import HttpResponse
from django.db.models import Q
from .forms import ImageForm


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/text_search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query)

def base(request):
    return render(request, 'blog/site5.html')
    

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/site.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/site.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class PostListView2(ListView):
    model = Post2
    template_name = 'blog/model.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        state = get_object_or_404(User, username=self.kwargs.get('state'))
        return Post.objects.filter(state=state).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','state','price','post_image','post_image2','post_image3','post_image4','post_image5','post_image6']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','state','price','post_image','post_image2','post_image3','post_image4','post_image5','post_image6']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def model(request):
    return render(request, 'blog/model.html')


def model1(request):
    return render(request, 'blog/model1.html')
def model2(request):
    return render(request, 'blog/model2.html')
def model3(request):
    return render(request, 'blog/model3.html')
def model4(request):
    return render(request, 'blog/model4.html')
def model5(request):
    return render(request, 'blog/model5.html')
def map(request):
    return render(request, 'blog/map.html')
def img(request):
    return render(request, 'blog/site2.html')