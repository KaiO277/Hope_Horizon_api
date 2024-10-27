from django.urls import path

from .views import *
from . import views

podcast_cate_get_all_api = PodcastCateMVS.as_view({
    'get':'podcast_cate_get_all_api'
})

podcast_cate_add_api = PodcastCateMVS.as_view({
    'post':'podcast_cate_add_api'
})

urlpatterns = [
    path('podcast_cate_get_all_api/', podcast_cate_get_all_api),
    path('podcast_cate_add_api/', podcast_cate_add_api),
]