import json

from django.test import TestCase, Client
import importlib 
import inspect 
from rest_framework import status

class TestCourseEntity(TestCase):
  def setUp(self) -> None:
    self.client = Client() 
  
  def test_if_test_is_active(self) -> None:
    self.assertTrue(True)
  
  def test_if_course_resource_exists(self) -> None:
    response = self.client.get('/api/courses/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_if_course_resource_accept_all_methods(self) -> None:
    response = self.client.options("/api/courses/")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    allowed_methods = response["Allow"]
    self.assertIn("GET", allowed_methods)
    self.assertIn("POST", allowed_methods)

  def test_if_course_resource_accept_get_method(self) -> None:
    response = self.client.get("/api/courses/")
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    response_json = json.loads(response.content)
    self.assertIsInstance(response_json, list)
  