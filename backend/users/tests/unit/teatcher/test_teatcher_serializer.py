from django.test import TestCase
from users.models.user import CustomUser
from users.models.teatcher import Teatcher
from users.serializers.teatcher_serializer import TeatcherSerializer

class TeatcherSerializerTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="test@example.com",
            password="12345678",
            first_name="John",
            last_name="Doe",
        )

    # ✅ CREATE

    def test_create_teacher_success(self):
        data = {
            "user": self.user.id,
            "bio": "Professor de matemática",
            "specialization": "Matemática",
        }

        serializer = TeatcherSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        teacher = serializer.save()

        self.assertEqual(teacher.user, self.user)
        self.assertEqual(teacher.bio, data["bio"])
        self.assertEqual(teacher.specialization, data["specialization"])

    def test_create_teacher_user_not_found(self):
        data = {
            "user": "11111111-1111-1111-1111-111111111111",
            "bio": "Teste",
        }

        serializer = TeatcherSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        with self.assertRaises(Exception):
            serializer.save()

    def test_create_teacher_already_exists(self):
        Teatcher.objects.create(user=self.user)

        data = {
            "user": self.user.id,
            "bio": "Outro perfil",
        }

        serializer = TeatcherSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        with self.assertRaises(Exception):
            serializer.save()

    # ✅ UPDATE

    def test_update_teacher_success(self):
        teacher = Teatcher.objects.create(
            user=self.user,
            bio="Antigo",
            specialization="Física",
        )

        data = {
            "bio": "Novo bio",
            "specialization": "Matemática",
        }

        serializer = TeatcherSerializer(instance=teacher, data=data, partial=True)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        updated = serializer.save()

        self.assertEqual(updated.bio, "Novo bio")
        self.assertEqual(updated.specialization, "Matemática")

    # ✅ REPRESENTATION

    def test_to_representation(self):
        teacher = Teatcher.objects.create(
            user=self.user,
            bio="Bio teste",
            specialization="Química",
        )

        serializer = TeatcherSerializer(instance=teacher)
        data = serializer.data

        self.assertEqual(data["user"]["email"], self.user.email)
        self.assertEqual(data["bio"], "Bio teste")
        self.assertEqual(data["specialization"], "Química")

    # ✅ VALIDATION

    def test_user_required(self):
        serializer = TeatcherSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertIn("user", serializer.errors)