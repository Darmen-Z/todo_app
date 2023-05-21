from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import Task, User
from .forms import TaskForm, MyUserCreationForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {'form': form}
    return render(request, 'base/login_register.html', context=context)


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = MyUserCreationForm(instance=user)

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, instance=user)
        # form = MyUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'base/update_user.html', {'form': form})


@login_required(login_url='login')
def home(request):
    tasks = Task.objects.all().filter(user=request.user)

    context = {'tasks': tasks}
    return render(request, 'base/home.html', context=context)


@login_required(login_url='login')
def task(request, pk):
    task = Task.objects.get(id=pk)

    if request.user != task.user:
        return HttpResponse('You are not allowed here!!!')

    context = {'task': task}
    return render(request, 'base/task.html', context=context)


@login_required(login_url='login')
def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user

        Task.objects.create(
            title=title,
            body=body,
            user=user
        )
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/task_form.html', context=context)


@login_required(login_url='login')
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.user != task.user:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.body = request.POST.get('body')
        task.user = request.user
        task.save()
        return redirect('home')
    context = {'task': task, 'form': form}
    return render(request, 'base/task_form.html', context=context)


@login_required(login_url='login')
def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.user != task.user:
        return HttpResponse('You are not allowed here!!!')

    if request.method == 'POST':
        task.delete()
        return redirect('home')
    context = {'obj': task}
    return render(request, 'base/delete.html', context=context)
