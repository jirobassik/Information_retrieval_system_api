import pathlib
from django.db import models


class FileModel(models.Model):
    upload_file = models.FileField("File", unique=True, )
    file_content = models.CharField(null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.upload_file:
            self.file_content = self.upload_file.read().decode('utf-8')
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        pathlib.Path('media', self.upload_file.name).unlink(missing_ok=False)
        super().delete()

    def __str__(self):
        return self.upload_file.name
