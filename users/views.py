from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile, skills, Message
from projects.models import project
from .forms import editForm, skill, formmessage
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def profile(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print('search:', search_query)

    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) | Q(short_intro__icontains=search_query))

    context = {"profile": profiles,
               "search_query": search_query}
    return render(request, "users/profiles.html", context)


def userprofile(request, pk):
    profile = Profile.objects.get(id=pk)
  #  projects = project.objects.get(id=pk)

    ##topskills = profile.skills_set.exclude(description__exact="")

    #otherskills = profile.skill_set.filter(description="")

    #topskills = profile.skills_set.exclude(description__exact="")

    skills = profile.skills_set.all()

    context = {"profile": profile, "skills": skills}

    return render(request, "users/user-profile.html", context)


@login_required(login_url="log-project")
def useraccount(request):
    profile = request.user.profile

    skills = profile.skills_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}

    return render(request, 'users/account.html', context)


def editprofile(request, pk):

    profile = Profile.objects.get(id=pk)

    editform = editForm(instance=profile)

    if request.method == 'POST':
        editform = editForm(request.POST, request.FILES, instance=profile)
        if editform.is_valid():
            editform.save()
            return redirect('user-account')

    context = {'form': editform}
    return render(request, 'users/editprofile.html', context)


@login_required(login_url="log-project")
def skillform(request):

    profile = request.user.profile
    form = skill()

    if request.method == 'POST':

        form = skill(request.POST)

        if form.is_valid():
            skillss = form.save(commit=False)
            skillss.owner = profile
            skillss.save()

            return redirect('user-account')

    context = {"skills": form}
    return render(request, 'users/skill_form.html', context)


def editskills(request, pk):
    profile = request.user.profile
    form = profile.skills_set.get(id=pk)

    forms = skill(instance=form)

    if request.method == 'POST':
        forms = skill(request.POST, instance=form)

        if forms.is_valid():
            forms.save()
            return redirect('user-account')

    context = {"skills": forms}

    return render(request, 'users/skill_form.html', context)


def deleteskills(request, pk):
    profile = request.user.profil

    form = profile.skills_set.get(id=pk)

    if request.method == 'POST':

        form.delete()

        return redirect('user-account')

    context = {"skillss": form}

    return render(request, 'users/delete_skill.html', context)


def sendMessage(request, pk):

    profile = Profile.objects.get(id=pk)
    profiles = request.user.profile

    form = formmessage()

    if request.method == "POST":
        form = formmessage(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.sender = profiles
            forms.recipient = profile
            forms.save()
            return redirect("user-profile", pk)

    context = {"form": form, 'profile': profile}

    return render(request, 'users/sendmessage.html', context)


def inbox(request):
    profile = request.user.profile

    message = Message.objects.filter(recipient=profile)

    context = {'message': message}

    return render(request, 'users/inbox.html', context)
