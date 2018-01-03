from django.db import models
import mptt


class Slide(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField()
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


mptt.register(Category)
