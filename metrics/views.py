from rest_framework.response import Response
from rest_framework.views import APIView
from file_upload.models import FileModel
from metrics.serializers import MetricSerializer
from utils.metrics import Metrics

class MetricsAPIView(APIView):
    def get(self, request):
        metric_serializer = MetricSerializer(data=request.data)
        if metric_serializer.is_valid(raise_exception=False) and FileModel.objects.all().exists():
            list_filenames = FileModel.objects.values_list('upload_file', flat=True)
            calc_metric = Metrics(metric_serializer.data.get('query'), list_filenames)
            test_metric = calc_metric()
            return Response(test_metric, status=200)
        else:
            return Response(metric_serializer.errors, status=400)
