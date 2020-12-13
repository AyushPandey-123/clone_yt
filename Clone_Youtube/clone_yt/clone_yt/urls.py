"""clone_yt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
import debug_toolbar
from core.views import HomeView,NewVideo,LoginView,RegisterView,VideoView,CommentView,VideoFileView,LogOutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/<int:video_id>',VideoView.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
    path('',HomeView.as_view()),
    path('login',LoginView.as_view()),
    path('register',RegisterView.as_view()),
    path('new_video',NewVideo.as_view()),
    path('comment',CommentView.as_view()),
    path('get_video/<file_name>',VideoFileView.as_view()),
    path('logout',LogOutView.as_view())
]
