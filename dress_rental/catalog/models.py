from django.db import models

class Dress(models.Model):
    title = models.CharField(max_length = 100)
    amount = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'catalog/images/')
    size = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)

    def __str__(self):
        return self.title