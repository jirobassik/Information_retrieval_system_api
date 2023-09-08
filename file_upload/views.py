import mimetypes
import os

from django.http import HttpResponse
from rest_framework import viewsets, views
from .models import FileModel
from .serializers import UploadedFileSerializer


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = UploadedFileSerializer


class DownloadFileViewSet(views.APIView):
    def get(self, request, id):
        file_object = FileModel.objects.get(pk=id)
        filename = file_object.upload_file.name
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_location = BASE_DIR + f'/media/{filename}'
        with open(file_location, 'r') as f:
            file_data = f.read()
        mime_type, _ = mimetypes.guess_type(file_location)
        response = HttpResponse(file_data, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
