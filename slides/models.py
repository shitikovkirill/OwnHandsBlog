from django.db import models
import mptt
from redactor.fields import RedactorField


class Slide(models.Model):
    title = models.CharField(max_length=100)
    content = RedactorField()
    date_added = models.DateTimeField(auto_now=True)
    sequence = models.IntegerField(default=100)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title


class SubSlide(models.Model):
    title = models.CharField(max_length=100)
    content = RedactorField()
    date_added = models.DateTimeField(auto_now=True)
    sequence = models.IntegerField(default=100)
    slides = models.ManyToManyField('Slide')

    def __str__(self):
        return self.title


class Category (models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True)

    def count_of_slides(self):
        return len(self.slide_set.all())

    def __str__(self):
        return self.name


mptt.register(Category)
