from django.urls import path

from .views import *
from . import views

post_index_get_all_api = PostIndexMVS.as_view({
    'get':'post_index_get_all_api'
})

urlpatterns = [
    path('post_index_get_all_api/', post_index_get_all_api),
]