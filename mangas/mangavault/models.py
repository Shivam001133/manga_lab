from django.db import models
from django.utils.translation import gettext_lazy as _

from mangas.harvest_routes.models import Harvester
from mangas.harvest_routes.models import HarvestType


class MangaCategory(models.TextChoices):
    MANGA = "Manga", _("Manga")
    MANHWA = "Manhwa", _("Manhwa")
    MANHUA = "Manhua", _("Manhua")
    COMICS = "Comics", _("Comics")
    NONE = "none", _("None")


class MangaStatus(models.TextChoices):
    ONGOING = "ongoing", _("Ongoing")
    COMPLETED = "completed", _("Completed")
    PAUSED = "paused", _("Paused")
    CANCELLED = "cancelled", _("Cancelled")
    NONE = "none", _("None")


class MangaGenre(models.Model):
    title = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=True)
    related_to = models.CharField(
        choices=HarvestType.choices,
        default=HarvestType.NONE,
        max_length=10,
    )
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class MangaVault(models.Model):
    title = models.CharField(max_length=200)
    manga_title = models.TextField(blank=True)
    website = models.ForeignKey(
        Harvester,
        on_delete=models.RESTRICT,
        related_name="manga_source",
    )
    genre = models.ManyToManyField(MangaGenre, related_name="manga_genre")
    cover_img = models.URLField(blank=True)
    description = models.TextField()
    vault_url = models.URLField(unique=True, blank=True)
    category = models.CharField(
        choices=MangaCategory.choices,
        default=MangaCategory.MANGA,
        max_length=10,
    )
    status = models.CharField(
        choices=MangaStatus.choices,
        default=MangaStatus.NONE,
        max_length=10,
    )
    is_new = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class MangaChapter(models.Model):
    chapter_title = models.CharField(max_length=100)
    manga = models.ForeignKey(
        MangaVault,
        on_delete=models.CASCADE,
        related_name="manga_chapter",
    )
    chapter_url = models.URLField(unique=True)
    chapter_number = models.PositiveSmallIntegerField()
    chapter_list = models.JSONField()
    is_new = models.BooleanField(default=False)
    is_latest = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.chapter_title
