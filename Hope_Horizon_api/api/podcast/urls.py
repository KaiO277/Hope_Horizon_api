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
podcast_author_get_all_api = PodcastAuthorMVS.as_view({
    'get':'podcast_author_get_all_api'
})

podcast_author_add_api = PodcastAuthorMVS.as_view({
    'post':'podcast_author_add_api'
})

podcast_author_update_api = PodcastAuthorMVS.as_view({
    'patch':'podcast_author_update_api'
})

podcast_author_delete_api = PodcastAuthorMVS.as_view({
    'delete':'podcast_author_delete_api'
})

#podcast index
podcast_index_get_all_api = PodcastIndexMVS.as_view({
    'get':'podcast_index_get_all_api'
})

podcast_index_update_api = PodcastIndexMVS.as_view({
    'patch':'podcast_index_update_api'
})

podcast_index_delete_api = PodcastIndexMVS.as_view({
    'delete':'podcast_index_delete_api'
})

podcast_index_add_api = PodcastIndexMVS.as_view({
    'post': 'podcast_index_add_api'
})

urlpatterns = [
    #podcast cate
    path('podcast_cate_get_all_api/', podcast_cate_get_all_api),
    path('podcast_cate_add_api/', podcast_cate_add_api),
    path('podcast_cate_update_api/', podcast_cate_update_api),
    path('podcast_cate_delete_api/', podcast_cate_delete_api),

    #podcast author
    path('podcast_author_get_all_api/', podcast_author_get_all_api),
    path('podcast_author_add_api/',podcast_author_add_api),
    path('podcast_author_update_api/', podcast_author_update_api),
    path('podcast_author_delete_api/', podcast_author_delete_api),

    #podcast index
    path('podcast_index_get_all_api/', podcast_index_get_all_api),
    path('podcast_index_add_api/', podcast_index_add_api),
    path('podcast_index_update_api/', podcast_index_update_api),
    path('podcast_index_delete_api/', podcast_index_delete_api),
]