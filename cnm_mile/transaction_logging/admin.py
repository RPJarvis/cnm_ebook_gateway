from django.contrib import admin
from .models import TouchnetTransaction, InklingTransaction


class TouchnetTransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['user_id', 'title', 'amount', 'success_or_fail', 'details']

    #fields = ['user_id', 'title', 'amount', 'success_or_fail', 'details']
    list_display = ('date_created', 'user_id', 'title', 'amount', 'success_or_fail', 'details')
    search_fields = ['date_created', 'user_id']


class InklingTransactionAdmin(admin.ModelAdmin):
    readonly_fields = fields = ['user_id', 'title', 'success_or_fail', 'details']
   # fields = ['user_id', 'title', 'success_or_fail', 'details']
    list_display = ('date_created', 'user_id', 'title', 'success_or_fail', 'details')
    search_fields = ['date_created', 'user_id']

admin.site.register(TouchnetTransaction, TouchnetTransactionAdmin)
admin.site.register(InklingTransaction, InklingTransactionAdmin)