from django.db import models
import uuid


class CommonId(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class CommonFields(models.Model):

    title = models.CharField(max_length=50, verbose_name='заголовок')
    description = models.TextField(default='', blank=True, verbose_name='описание')

    class Meta:
        abstract = True
