from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    salary = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
