from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path, reverse_lazy
from rest_framework.routers import DefaultRouter

from repository import views

router = DefaultRouter()
router.register(r"repository", views.RepositoryViewSet)
router.register(r"developer", views.DeveloperViewSet)
router.register(r"ticket", views.TicketViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("", views.HomePage.as_view(), name="home"),
    path("devs/", views.DevsPage.as_view()),
    path("login/", LoginView.as_view(template_name="login.html")),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("home")),
        name="logout",
    ),
    path("profile/", views.ProfilePage.as_view()),
]
