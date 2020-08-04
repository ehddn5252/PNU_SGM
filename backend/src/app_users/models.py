from django.db import models

# Create your models here.

class Users(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    #registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        """A string representation of the model."""
        return self.username

    class Meta:
        db_table = '송골매 users'
        verbose_name = '유저'
        verbose_name_plural = "유저"