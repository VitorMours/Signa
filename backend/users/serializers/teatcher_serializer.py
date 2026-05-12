from rest_framework import serializers
from users.models.teatcher import Teatcher
from users.models.user import CustomUser
from django.db import IntegrityError


class TeatcherSerializer(serializers.Serializer):
    user = serializers.UUIDField(write_only=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    specialization = serializers.CharField(required=False, allow_blank=True, max_length=100)

    # saída estruturada
    def to_representation(self, instance):
        return {
            "user": {
                "id": str(instance.user.id),
                "first_name": instance.user.first_name,
                "last_name": instance.user.last_name,
                "email": instance.user.email,
            },
            "bio": instance.bio,
            "specialization": instance.specialization,
        }

    def create(self, validated_data):
        user_id = validated_data.pop("user")

        user = CustomUser.objects.filter(id=user_id).first()
        if not user:
            raise serializers.ValidationError({"user": "Usuário não encontrado"})

        try:
            return Teatcher.objects.create(user=user, **validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"user": "Usuário já possui perfil de professor"})

    def update(self, instance, validated_data):
        instance.bio = validated_data.get("bio", instance.bio)
        instance.specialization = validated_data.get("specialization", instance.specialization)
        instance.save()
        return instance