from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


# from api.views import SecureFile
# from api.views import protected_media_view, textfile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
