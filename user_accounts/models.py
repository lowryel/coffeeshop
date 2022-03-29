from django.db import models

# Create your models here.
class FileModel(models.Model):
    name=models.CharField('file name', max_length=60)
    file=models.FileField()

    def __str__(self):
        return self.name
