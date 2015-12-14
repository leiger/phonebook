from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user_id = models.ForeignKey(User)
    name = models.CharField(verbose_name="name", max_length=100, default='')
    company = models.CharField(verbose_name="company", max_length=100, default='')
    position = models.CharField(verbose_name="position", max_length=100, default='')
    phoneType = models.CharField(verbose_name="phoneType", max_length=100, default='')
    phone = models.CharField(verbose_name="phone", max_length=100, default='')
    emailType = models.CharField(verbose_name='emailType', max_length=100, default='')
    email = models.EmailField(verbose_name='email', max_length=100)
    socialType = models.CharField(verbose_name='socialType', max_length=100, default='')
    social = models.CharField(verbose_name="social", max_length=100, default='')
    remark = models.CharField(verbose_name="remark", max_length=100, default='')
