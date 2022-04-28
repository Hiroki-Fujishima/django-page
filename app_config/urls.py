from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('app_folder/', include('app_folder.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)