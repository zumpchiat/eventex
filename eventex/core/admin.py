from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speaker, Contact

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_link', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)
    website_link.short_description = 'site'

    def photo_link(self, obj):
        return format_html('<img width="32px" src={} />', obj.photo)

    photo_link.short_description = 'foto'


admin.site.register(Speaker, SpeakerModelAdmin)
