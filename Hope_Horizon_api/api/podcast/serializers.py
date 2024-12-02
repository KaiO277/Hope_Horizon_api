from rest_framework import serializers
from api.models import *
from api.submodels import *
from api.podcast.utils import generate_unique_filename 

class PodcastCateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PodcastCate
        fields = '__all__'

    def add(self, request):
        try:
            title = self.validated_data.get('title')
            
            if PodcastCate.objects.filter(title=title).exists():
                # Handle duplicate case
                print("PodcastCateSerializers_add_error: Duplicate title")
                return None
            
            return PodcastCate.objects.create(title=title)

        except Exception as e:
            print("PodcastCateSerializer_add_error: ", e)
            raise
        
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
            # Extract the name from validated data
            name = self.validated_data.get('name')
            
            # Check if an author with the same name already exists
            if PodcastAuthor.objects.filter(name=name).exists():
                print("PodcastAuthorSerializers_add_error: Duplicate name")
                return None
            
            # Create and return the new PodcastAuthor instance
            return PodcastAuthor.objects.create(name=name)

        except Exception as error:
            # Log the error and return None
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
    podcast_cate = PodcastCateSerializers(required=False)
    podcast_author = PodcastAuthorSerializers(required=False)
    id = serializers.IntegerField(required=False)
    podcast_cate_id = serializers.IntegerField(required=False)
    podcast_author_id = serializers.IntegerField(required=False)
    
    class Meta:
        model = PodcastIndex1
        fields = '__all__'

    def add(self, request):
        try:
            # Lấy dữ liệu từ request
            title = self.validated_data['title']
            image_title = self.validated_data.get('image_title')  # Có thể không có
            podcast_cate_id = self.validated_data.get('podcast_cate_id')  # Có thể không có
            podcast_author_id = self.validated_data.get('podcast_author_id')  # Có thể không có
            content = self.validated_data.get('content')  # Có thể không có

            # Tạo tên podcast duy nhất từ title
            unique_title = generate_unique_filename(title, content)

            # Tạo và lưu PodcastIndex1
            podcast = PodcastIndex1.objects.create(
                title=title,  # Lưu tên duy nhất
                image_title=image_title,
                podcast_cate_id=podcast_cate_id,
                podcast_author_id=podcast_author_id,
                content=unique_title
            )

            return podcast

        except Exception as error:
            print("PodcastIndexSerializers_add_error: ", error)
            return None
        
    def delete(self, request):
        try:
            model = PodcastIndex1.objects.get(pk=self.validated_data['id'])
            model.delete()
            return True
        except Exception as error:
            print("PodcastIndexSerializers_delete_error: ", error)
            return None
        
    def update(self, request):
        try:
            title = self.validated_data['title']
            image_title = self.validated_data['image_title']
            podcast_cate_id = self.validated_data['podcast_cate_id']
            podcast_author_id = self.validated_data['podcast_author_id']
            content = self.validated_data['content']
            podcast_index_id = self.validated_data['id']

            podcast_index = PodcastIndex1.objects.get(pk=podcast_index_id)

            podcast_index.title = title
            podcast_index.image_title = image_title
            podcast_index.podcast_cate_id = podcast_cate_id
            podcast_index.podcast_author_id = podcast_author_id
            podcast_index.content = content
            podcast_index.save()
            return podcast_index
        except PodcastIndex1.DoesNotExist:
            print("PodcastIndexSerializers_update_error: PodcastIndex1 does not exist")
            return None
        except Exception as error:
            print("PodcastIndexSerializers_update_error: ", error)
            return None