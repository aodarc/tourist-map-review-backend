from django.db import models

# Create your models here.


class ReviewObject(models.Model):
    lat = models.FloatField(verbose_name='lat', db_index=True, blank=False, null=False, default=49.836085)
    lon = models.FloatField(verbose_name='lon', db_index=True, blank=False, null=False, default=24.005691)
    title = models.CharField(max_length=255, verbose_name=u'Заголовок', db_index=True, unique=True)
    description = models.TextField(max_length=300,
                                   verbose_name=u'Короткий опис',
                                   default='Some Description',
                                   blank=False)
    text = models.TextField(max_length=3000, verbose_name=u'Текст статті')
    title_image = models.ImageField(upload_to='./reviews/images',
                                    verbose_name=u'Головне зоображення',
                                    blank=True,
                                    default='./reviews/images/maps.png')

    def __str__(self):
        return self.title

