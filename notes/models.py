# /notekeeper/notes/models.py

from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ['-updated_at']

class ResearchReference(models.Model):
    note = models.ForeignKey(
        Note, 
        on_delete=models.CASCADE,
        related_name='references'
    )
    url = models.URLField()
    title = models.CharField(max_length=200)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)