from rest_framework.response import Response
from rest_framework.views import APIView
from text_processing.search_processing import SearchProcessing
from search.serializers import QuerySerializer

class SearchAPIView(APIView):
    def get(self, request):
        serializer = QuerySerializer(data=request.data)
        if serializer.is_valid():
            search_proc = SearchProcessing(serializer.data.get('query'), 'text1.txt', 'text2.txt', 'text3.txt')
            return Response(search_proc(), status=200)
        else:
            return Response(serializer.errors, status=400)
