from django.db import models

class DummyOpenNotes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    note = models.TextField()
    
    class Meta:
        ordering = ['created']
