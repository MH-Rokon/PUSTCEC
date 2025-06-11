from django.shortcuts import render
from .models import ClubMember

def executive_view(request):
    # Fetch all executive members from the database
    executives = ClubMember.objects.filter(role='Executive', is_active=True, is_visible_on_website=True)
    return render(request, 'executive_list.html', {'executives': executives})

def pre_exe_view(request):
    # Fetch all pre-executive members from the database
    pre_executives = ClubMember.objects.filter(role='Pre-Executive', is_active=True, is_visible_on_website=True)
    return render(request, 'pre_executive_list.html', {'pre_executives': pre_executives})

def fmember_view(request):
    # Fetch all founding members from the database
    founding_members = ClubMember.objects.filter(role='Founder', is_active=True, is_visible_on_website=True)
    return render(request, 'founding_member_list.html', {'founding_members': founding_members})

def external_view(request):
    # Fetch external advisors (members with 'External Advisor' role)
    external_advisors = ClubMember.objects.filter(role='External Advisor', is_active=True, is_visible_on_website=True)
    return render(request, 'external_advisor_list.html', {'external_advisors': external_advisors})

def internal_view(request):
    # Fetch internal members (those with 'Internal' role)
    internal_members = ClubMember.objects.filter(role='Internal Advisor', is_active=True, is_visible_on_website=True)
    return render(request, 'internal_advisor_list.html', {'internal_members': internal_members})
