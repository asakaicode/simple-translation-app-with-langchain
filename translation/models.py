from django.db import models

from translation.fields import ULIDField


class Translation(models.Model):
    id = ULIDField(primary_key=True)
    src_lang = models.CharField(max_length=200)
    dest_lang = models.CharField(max_length=200)
    src_text = models.TextField()
    dest_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.src_text[:50]} -> {self.dest_text[:50]}"
