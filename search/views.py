from rest_framework.response import Response
from rest_framework.views import APIView
from text_processing.search_processing import SearchProcessingLogical, SearchProcessingRank
from search.serializers import QuerySerializer
from file_upload.models import FileModel


class SearchAPIView(APIView):
    def get(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid() and FileModel.objects.all().exists():
            file_list = FileModel.objects.values_list('upload_file', flat=True)
            search_proc = SearchProcessingRank(serializer.data.get('query'), *file_list)
            return Response(search_proc(), status=200)
        else:
            return Response(serializer.errors, status=400)
