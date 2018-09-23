from django.db.models import Model, URLField, CharField

# Create your models here.


class ShortenedURL(Model):
    class Meta:
        db_table = "shortened_url"
    original_url = URLField(verbose_name="original", name="original_url")
    generated_key = CharField(verbose_name="generated", name="generated_key",
                              primary_key=True, max_length=8)
