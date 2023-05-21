from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    # fields = ['name', 'username', 'email', 'password1', 'password2']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'body']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
