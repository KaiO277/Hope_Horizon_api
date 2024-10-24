from rest_framework import serializers
from api.models import *
from api.submodels import *

# class PostCateSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PostCate
#         fields = '__all__'

# class PostIndexSerializers(serializers.ModelSerializer):
#     post_cate = PostCateSerializers(required=False)
    
#     class Meta:
#         model = PostIndex
#         fields = '__all__'

    