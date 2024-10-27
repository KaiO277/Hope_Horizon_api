from rest_framework import serializers
from api.models import *
from api.submodels import *

class PodcastCateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PodcastCate
        fields = '__all__'

    def add(self, request):
        try:
            title = self.validated_data['title']
            return PodcastCate.objects.create(title=title)
        except Exception as e:
            print("PodcastCateSerializer_add_error: ", e)
            return None


# class PostIndexSerializers(serializers.ModelSerializer):
#     post_cate = PostCateSerializers(required=False)
    
#     class Meta:
#         model = PostIndex
#         fields = '__all__'

    