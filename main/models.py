from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from image_cropping import ImageRatioField

from main.validators import image_dimensions


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    salary = models.FloatField()
    cropping = ImageRatioField('cover', '100x100', free_crop=True)
    cover = models.ImageField(upload_to='cover', validators=[image_dimensions], null=True)
    description = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
