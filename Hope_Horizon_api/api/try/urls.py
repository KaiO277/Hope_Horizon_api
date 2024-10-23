from django.urls import path

from .views import *
from . import views

try_add_api = TryMVS.as_view({
    'post':'try_add_api'
})

try_get_all_api = TryMVS.as_view({
    'get':'try_get_all_api'
})

urlpatterns = [
    path('try_add_api/', try_add_api),
    path('try_get_all_api/', try_get_all_api), 
]