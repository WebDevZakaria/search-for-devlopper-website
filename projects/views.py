from typing import ContextManager
from django.shortcuts import redirect, render
from django.http import HttpResponse

from users.models import Profile
from .models import formation, project
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

import projects
from .forms import projectform, formationform, formuser
# Create your views here.


def pro(request):

    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')
        print('search:', search)

    projects = project.objects.filter(
        Q(title__icontains=search) |
        Q(description__icontains=search) |
        Q(owner__name__icontains=search)

    )
    

    page = request.GET.get('page')
    result = 3

    paginator = Paginator(projects, result)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    context = {"proj": projects, "search": search, "paginator": paginator}

    return render(request, 'projects/projects.html', context)


def sngle(request, pk):

    projectObj = project.objects.get(id=pk)

    return render(request, 'projects/singleproject.html', {'project': projectObj})


@login_required(login_url="log-project")
def createproject(request):
    profile = request.user.profile

    form = projectform()
   # tag = project.tags.all()

    if request.method == 'POST':
        form = projectform(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('pro')
    context = {'form': form}

    return render(request, 'projects/project_form.html', context)


@login_required(login_url="log-project")
def updateproject(request, pk):
    profile = request.user.profile

    projects = profile.project_set.get(id=pk)
    form = projectform(instance=projects)

    if request.method == 'POST':
        form = projectform(request.POST, request.FILES, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('pro')
    context = {'form': form}

    return render(request, 'projects/project_form.html', context)


@login_required(login_url="log-project")
def deleteproject(request, pk):
    projects = project.objects.get(id=pk)
    if request.method == "POST":
        projects.delete()
        return redirect('pro')

    context = {"object": projects}

    return render(request, 'projects/delete_object.html', context)


def logproject(request):

    page = 'register'

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            formations = User.objects.get(username=username)
        except:
            messages.error(request, 'user name not found')

        formations = authenticate(
            request, username=username, password=password)

        if formations is not None:
            login(request, formations)
            return redirect("pro")
        else:
            messages.error(request, 'password  is requered')
    return render(request, 'projects/login.html')


def welcomeproject(request):

    return render(request, 'projects/welcome.html')


def logoutproject(request):
    logout(request)
    return redirect("log-project")


def regproject(request):

    page = 'register'

    form = formuser()

    if request.method == 'POST':
        form = formuser(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.username == form.username.lower()

            form.save()

            return redirect("log-project")

        else:
            messages.error(request, "an error occorded")

    context = {"page": page, "form": form}

    return render(request, 'projects/login.html', context)
