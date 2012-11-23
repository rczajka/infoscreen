from django.db import models


class InfoBox(models.Model):
    slug = models.SlugField(unique=True, editable=False)
    body = models.TextField(blank=True)
    seconds = models.IntegerField(default=30)
    stamp = models.DateTimeField(auto_now=True)

    @classmethod
    def get(cls, slug):
        try:
            return cls.objects.get(slug=slug)
        except cls.DoesNotExist:
            return cls(slug=slug, body="")
