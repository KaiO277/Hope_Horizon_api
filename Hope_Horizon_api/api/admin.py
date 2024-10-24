from django.contrib import admin
from .submodels.models_post import *
from .submodels.models_try import *
from .submodels.models_podcast import *

# Register your models here.
#post
admin.site.register(PostCate)
admin.site.register(PostIndex)
admin.site.register(PostAuthor)
admin.site.register(PostViews)

#podcast
admin.site.register(PodcastCate)
admin.site.register(PodcastIndex1)
admin.site.register(PodcastAuthor)
admin.site.register(PodcastIndex2)
admin.site.register(PodcastViews)

# try 
admin.site.register(Try)