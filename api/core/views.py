from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import UserModel, ProgressDetailModel
from core.serializers import UserSerializer, ProgressDetailSerializer


class HealthCheckViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = UserModel.objects.all()
        email = self.request.query_params.get('email')
        fase = self.request.query_params.get('fase')

        filtros={}

        if email:
            filtros['email__icontains'] = email

        if fase:
            filtros['progress__stage'] = fase

        if filtros:
            return queryset.filter(**filtros)

        return queryset

class ProgressDetailViewSet(viewsets.ModelViewSet):
    queryset = ProgressDetailModel.objects.all()
    serializer_class = ProgressDetailSerializer