from django.test import TestCase 
from api.views.teatcher import TeatcherViewSet 
import importlib 
import inspect 
from rest_framework.viewsets import ModelViewSet
from api.serializers.teatcher_serializer import TeatcherSerializer
from api.models.teatcher import Teatcher 

class TestTeatcherViewSet(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_can_import_teatcher_view_set(self) -> None:
    try:
      from api.views.teatcher import TeatcherViewSet
    except ImportError:
      raise ImportError("was not possible to import the user view set")
    
  def test_if_teatcher_view_set_have_correct_superclass(self) -> None:
    module = importlib.import_module("api.views.teatcher")
    class_ = module.TeatcherViewSet 
    self.assertTrue(issubclass(class_, ModelViewSet))
    
  def test_if_teatcher_view_set_have_correct_serializer_class(self) -> None:
    module = importlib.import_module("api.views.teatcher")
    class_ = module.TeatcherViewSet 
    self.assertTrue(class_.serializer_class, TeatcherSerializer)
    
  def test_if_teatcher_view_set_have_correct_authentication_classes(self) -> None:
    module = importlib.import_module("api.views.teatcher")
    class_ = module.TeatcherViewSet 
    self.assertTrue(class_.authentication_classes == [])
    
    
  def test_if_teatcher_view_set_have_correct_queryset(self) -> None:
    module = importlib.import_module("api.views.teatcher")
    class_ = module.TeatcherViewSet
    self.assertTrue(hasattr(class_, "queryset"))
    self.assertEqual(class_.queryset.model.__name__, "Teatcher")
    self.assertEqual(type(class_.queryset), type(Teatcher.objects.all()))
    
    