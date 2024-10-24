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

#index
post_index_get_all_api = PostIndexMVS.as_view({
    'get':'post_index_get_all_api'
})

urlpatterns = [
    path('post_index_get_all_api/', post_index_get_all_api),
    path('post_cate_get_all_api/', post_cate_get_all_api),
    path('post_cate_add_api/', post_cate_add_api),
    path('post_cate_update_api/', post_cate_update_api),
]