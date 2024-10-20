from django.contrib import admin
from django.conf.urls import include
from django.urls import path


# from api.views import SecureFile
# from api.views import protected_media_view, textfile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 


]
