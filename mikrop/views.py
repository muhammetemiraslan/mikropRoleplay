from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.conf import settings
from .models import Character


def index(request):
    return render(request, "mikrop/index.html")


def hikayeler(request):
    characters = Character.objects.filter(is_home=True)
    return render(request, "mikrop/hikayeler.html", {"characters": characters})


def karakter_detay(request, karakter_id):
    # Karakteri ve onun detayını al
    karakter = get_object_or_404(Character, id=karakter_id)
    detay = getattr(karakter, "detail", None)  # Karakterin detaylarını al

    # Karakterin bağlı olduğu kategorileri al
    kategoriler = karakter.categories.all()

    # Bu kategorilerdeki diğer karakterleri al
    # exclude(id=karakter.id) ile tıklanan karakteri hariç tutuyoruz
    karakterler = Character.objects.filter(categories__in=kategoriler).exclude(
        id=karakter.id
    )

    # Context'e karakter ve diğer karakterleri ekle
    context = {
        "karakter": {
            "title": detay.title if detay else "",
            "full_name": detay.full_name if detay else "",
            "name": karakter.name,
            "years": detay.years if detay else "",
            "story": detay.get_story_paragraphs() if detay else [],
            "image": karakter.image.url,
        },
        "karakterler": karakterler,  # Kategorisindeki diğer karakterler
    }

    return render(request, "mikrop/karakter_detay.html", context)


def forum(request):
    return render(request, "mikrop/forum.html")

def sss(request):
    return render(request, "mikrop/sss.html")


def technicalSupport(request):
    if request.method == "POST":
        user_email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Gönderen Email: {user_email}\n\nSorun Mesajı:\n{message}"

        send_mail(
            subject="Yeni Sorun Bildirimi",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["mikroprust@gmail.com"],
            fail_silently=False,
        )

        return render(request, "mikrop/technicalSupport.html", {"success": True})

    return render(request, "mikrop/technicalSupport.html")
