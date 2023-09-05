import os
import pathlib

from django.db import models


class FileModel(models.Model):
    upload_file = models.FileField("File", unique=True, )

    def delete(self, using=None, keep_parents=False):
        pathlib.Path('media', self.upload_file.name).unlink(missing_ok=False)
        super().delete()

    def __str__(self):
        return self.upload_file.name
