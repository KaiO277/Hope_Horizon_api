from rest_framework import serializers
from api.models import *
from api.submodels import *

class PostCateSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PostCate
        fields = '__all__'

    def add(self,request):
        try:
            title = self.validated_data['title']

            return PostCate.objects.create(
                title=title
            )
        except Exception as error:
            print("PostCateSerializer_add_error: ", error)
            return None

    def update(self,request):
        try:
            print("post_cate_id: ",self.validated_data['title'])
            post_cate_id = self.validated_data['id']
            title = self.validated_data['title']

            post_cate = PostCate.objects.get(pk=post_cate_id)

            post_cate.title = title
            post_cate.save()
            return post_cate
        except PostCate.DoesNotExist:
            return None
        except Exception as error:
            print("PostCateSerializer_update_error: ", error)
            return None

    def delete(self, request):
        try:
            model = PostCate.objects.get(pk=self.validated_data['id'])
            model.delete()
            return True
        except Exception as error:
            print("PostCateSerializers_delete_error: ",error)
            return None

class PostAuthorSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PostAuthor
        fields = '__all__'

    def add(self, request):
        try:
            name = self.validated_data['name']
            return PostAuthor.objects.create(
                name = name
            )
        except Exception as error:
            print("PostAuthorSerializers_add_error: ", error)
            return None
        
    def update(self,request):
        try:
            post_author_id = self.validated_data['id']
            name = self.validated_data['name']

            post_author = PostAuthor.objects.get(pk=post_author_id)

            post_author.name = name
            post_author.save()
            return post_author
        except PostAuthor.DoesNotExist:
            return None
        except Exception as error:
            print("PostCateSerializer_update_error: ", error)
            return None

    def delete(self, request):
        try:
            model = PostAuthor.objects.get(pk=self.validated_data['id'])
            model.delete()
            return True
        except Exception as error:
            print("PostauthorSerializers_delete_error: ",error)
            return None

class PostIndexSerializers(serializers.ModelSerializer):
    post_cate = PostCateSerializers(required=False)
    post_author = PostAuthorSerializers(required = False)
    
    class Meta:
        model = PostIndex
        fields = '__all__'


    