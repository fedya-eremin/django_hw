from django.views.generic import TemplateView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.viewsets import ModelViewSet

from repository.models import Developer, Repository, Ticket
from repository.serializers import (
    DeveloperSerializer,
    RepositorySerializer,
    TicketSerializer,
)


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_superuser)


def create_viewset(model, serializer):
    class CustomViewSet(ModelViewSet):
        queryset = model.objects.all()
        serializer_class = serializer
        permission_classes = [MyPermission]
        authentication_classes = [TokenAuthentication]

    return CustomViewSet


RepositoryViewSet = create_viewset(Repository, RepositorySerializer)
DeveloperViewSet = create_viewset(Developer, DeveloperSerializer)
TicketViewSet = create_viewset(Ticket, TicketSerializer)


class HomePage(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context["repos"] = Repository.objects.all()
        context["serializer"] = RepositorySerializer
        if self.request.user.is_authenticated:
            context["token"] = Token.objects.get(user=self.request.user)
        return context


class DevsPage(TemplateView):
    template_name = "devs.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DevsPage, self).get_context_data(**kwargs)
        context["devs"] = Developer.objects.all()
        return context


class ProfilePage(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context["repos"] = Repository.objects.filter(
            developers=self.request.user.developer
        )
        if self.request.user.is_authenticated:
            context["token"] = Token.objects.get(user=self.request.user)
        return context


class TicketsPage(TemplateView):
    template_name = "tickets.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TicketsPage, self).get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()
        return context
