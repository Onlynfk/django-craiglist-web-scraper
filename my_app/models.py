from django.db import models

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.search


    class Meta:
        verbose_name_plural = 'Searches'