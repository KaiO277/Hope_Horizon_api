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
        
    def update(self, request):
        try:
            podcast_cate_id = self.validated_data['id']
            title = self.validated_data['title']

            podcast_cate = PodcastCate.objects.get(pk=podcast_cate_id)

            podcast_cate.title = title
            podcast_cate.save()
            return podcast_cate
        except PodcastCate.DoesNotExist:
            print("PodcastCateSerializer_update_DoesNotExist: ")
            return None
        except Exception as error:
            print("PodcastCateSerializer_update_error: ", error)
            return None
        
    def delete(self, request):
        try:
            print(self.validated_data['id'])
            model = PodcastCate.objects.get(pk=self.validated_data['id'])
            print(model)
            model.delete()
            return True 
        except Exception as error:
            print("PodcastCateSerializer_delete_error: ", error)
            return None


# class PostIndexSerializers(serializers.ModelSerializer):
#     post_cate = PostCateSerializers(required=False)
    
#     class Meta:
#         model = PostIndex
#         fields = '__all__'

    