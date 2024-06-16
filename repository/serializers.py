from django.contrib.auth.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework.serializers import ModelSerializer

from repository.models import Developer, Repository, Ticket


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = "id", "name"

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["name"])
        user.save()
        validated_data["user_id"] = user.id
        return super().create(validated_data)


class RepositorySerializer(WritableNestedModelSerializer):
    developers = DeveloperSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Repository
        fields = "id", "name", "stars", "developers"

    def create(self, validated_data):
        """Don't try this at home"""
        developer = self.context["request"].data.get("developer")
        if developer:
            validated_data["developers"] = [
                Developer.objects.get(pk=developer)
            ]
        return super().create(validated_data)


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "id", "name", "description", "status", "repository"
