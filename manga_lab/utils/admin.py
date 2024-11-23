from django.contrib import admin

from manga_lab.utils.models import BannerImage


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("manga", "source_type", "is_active", "created_at")
    search_fields = (
        "manga",
        "source_type",
    )
    list_filter = ["manga", "source_type", "is_active", "created_at"]
