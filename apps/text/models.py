from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='заголовка'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Статус '
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'дела'