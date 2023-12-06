from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Applicant
from .serializers import ApplicantSerializer


class ApplicantViewSet(ReadOnlyModelViewSet):
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()
