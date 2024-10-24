from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class PodcastCate(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

class PodcastAuthor(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name 
    
class PodcastIndex1(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image_title = models.ImageField(upload_to='uploads/', null=True, blank=True)
    podcast_cate = models.ForeignKey(
        PodcastCate, related_name='podcast_cate_w_podcast_index1', on_delete=models.SET_NULL, blank=True, null=True
    )
    podcast_author = models.ForeignKey(
        PodcastAuthor, related_name='podcast_author_w_podcast_index1', on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title

class PodcastIndex2(models.Model):
    name_chapter = models.CharField(max_length=50, null=True, blank=True)
    content = models.FileField(upload_to='audio_uploads/', null=True, blank=True)
    pod_index1 = models.ForeignKey(
        PodcastIndex1, related_name='podcast_index1_w_podcast_index2', on_delete=models.SET_NULL, blank=True, null=True 
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name_chapter
    
class PodcastViews(models.Model):
    pod_index1 = models.ForeignKey(PodcastIndex1, related_name='podcast_index1_w_podcast_views', on_delete=models.SET_NULL, blank=True, null=True)
    use = models.ForeignKey(User, related_name='user_w_podcast_views', on_delete=models.SET_NULL, blank=True, null=True)
    number_views = models.IntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.number_views