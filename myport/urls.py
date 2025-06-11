from django.urls import path
from . import views

urlpatterns = [
    # Profile View
    path('profile/', views.profile_view, name='profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('featured/add/', views.add_featured, name='add_featured'),
    path('featured/edit/<int:pk>/', views.edit_featured, name='edit_featured'),
    # Experience Section
    path('add_experience/', views.add_experience, name='add_experience'),
    path('edit_experience/<int:pk>/', views.edit_experience, name='edit_experience'),

    # Education Section
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:pk>/', views.edit_education, name='edit_education'),

    # Skills Section
    path('add_skills/', views.add_skills, name='add_skills'),
    path('edit_skills/<int:pk>/', views.edit_skills, name='edit_skills'),

    # Projects Section
    path('add_projects/', views.add_projects, name='add_projects'),
    path('edit_projects/<int:pk>/', views.edit_projects, name='edit_projects'),

    # Research Section
    path('add_research/', views.add_research, name='add_research'),
    path('edit_research/<int:pk>/', views.edit_research, name='edit_research'),

    # # Certifications Section
    # path('add_certification/', views.add_certification, name='add_certification'),
    # path('edit_certification/<int:pk>/', views.edit_certification, name='edit_certification'),

    # # Achievements Section
    # path('add_achievement/', views.add_achievement, name='add_achievement'),
    # path('edit_achievement/<int:pk>/', views.edit_achievement, name='edit_achievement'),

    # # Publications Section
    # path('add_publication/', views.add_publication, name='add_publication'),
    # path('edit_publication/<int:pk>/', views.edit_publication, name='edit_publication'),

    # # Volunteer Experience Section
    # path('add_volunteer_experience/', views.add_volunteer_experience, name='add_volunteer_experience'),
    # path('edit_volunteer_experience/<int:pk>/', views.edit_volunteer_experience, name='edit_volunteer_experience'),

    # Authentication Views
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
