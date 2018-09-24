__author__ = 'Vladimir'

import hashlib
from django.shortcuts import render, redirect, Http404
from .models import ShortenedURL
from url_shortener.settings import ROOT_URL, KEY_SIZE


# Create your views here.


def shorten_url(request):
    """
    
    :param request:
    :return:
    """
    if request.method == "POST":
        input_url = request.POST.get("input_url", None)
        h = hashlib.blake2b(digest_size=KEY_SIZE)
        h.update(str(input_url).encode())
        generated_key = h.hexdigest()
        shortened_url, created = ShortenedURL.objects.get_or_create(
            original_url=input_url
        )
        if created:
            shortened_url.generated_key = generated_key
            shortened_url.save()
        else:
            generated_key = shortened_url.generated_key
        return render(
            request,
            "result.html",
            {
                "short_url": "{}/shortener/{}/"
                             "".format(ROOT_URL, generated_key)
            }
        )
    return render(request, "shortener.html")


def redirect_to_original_url(request, short_key):
    """
    
    :param request:
    :param short_key:
    :return:
    """
    db_response = ShortenedURL.objects.filter(generated_key=short_key)
    if db_response.exists():
        return redirect(db_response.first().original_url)
    else:
        raise Http404
