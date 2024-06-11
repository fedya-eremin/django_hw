from datetime import datetime, timezone
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


def get_datetime() -> datetime:
    return datetime.now(timezone.utc)


def check_date_created(dt: datetime) -> None:
    if dt > get_datetime():
        raise ValidationError(
            "Date and time is bigger than current!", params={"created": dt}
        )


class CreatedMixin(models.Model):
    created = models.DateTimeField(
        "created",
        default=get_datetime,
        null=True,
        blank=True,
        validators=[check_date_created],
    )

    class Meta:
        abstract = True


class Repository(UUIDMixin):
    name = models.TextField("name", null=False, blank=False)
    description = models.TextField("description", null=False, blank=False)
    stars = models.PositiveIntegerField(
        "stars",
        null=False,
        blank=False,
        default=0,
    )
    developers = models.ManyToManyField(
        "developer", related_name="repository_developer"
    )

    class Meta:
        db_table = '"django_hw"."repository"'
        verbose_name = "repository"
        verbose_name_plural = "repositories"

    def __str__(self):
        return f"{self.name} {self.stars} stars"


class Developer(UUIDMixin, CreatedMixin):
    name = models.TextField("name", null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = '"django_hw"."developer"'
        verbose_name = "developer"
        verbose_name_plural = "developers"

    def __str__(self):
        return self.name


class Ticket(UUIDMixin):
    name = models.TextField("name", null=False, blank=False)
    description = models.TextField("description", null=False, blank=False)

    class Status(models.TextChoices):
        CREATED = "created", "created"
        IN_WORK = "in work", "in work"
        DONE = "done", "done"

    status = models.TextField(
        "status", choices=Status, null=False, blank=False
    )

    repository = models.ForeignKey(
        "repository", null=False, blank=False, on_delete=models.CASCADE
    )

    class Meta:
        db_table = '"django_hw"."ticket"'
        verbose_name = "ticket"
        verbose_name_plural = "tickets"
