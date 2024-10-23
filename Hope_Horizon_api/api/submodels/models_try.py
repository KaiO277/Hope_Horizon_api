from django.db import models


class Try(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)  # Đường dẫn lưu trữ ảnh trong thư mục media/uploads/
    

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
    
