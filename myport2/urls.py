from django.urls import path
from . import views

urlpatterns = [
   
    # Certifications Section
    path('add_certification/', views.add_certification, name='add_certification'),
    path('edit_certification/<int:pk>/', views.edit_certification, name='edit_certification'),

    # Achievements Section
    path('add_achievement/', views.add_achievement, name='add_achievement'),
    path('edit_achievement/<int:pk>/', views.edit_achievement, name='edit_achievement'),
    # award_and_honor Section
    path('add_award_and_honor/', views.add_award_and_honor, name='add_award_and_honor'),
    path('edit_award_and_honor/<int:pk>/', views.edit_award_and_honor, name='edit_award_and_honor'),

    # Publications Section
    path('add_publication/', views.add_publication, name='add_publication'),
    path('edit_publication/<int:pk>/', views.edit_publication, name='edit_publication'),

    # Volunteer Experience Section
    path('add_volunteer_experience/', views.add_volunteer_experience, name='add_volunteer_experience'),
    path('edit_volunteer_experience/<int:pk>/', views.edit_volunteer_experience, name='edit_volunteer_experience'),

]
