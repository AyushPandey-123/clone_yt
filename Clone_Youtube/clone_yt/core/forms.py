from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'Username',max_length = 20)
    password = forms.CharField(label = 'Password',max_length = 20)

class RegisterForm(forms.Form):
    username = forms.CharField(label = 'Username',max_length = 20)
    password = forms.CharField(label = 'Password',max_length = 20)
    email = forms.CharField(label = "Your Email",max_length = 20)

class NewVideoForm(forms.Form):
    title = forms.CharField(label = 'Title',max_length = 20)
    description = forms.CharField(label = 'Description',max_length = 100)
    file = forms.FileField()

class CommentForm(forms.Form):
    text = forms.CharField(label = 'Text',max_length = 200)
    video = forms.IntegerField(widget=forms.HiddenInput(),initial=1)
