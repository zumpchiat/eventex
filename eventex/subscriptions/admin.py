from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.timezone import now

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'create_at','subscribe_today', 'paid')
    date_hierarchy = 'create_at'
    search_fields = ('name', 'email', 'cpf',)
    list_filter = ('paid', 'create_at')

    actions = ['mark_as_paid']

    def subscribe_today(self, obj):
        return obj.create_at == now().date()

    subscribe_today.short_description = 'Inscrito hoje?'
    subscribe_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'
        self.message_user(request, msg.format(count))
    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Subscription, SubscriptionModelAdmin)