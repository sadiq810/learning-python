from django.contrib import admin
from . import models

# to reorder fields in admin detail view
# class name should be like ModelName+Admin
# then pass this class to model registration as in line 11
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
    search_fields = ['title', 'length'] #to add searching
    list_filter = ['release_year', 'length'] # to add filter to your model.
    list_display = ['title', 'release_year', 'length'] # to show fields in the admin
    list_editable = ['length'] #to make your model fields editable in admin

# Register your models here.
admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
