from rest_framework.response import Response
from rest_framework.views import APIView
from file_upload.models import FileModel
from pathlib import Path
from utils.text_classification import text_classification

class ClassificationAPIView(APIView):
    def get(self, request, id):
        file_object = FileModel.objects.get(pk=id)
        filename = file_object.upload_file.name
        file_text = Path('media', filename).read_text()
        return Response({'text_class': text_classification(file_text), 'filename': filename})
