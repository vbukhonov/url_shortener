from django.db.models import Model, URLField, CharField
from url_shortener.settings import KEY_SIZE

# Create your models here.


class ShortenedURL(Model):
    class Meta:
        db_table = "shortened_url"
    original_url = URLField(verbose_name="original", name="original_url",
                            primary_key=True)
    generated_key = CharField(verbose_name="generated", name="generated_key",
                              max_length=KEY_SIZE)
