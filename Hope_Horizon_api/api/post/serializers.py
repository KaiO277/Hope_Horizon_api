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

class PostAuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostAuthor
        fields = '__all__'

class PostIndexSerializers(serializers.ModelSerializer):
    post_cate = PostCateSerializers(required=False)
    post_author = PostAuthorSerializers(required = False)
    
    class Meta:
        model = PostIndex
        fields = '__all__'


# class PracticeCourseSerializer(serializers.ModelSerializer):
#     course_category_level2 = CourseCategoryLevel2Serializers(required=False)
#     id = serializers.IntegerField(required=False)
#     course_category_level2_id = serializers.IntegerField(required=False)
#     title = serializers.CharField(required=False)
#     order = serializers.IntegerField(required = False)
#     user_mentor = UserMentorBasicSerializer(required=False)

#     class Meta:
#         model = PracticeCourse
#         fields = '__all__'

#     def slug_validate_add(self, request):
#         title = self.validated_data['title']
#         slug = slugify(unidecode(title))
#         filterExist = PracticeCourse.objects.filter(slug=slug)
#         if len(filterExist)>0:
#             return False
#         return True 
    
#     def slug_validate_update(self,request):
#         id = self.validated_data['id']
#         name =self.validated_data['title']
#         slug = slugify(unidecode(name))
#         filterExist = PracticeCourse.objects.filter(slug=slug).exclude(id=id)
#         if len(filterExist) > 0:
#             return False
#         return True 
    
#     def add(self, request):
#         try:
#             title = self.validated_data['title']
#             slug = slugify(unidecode(title))
#             order = self.validated_data['order']
#             course_category_level2_id = self.validated_data['course_category_level2_id']
#             user_mentor_id = request.user.id

#             return PracticeCourse.objects.create(
#                 title = title,
#                 slug = slug,
#                 order = order,
#                 course_category_level2_id = course_category_level2_id,
#                 user_mentor_id = user_mentor_id
#             )        
#         except Exception as error:
#             print("PracticeCourseSerializer_add_error: ", error)    
#             return None

#     def delete(self, request):
#         try:
#             model = PracticeCourse.objects.get(pk=self.validated_data['id'])
#             model.delete()
#             return True
#         except Exception as error:
#             print("PracticeCourse_delete_error: ", error)
#             return None             

#     def update(self, request):
#         try:
#             practice_course_id = self.validated_data['id']
#             title = self.validated_data['title']
#             slug = slugify(unidecode(title))
#             order = self.validated_data['order']
#             num_of_life = self.validated_data['num_of_life']
#             description = self.validated_data['description']
             
#             practice_course = PracticeCourse.objects.get(pk=practice_course_id)

#             practice_course.title = title
#             practice_course.slug = slug
#             practice_course.order = order
#             practice_course.description = description
#             practice_course.num_of_life = num_of_life       

#             practice_course.save()
#             return practice_course
#         except Exception as error:
#             print("PracticeCourseSerializer_update_error: ", error)
#             return None 
                        
#     def updateStatusPublish(self, request):
#         try:
#             id = self.validated_data['id']
#             is_display = self.validated_data['is_display']
#             model = PracticeCourse.objects.get(pk=id)
#             model.is_display = is_display
#             model.save()
#             return model 
#         except Exception as error:
#             print("PracticeCourseSerializer_updateStatusPublic_error: ", error)
#             return None 
    