from django.urls import path

from .views import *
from . import views

#podcast cate
podcast_cate_get_all_api = PodcastCateMVS.as_view({
    'get':'podcast_cate_get_all_api'
})

podcast_cate_add_api = PodcastCateMVS.as_view({
    'post':'podcast_cate_add_api'
})

podcast_cate_update_api = PodcastCateMVS.as_view({
    'patch':'podcast_cate_update_api'
})

podcast_cate_delete_api = PodcastCateMVS.as_view({
    'delete':'podcast_cate_delete_api'
})

#podcast author

urlpatterns = [
    #podcast cate
    path('podcast_cate_get_all_api/', podcast_cate_get_all_api),
    path('podcast_cate_add_api/', podcast_cate_add_api),
    path('podcast_cate_update_api/', podcast_cate_update_api),
    path('podcast_cate_delete_api/', podcast_cate_delete_api),

    #podcast author
]