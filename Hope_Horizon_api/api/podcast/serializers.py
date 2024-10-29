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
            model = PodcastCate.objects.get(pk=self.validated_data['id'])
            model.delete()
            return True 
        except Exception as error:
            print("PodcastCateSerializer_delete_error: ", error)
            return None

class PodcastAuthorSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PodcastAuthor
        fields = '__all__'

    def add(self, request):
        try:
            name = self.validated_data['name']

            return PodcastAuthor.objects.create(name=name)
        except Exception as error:
            print("PodcastAuthorSerializers_add_error: ", error)
            return None
    def update(self, request):
        try:
            podcast_author_id = self.validated_data['id']
            name = self.validated_data['name']

            podcast_author = PodcastAuthor.objects.get(pk=podcast_author_id)

            podcast_author.name = name
            podcast_author.save()
            return podcast_author
        except PodcastAuthor.DoesNotExist:
            print("PodcastAuthorSerializers_update_DoesNotExist ")
            return None
        except Exception as error:
            print("PodcastAuthorSerializers_update_error: ", error)
            return None
        
    def delete(self, request):
        try:
            podcast_author_id = self.validated_data['id']
            podcast_author = PodcastAuthor.objects.get(pk=podcast_author_id)
            podcast_author.delete()
            return True
        except Exception as error:
            print("PodcastAuthorSerializers_delete_error: ", error)
            return None

class PodcastIndexSerializers(serializers.ModelSerializer):
    # post_cate = PodcastIndex1(required=False)
    
    class Meta:
        model = PodcastIndex1
        fields = '__all__'

    