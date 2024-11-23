from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from mangavault.models import MangaChapter

# models
from mangavault.models import MangaVault

from manga_lab.utils.models import BannerImage


def home_view(request):
    banner = BannerImage.objects.filter(
        Q(image__isnull=False) & ~Q(image="") | Q(image_url__exact=""),
    )
    banner = BannerImage.objects.all()
    data = MangaVault.objects.filter(is_active=True)
    context = {"banner": banner, "data": data}
    return render(request, "pages/home.html", context)


def manga_detail(request, pk):
    manga = get_object_or_404(MangaVault, pk=pk)
    chapters = MangaChapter.objects.filter(manga=manga)
    return render(
        request, "pages/manga_detail.html", {"manga": manga, "chapters": chapters}
    )
