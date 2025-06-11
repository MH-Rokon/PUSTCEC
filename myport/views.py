from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Profile, Experience, Education, Skill, Project, Research
from .forms import ProfileForm, ExperienceForm, EducationForm, SkillForm, ProjectForm, ResearchForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import FeaturedItem
from .forms import FeaturedItemForm


# Profile Section

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})



# Add Featured Content
@login_required
def add_featured(request):
    if request.method == 'POST':
        form = FeaturedItemForm(request.POST, request.FILES)
        if form.is_valid():
            featured = form.save(commit=False)
            featured.user = request.user  # Link featured content to the logged-in user
            featured.save()
            return redirect('profile_view')  # Redirect to profile view after adding
    else:
        form = FeaturedItemForm()
    return render(request, 'add_feature.html', {'form': form})

# Edit Featured Content
@login_required
def edit_featured(request, pk):
    featured = get_object_or_404(FeaturedItem, pk=pk)
    if request.method == 'POST':
        form = FeaturedItemForm(request.POST, request.FILES, instance=featured)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to profile view after editing
    else:
        form = FeaturedItemForm(instance=featured)
    return render(request, 'edit_feature.html', {'form': form})

# Delete Featured Content

@login_required
def add_experience(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.profile = profile
            experience.save()
            return redirect('profile_view')
    else:
        form = ExperienceForm()
    return render(request, 'add_experience.html', {'form': form})

@login_required
def edit_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'edit_experience.html', {'form': form})

# Education Section
@login_required
def add_education(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.profile = profile
            education.save()
            return redirect('profile_view')
    else:
        form = EducationForm()
    return render(request, 'add_education.html', {'form': form})

@login_required
def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = EducationForm(instance=education)
    return render(request, 'edit_education.html', {'form': form})

# Skills Section
@login_required
def add_skills(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = profile
            skill.save()
            return redirect('profile_view')
    else:
        form = SkillForm()
    return render(request, 'add_skills.html', {'form': form})

@login_required
def edit_skills(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'edit_skills.html', {'form': form})

# Projects Section
@login_required
def add_projects(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = profile
            project.save()
            return redirect('profile_view')
    else:
        form = ProjectForm()
    return render(request, 'add_projects.html', {'form': form})

@login_required
def edit_projects(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_projects.html', {'form': form})

# Research Section
@login_required
def add_research(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ResearchForm(request.POST)
        if form.is_valid():
            research = form.save(commit=False)
            research.profile = profile
            research.save()
            return redirect('profile_view')
    else:
        form = ResearchForm()
    return render(request, 'add_research.html', {'form': form})

@login_required
def edit_research(request, pk):
    research = get_object_or_404(Research, pk=pk)
    if request.method == 'POST':
        form = ResearchForm(request.POST, instance=research)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ResearchForm(instance=research)
    return render(request, 'edit_research.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile_view')
        messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
