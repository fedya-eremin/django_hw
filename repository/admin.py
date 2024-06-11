from django.contrib import admin

from repository.models import Developer, Repository, Ticket


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Repository

    list_display = (
        "name",
        "description",
        "stars",
    )
    list_filter = (
        "name",
        "stars",
    )


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    class Meta:
        model = Developer

    list_display = ("name", "created")
    readonly_fields = ("created",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    class Meta:
        model = Ticket

    list_display = (
        "name",
        "status",
    )
