from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import StudentCreateView, StudentListView, StudentDetailView
from django.conf import settings
from django.conf.urls.static import static


app_name = "stem"

urlpatterns = [
    #path('', views.home, name='home'),
    path('', StudentCreateView.as_view(), name='home'),
    path('manage-students/', StudentListView.as_view(), name='list-students'),
    path('profile/<int:pk>/', StudentDetailView.as_view(), name='student-details'),
    path('login/', auth_views.LoginView.as_view(template_name='stem/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='stem/logout.html'), name='logout'),
    #path('new/', PostCreateView.as_view(), name='post-create'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('result/', views.search, name='result'),
    #path('new/', views.post_create, name='post-create'),
    #url(r'post/(?P<id>\d+)/$', views.post_detail, name='post-detail'),
    #url(r'^like/$', views.like_post, name='like_post'),
]