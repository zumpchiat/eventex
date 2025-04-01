from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.timezone import now

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'create_at','subscribe_today')
    date_hierarchy = 'create_at'
    search_fields = ('name', 'email', 'cpf',)
    list_filter = ('create_at',)

    def subscribe_today(self, obj):
        return obj.create_at == now().date()

    subscribe_today.short_description = 'Inscrito hoje?'
    subscribe_today.boolean = True
admin.site.register(Subscription, SubscriptionModelAdmin)