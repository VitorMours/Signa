from django.test import TestCase, Client  
import importlib 
import inspect 
import json
from rest_framework import status 
from api.models import Student, Class, Teatcher

class TestEnrollmentEntity(TestCase):
  def setUp(self) -> None:
    self.client = Client()
    # self.mock_teatcher = Teatcher.objects.create()
    # self.mock_classroom = Class.objects.create(
    #   class_name = "Sistemas Operacionais",
    #   search_code = "SO221",
    #   teatcher = "",
    #   lesson = "",
    #   subject = ""
    # )
    # self.mock_student = Student.objects.create(
    #   first_name="",
    #   last_name="",
    #   email="",
    #   password=""
    # )
    
    
    # self.mock_data = {
      
      
      
    # }
    
  # def test_if_is_active(self) -> None:
  #   self.assertTrue(True)
  
  # def test_if_resource_exists(self) -> None:
  #   response = self.client.get("/api/enrollment/")
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  # def test_if_resource_accept_correct_methods(self) -> None:
  #   response = self.client.options("/api/enrollment/")
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)
  #   allowed_methods = response["Allow"]
  #   self.assertIn("GET", allowed_methods)
  #   self.assertIn("POST", allowed_methods)
    
  # def test_if_resource_accept_get_method(self) -> None:
  #   response = self.client.get("/api/enrollment/")
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)
  #   response_json = json.loads(response.content)
  #   self.assertIsInstance(response_json, list)
    
  # # def test_if_resource_accept_post_method(self) -> None:
  # #   response = self.client.post("/api/enrollment/")
    
  
  # def test_if_resource_accept_put_method(self) -> None:
  #   pass
  
  # def test_if_resource_accept_patch_method(self) -> None:
  #   pass
  
  # def test_if_resource_accept_delete_method(self) -> None:
  #   pass