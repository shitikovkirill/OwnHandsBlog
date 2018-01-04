from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin
from .models import Category, Slide


class SlideResource(resources.ModelResource):

    class Meta:
        model = Slide


class SlideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SlideResource
    list_display = ('title', 'date_added')


admin.site.register(Slide, SlideAdmin)
admin.site.register(Category, MPTTModelAdmin)
