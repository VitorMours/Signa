from django.test import TestCase 
import importlib 
import inspect 
from rest_framework.serializers import Serializer 


class TestLoginSerializer(TestCase):
  def setUp(self) -> None:
    pass 
  
  def test_if_is_running(self) -> None:
    self.assertTrue(True)