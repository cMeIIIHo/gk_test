from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
