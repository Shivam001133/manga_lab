from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HarvesterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mangas.harvest_routes"
    verbose_name = _("Mangavault")
