from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Lesson(MPTTModel):
    title = models.TextField(max_length=500, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return (str(self.parent) + " » " if self.parent is not None else "") + self.title