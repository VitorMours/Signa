from rest_framework.viewsets import ModelViewSet
from api.models.teatcher import Teatcher 
from api.serializers.teatcher_serializer import TeatcherSerializer 


class TeatcherViewSet(ModelViewSet):
  """
  Viewset for the teatcher data in the database, 
  some fields area write_only or read_only.
    read_only: created_at, updated_at
    write_only: password
  """
  
  serializer_class = TeatcherSerializer
  authentication_classes = []
  queryset = Teatcher.objects.all()
  