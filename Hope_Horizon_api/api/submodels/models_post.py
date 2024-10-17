from django.db import models
from ckeditor.fields import RichTextField


class PostCate(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title
    
class PostIndex(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text_short = models.CharField(max_length=250, null=True, blank=True)
    text_long = RichTextField(blank=True, null=True) 
    image_title = models.CharField(max_length=250, null=True, blank=True)
    post_cate = models.ForeignKey(
        PostCate, related_name='post_cate_w_post_index', on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title
