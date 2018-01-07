from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Slide


class CategoryForm(forms.ModelForm):
    slides = forms.ModelMultipleChoiceField(
        Slide.objects.all(),
        # Add this line to use the double list widget
        widget=FilteredSelectMultiple('Slides', False),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            # if this is not a new object, we load related slides
            self.initial['slides'] = self.instance.slides.values_list('pk', flat=True)

    def save(self, *args, **kwargs):
        instance = super(CategoryForm, self).save(*args, **kwargs)
        if instance.pk:
            for slide in instance.slides.all():
                if slide not in self.cleaned_data['slides']:
                    # we remove slides which have been unselected
                    instance.slides.remove(slide)
            for slide in self.cleaned_data['slides']:
                if slide not in instance.slides.all():
                    # we add newly selected slides
                    instance.slides.add(slide)
        return instance
