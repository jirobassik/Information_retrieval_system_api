from django.db import models

class FileModel(models.Model):
    upload_file = models.FileField("File", unique=True, )

    def __str__(self):
        return self.upload_file.name
