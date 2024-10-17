from django.contrib import admin
from .submodels.models_post import *

# Register your models here.
admin.site.register(PostCate)
admin.site.register(PostIndex)