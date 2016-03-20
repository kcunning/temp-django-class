from __future__ import unicode_literals

from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    servings = models.PositiveIntegerField(blank=True)
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.title