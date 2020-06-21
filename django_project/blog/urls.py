from django.urls import path
from .views import (
    PostListView,
    PostListView2,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    SearchResultsView
)
from . import views

urlpatterns = [
    path('', views.base, name='base_site'),
    path('home', PostListView.as_view(), name='blog-home'),
    path('model/', PostListView2.as_view(), name='blog-model'),
    path('state/<str:state>', UserPostListView.as_view(), name='state-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('img/', views.img, name='img'),
    path('model/model1', views.model1, name='model1'),
    path('model/model2', views.model2, name='model2'),
    path('model/model3', views.model3, name='model3'),
    path('model/model4', views.model4, name='model4'),
    path('model/model5', views.model5, name='model5'),



]
