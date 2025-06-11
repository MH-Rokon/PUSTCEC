from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Certification, Achievement, Publication, VolunteerExperience, Award_and_Honor
from .forms import CertificationForm, AchievementForm, PublicationForm, VolunteerExperienceForm, Award_and_HonorForm

# Profile Section
@login_required
def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.profile = request.user.profile  # Link to logged-in user's profile
            certification.save()
            return redirect('profile_view')
    else:
        form = CertificationForm()
    return render(request, 'add_certification.html', {'form': form})

@login_required
def edit_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk)
    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = CertificationForm(instance=certification)
    return render(request, 'edit_certification.html', {'form': form})

# Achievements Section
@login_required
def add_achievement(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.profile = request.user.profile  # Link to logged-in user's profile
            achievement.save()
            return redirect('profile_view')
    else:
        form = AchievementForm()
    return render(request, 'add_achievement.html', {'form': form})

@login_required
def edit_achievement(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'edit_achievement.html', {'form': form})

# Award and Honor Section
@login_required
def add_award_and_honor(request):
    if request.method == 'POST':
        form = Award_and_HonorForm(request.POST, request.FILES)
        if form.is_valid():
            award_and_honor = form.save(commit=False)
            award_and_honor.profile = request.user.profile  # Link to logged-in user's profile
            award_and_honor.save()
            return redirect('profile_view')
    else:
        form = Award_and_HonorForm()
    return render(request, 'add_award_and_honor.html', {'form': form})

@login_required
def edit_award_and_honor(request, pk):
    award_and_honor = get_object_or_404(Award_and_Honor, pk=pk)
    if request.method == 'POST':
        form = Award_and_HonorForm(request.POST, request.FILES, instance=award_and_honor)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = Award_and_HonorForm(instance=award_and_honor)
    return render(request, 'edit_award_and_honor.html', {'form': form})

# Publications Section
@login_required
def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.profile = request.user.profile  # Link to logged-in user's profile
            publication.save()
            return redirect('profile_view')
    else:
        form = PublicationForm()
    return render(request, 'add_publication.html', {'form': form})

@login_required
def edit_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'edit_publication.html', {'form': form})

# Volunteer Experience Section
@login_required
def add_volunteer_experience(request):
    if request.method == 'POST':
        form = VolunteerExperienceForm(request.POST)
        if form.is_valid():
            volunteer_experience = form.save(commit=False)
            volunteer_experience.profile = request.user.profile  
            volunteer_experience.save()
            return redirect('profile_view')
    else:
        form = VolunteerExperienceForm()
    return render(request, 'add_volunteer_experience.html', {'form': form})

@login_required
def edit_volunteer_experience(request, pk):
    volunteer_experience = get_object_or_404(VolunteerExperience, pk=pk)
    if request.method == 'POST':
        form = VolunteerExperienceForm(request.POST, instance=volunteer_experience)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = VolunteerExperienceForm(instance=volunteer_experience)
    return render(request, 'edit_volunteer_experience.html', {'form': form})
