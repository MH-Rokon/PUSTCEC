from django.urls import path
from . import views

urlpatterns = [
    path('exe/', views.executive_view, name='exe'),
    path('pre-exe/', views.pre_exe_view, name='pre_exe'),
    path('f-mem/', views.fmember_view, name='f_member'),
    path('external/', views.external_view, name='external'),
    path('internal/', views.internal_view, name='internal'),
]
