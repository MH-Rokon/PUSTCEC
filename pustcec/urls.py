from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Home page URL (you can adjust this as needed)
    path('', views.index, name='index'),

    # Include the URLs from the 'events' app
    path('event/', include('events.urls')),  
    path('contact/', include('contacts.urls')),      
    path('myport/', include('myport.urls')),  # This is for the first myport app
    path('myport2/', include('myport2.urls')),  # This is for the second myport app
    path('gpanel/', include('gpanel.urls')),  # Ensure gpanel.urls is valid
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
