from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin
from .models import Category, Slide, SubSlide
from .forms import CategoryForm


class SlideInline(admin.TabularInline):
    model = Slide.categories.through


class CategoryAdmin(MPTTModelAdmin):
    form = CategoryForm
    inlines = [SlideInline, ]
    prepopulated_fields = {'slug': ('name',)}


class SubSlideInline(admin.TabularInline):
    model = SubSlide.slides.through


class SlideResource(resources.ModelResource):

    class Meta:
        model = Slide


class SlideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SlideResource
    inlines = [SubSlideInline, ]
    list_display = ('title', 'date_added')
    exclude = ('date_added', )


class SubSlideResource(resources.ModelResource):

    class Meta:
        model = SubSlide


class SubSlideAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SubSlideResource
    list_display = ('title', 'date_added')
    exclude = ('date_added', )


admin.site.register(SubSlide, SubSlideAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Category, CategoryAdmin)
