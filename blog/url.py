from django.urls import path
from . import views
from blog.views import PostListView, PostDetailView, PostCreateView
# from users import views as user_views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

   # path('profile/', user_views.profile, name='profile')


]