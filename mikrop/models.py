from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.html import format_html


class Category(models.Model):
    """Karakter kategorileri için model"""

    name = models.CharField("Kategori Adı", max_length=100)
    description = models.TextField("Açıklama", blank=True, null=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name


class Character(models.Model):
    """Ana karakter modeli"""

    name = models.CharField("Karakter Adı", max_length=100)
    image = CloudinaryField(
        "Profil Resmi",
        folder="mikro-roleplay/characters",
        # Transformation kaldırıldı (orijinal boyutta yüklenecek)
        blank=True,
        null=True,
    )
    is_home = models.BooleanField("Ana Sayfada Gösterilsin Mi?", default=True)
    categories = models.ManyToManyField(
        Category, verbose_name="Kategoriler", related_name="characters", blank=True
    )

    class Meta:
        verbose_name = "Karakter"
        verbose_name_plural = "Karakterler"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def image_preview(self):
        """Admin panelinde resim önizleme"""
        if self.image:
            return format_html(
                '<img src="{}" style="max-height:150px;width:auto;border-radius:8px;"/>',
                self.image.url,
            )
        return "Resim Yok"


class CharacterDetail(models.Model):
    """Karakter detayları için genişletme modeli"""

    character = models.OneToOneField(
        Character,
        verbose_name="Karakter",
        on_delete=models.CASCADE,
        related_name="detail",
    )
    title = models.CharField("Ünvan", max_length=150)
    years = models.CharField("Yıllar", max_length=50)
    full_name = models.CharField("Tam Adı", max_length=150)
    story = models.TextField("Hikaye", help_text="Paragraflar için çift enter kullanın")

    class Meta:
        verbose_name = "Karakter Detayı"
        verbose_name_plural = "Karakter Detayları"

    def get_story_paragraphs(self):
        """Hikayeyi paragraflara ayırır"""
        return self.story.split("\n\n")

    def __str__(self):
        return f"{self.character.name} - Detaylar"
