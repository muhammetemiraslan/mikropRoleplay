from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="characters/")
    is_home = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name="characters", blank=True)

    def __str__(self):
        return self.name


class CharacterDetail(models.Model):
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, related_name="detail"
    )
    title = models.CharField(max_length=150)
    years = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    # image is already on Character, but you can keep a separate one if needed
    story = models.TextField(help_text="Paragrafları iki yeni satırla ayır (\\n\\n)")

    def get_story_paragraphs(self):
        return self.story.split("\n\n")

    def __str__(self):
        return f"{self.character.name} Detayı"