from rest_framework import serializers
from users.models.teatcher import Teatcher
from users.models.user import CustomUser


class TeatcherSerializer(serializers.Serializer):
    user = serializers.UUIDField(write_only=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    specialization = serializers.CharField(required=False, allow_blank=True)

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

        if hasattr(user, "teacher_profile"):
            raise serializers.ValidationError({"user": "Usuário já possui perfil de professor"})

        return Teatcher.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.bio = validated_data.get("bio", instance.bio)
        instance.specialization = validated_data.get("specialization", instance.specialization)
        instance.save()
        return instance