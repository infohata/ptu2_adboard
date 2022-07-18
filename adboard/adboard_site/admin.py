from django.contrib import admin
from . import models


class AdPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'owner', 'status', 'created_at', 'buyer', 'promoted', )
    list_filter = ('category', 'promoted', 'created_at', 'updated_at', )
    search_fields = ('title', 'owner__username', 'owner__last_name', )
    list_editable = ('promoted', 'status', )


admin.site.register(models.Category)
admin.site.register(models.AdPost, AdPostAdmin)
