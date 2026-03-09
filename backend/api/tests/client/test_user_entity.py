from rest_framework import serializers
from django.test import TestCase, Client
from django.urls import reverse
import importlib
import inspect
from api.models.user import CustomUser
import json

from rest_framework import status


class TestUserEntity(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.mock_user = CustomUser.objects.create(
            first_name  = "Vitor Moura",
            last_name  = "Rezede",
            email  = "rezendemoura@gmail.com",
            password = "32322916aA!"
        )
        self.mock_user_data = {
            "first_name": "Vitor Moura",
            "last_name": "Rezede",
            "email": "jvrezendemoura@gmail.com",
            "password": "32322916aA!"
        }

    def test_is_active(self) -> None:
        self.assertTrue(True)

    def test_if_user_resource_endpoint_exists(self) -> None:
        """Testar apenas se existe a rota para o recurso"""
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_user_resource_have_all_methods(self) -> None:
        """Testar se a rota possui acesso a todos os metodos do recurso"""
        response = self.client.options("/api/users/")
        allowed_methods = response["Allow"]
        self.assertIn("GET", allowed_methods)
        self.assertIn("POST", allowed_methods)

    def test_if_user_resource_have_reverse_url(self) -> None:
        pass

    def test_if_user_resource_can_create_the_resource(self) -> None:
        """Testar se consegue criar usuario dentro do banco de dados"""
        response = self.client.post("/api/users/", self.mock_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_user_resource_can_search_created_user(self) -> None:
        response = self.client.post("/api/users/", self.mock_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        search_response = self.client.get("/api/users/")
        data = json.loads(search_response.content)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_if_user_resource_can_delete_the_resource(self) -> None:
        pass

    def test_if_user_resource_can_update_the_resource(self) -> None:
        pass

    def test_if_user_resource_can_get_the_resource(self) -> None:
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_if_user_resource_can_get_the_resource_by_the_id(self) -> None:
        pass

    def test_if_user_resource_can_partial_update_the_resource(self) -> None:
        pass


class TestUserRaiseErrorEntity(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.exist_user = CustomUser.objects.create(
            first_name = "I",
            last_name="Exist",
            email="i.exist@gmail.com",
            password="123123123asd"

        )
    def test_if_raise_error_create_user_with_credentials_in_use(self) -> None:
        response = self.client.post(
            "/api/users/",
            data=json.dumps({
                "first_name": "Vitor Moura",
                "last_name": "Rezede",
                "email": "i.exist@gmail.com",
                "password": "32322916aA!"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.content)
        self.assertIn("Este email já está em uso", *data["email"])

    def test_if_raise_error_if_try_to_delete_user_resource_tht_does_not_exists(self) -> None:
        pass

