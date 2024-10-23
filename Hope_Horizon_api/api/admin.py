from django.contrib import admin
from .submodels.models_post import *
from .submodels.models_try import *

# Register your models here.
admin.site.register(PostCate)
admin.site.register(PostIndex)
admin.site.register(Try)