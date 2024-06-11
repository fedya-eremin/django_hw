from rest_framework.serializers import ModelSerializer

from repository.models import Developer, Repository, Ticket


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = "id", "name"


class RepositorySerializer(ModelSerializer):
    developers = DeveloperSerializer(read_only=True, many=True)

    class Meta:
        model = Repository
        fields = "id", "name", "stars", "developers"


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "id", "name", "description", "status", "repository"
