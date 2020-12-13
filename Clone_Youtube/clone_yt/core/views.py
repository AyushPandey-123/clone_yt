from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.base import View
from .forms import LoginForm,RegisterForm,NewVideoForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Video,Comment
import os
from wsgiref.util import FileWrapper
# Create your views here.

class VideoFileView(View):
    def get(self,request,file_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response

class HomeView(View):
    template_name = 'index.html'
    def get(self,request):
        most_recent_video = Video.objects.order_by('-datetime')[:10]
        return render(request,self.template_name,{'most_recent_video':most_recent_video})

class VideoView(View):
    template_name = 'video.html'
    def get(self,request,video_id):
        video_by_id = Video.objects.get(id=video_id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        video_by_id.path = 'http://localhost:8000/get_video/'+ video_by_id.path
        context = {'video':video_by_id}
        if request.user.is_authenticated == True:
            print('User Signed in')
            form = CommentForm()
            context['form'] = form

        comments = Comment.objects.filter(video__id=video_id).order_by('-datetime')[:5]
        print(comments)
        context['comments'] = comments
        return render(request,self.template_name,context)

class LoginView(View):
    template_name = 'login.html'

    def get(self,request):
        if request.user.is_authenticated:
            print("Alredy LoggedIn, redirecting!")
            return HttpResponseRedirect("/")
        form = LoginForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            print("Successful login")
            return HttpResponseRedirect("/")
        else:
            print("unsuccessful login")
            return HttpResponseRedirect("/login/")

class CommentView(View):
    template_name = 'comment.html'

    def post(self,request):
        form = CommentForm(request.POST)
        if form.is_valid():
            text = request.POST['text']
            video_id = request.POST['video']
            video = Video.objects.get(id=video_id)
            new_comment = Comment(text = text,user=request.user,video=video)
            new_comment.save()
            return HttpResponseRedirect('/video/{}'.format(str(video_id)))
        return HttpResponse('This is Register. POST req!')



class RegisterView(View):
    template_name = 'register.html'

    def get(self,request):
        if request.user.is_authenticated:
            print("Alredy LoggedIn, redirecting!")
            return HttpResponseRedirect("/")
        form = RegisterForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username = username,password=password,email=email)
            new_user.set_password(password)
            new_user.save()
            print(new_user)
            return HttpResponseRedirect('/login/')
        return HttpResponse('This is Register. POST req!')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self,request):
        if request.user.is_authenticated == False:
            return HttpResponseRedirect("/")
        variable = 'new video'
        form = NewVideoForm()
        return render(request,self.template_name,{'variable':variable,'form':form})

    def post(self,request):
        form = NewVideoForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            file = request.FILES['file']
            print(title)
            new_video = Video(title=title,description=description,user=request.user,path=file)
            new_video.save()
            return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:
            return HttpResponse("Invalid Form")

class LogOutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')
