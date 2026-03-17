import json
from api.models import Teatcher
from django.test import TestCase, Client
import importlib 
import inspect 
from rest_framework import status

class TestCourseEntity(TestCase):
  def setUp(self) -> None:
    self.client = Client() 
  
    self.teatcher_entity = Teatcher.objects.create(
        first_name = "Vitor Flavio", 
        last_name = "Dantas",
        email = "vitor.dantas@gmail.com",
        password = "32322916aA!"
    )


    self.mock_course_data = {
        "name":"Curso de exemplo",
        "description":"Criando um curso de exemplo de teste",
        "teatcher": self.teatcher_entity.id,
        "total_semesters":12,
        "actual_semester":6,
        "start_date":"2026-03-17",
        "end_date":"2026-03-17",
        "is_active":True,
    }

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
 
  def test_if_course_resource_accept_post_method(self) -> None:
    response = self.client.post("/api/courses/", self.mock_course_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_if_can_delete_the_course_that_exists(self) -> None:
      response = self.client.post("/api/courses/", self.mock_course_data)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
      data = json.loads(response.content)
      self.assertIsInstance(data, dict)
      new_response = self.client.delete(f"/api/courses/{data["id"]}/")
      self.assertEqual(new_response.status_code, status.HTTP_204_NO_CONTENT)


  def test_if_course_resource_accept_to_get_user_by_id(self) -> None:
      response = self.client.post("/api/courses/", self.mock_course_data)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      data = json.loads(response.content)
      fetch_user_by_id = self.client.get(f"/api/courses/{data['id']}/")
      self.assertEqual(fetch_user_by_id.status_code, status.HTTP_200_OK)
      data = json.loads(fetch_user_by_id.content)
      self.assertEqual(data["teatcher"], self.teatcher_entity.first_name)
      self.assertEqual(data["name"], self.mock_course_data["name"])

  def test_if_can_update_partially_course_that_exists(self) -> None:
    response = self.client.post("/api/courses/", self.mock_course_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # TODO: Test if can update  

class TestCourseEntityError(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_if_raise_error_creating_user_with_email_already_in_use(self) -> None:
        pass 

    def test_if_raise_error_if_trying_to_delete_user_that_does_not_exist(self) -> None:
        pass 

    def test_raise_error_if_trying_to_get_by_id_user_that_does_not_exists(self) -> None:
        pass

