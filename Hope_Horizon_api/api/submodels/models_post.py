from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class PostCate(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        if self.title:
            return self.title 
        return str(self.id) + "_" + "PostCate"

class PostAuthor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    # post_index = models.ForeignKey(
    #     PostIndex, related_name='post_index_w_post_author', on_delete=models.SET_NULL, blank= True, null=True    
    # )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name 
    
class PostIndex(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text_short = models.CharField(max_length=250, null=True, blank=True)
    text_long = RichTextField(blank=True, null=True) 
    image_title = models.ImageField(upload_to='uploads/', null=True, blank=True)
    post_cate = models.ForeignKey(
        PostCate, related_name='post_cate_w_post_index', on_delete=models.SET_NULL, blank=True, null=True
    )
    post_author = models.ForeignKey(
        PostAuthor, related_name='post_author_w_post_index', on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

    
class PostViews(models.Model):
    post_index = models.ForeignKey(PostIndex, related_name='post_index_w_post_views', on_delete=models.SET_NULL, blank=True, null=True)
    use = models.ForeignKey(User, related_name='user_w_post_views', on_delete=models.SET_NULL, blank=True, null=True)
    number_views = models.IntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.number_views