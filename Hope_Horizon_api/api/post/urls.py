from django.urls import path

from .views import *
from . import views

#post category
post_cate_get_all_api = PostCateMVS.as_view({
    'get': 'post_cate_get_all_api',
})

post_cate_add_api = PostCateMVS.as_view({
    'post': 'post_cate_add_api',
})

post_cate_update_api = PostCateMVS.as_view({
    'patch':'post_cate_update_api'
})

post_cate_delete_api = PostCateMVS.as_view({
    'delete':'post_cate_delete_api'
})

#post author
post_author_add_api = PostAuthorMVS.as_view({
    'post':'post_author_add_api'
})

post_author_get_all_api = PostAuthorMVS.as_view({
    'get':'post_author_get_all_api'
})

post_author_get_by_id_api = PostAuthorMVS.as_view({
    'get': 'post_author_get_by_id_api'
})

post_author_update_api = PostAuthorMVS.as_view({
    'patch':'post_author_update_api'
})

post_author_delete_api = PostAuthorMVS.as_view({
    'delete':'post_author_delete_api'
})

#index
post_index_get_all_api = PostIndexMVS.as_view({
    'get':'post_index_get_all_api'
})

post_index_get_all_by_post_cate_id_api = PostIndexMVS.as_view({
    'get':'post_index_get_all_by_post_cate_id_api'
})

post_index_add_api = PostIndexMVS.as_view({
    'post':'post_index_add_api'
})

post_index_delete_api = PostIndexMVS.as_view({
    'delete':'post_index_delete_api'
})


urlpatterns = [
    path('post_index_get_all_api/', post_index_get_all_api),
    path('post_index_get_all_by_post_cate_id_api/<int:post_cate_id>',post_index_get_all_by_post_cate_id_api),
    path('post_index_add_api/', post_index_add_api),
    path('post_index_delete_api/', post_index_delete_api),

    #post_cate
    path('post_cate_get_all_api/', post_cate_get_all_api),
    path('post_cate_add_api/', post_cate_add_api),
    path('post_cate_update_api/', post_cate_update_api),
    path('post_cate_delete_api/', post_cate_delete_api),

    #post_author
    path('post_author_get_all_api/', post_author_get_all_api),
    path('post_author_add_api/', post_author_add_api),
    path('post_author_get_by_id_api/<int:id>', post_author_get_by_id_api),
    path('post_author_update_api/', post_author_update_api),
    path('post_author_delete_api/', post_author_delete_api),
]