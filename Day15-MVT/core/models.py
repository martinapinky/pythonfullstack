from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
class Painting(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='paintings', default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title + ' by ' + self.artist