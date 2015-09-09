from django.contrib import admin
from .models import TouchnetTransaction, InklingTransaction


class TouchnetTransactionAdmin(admin.ModelAdmin):
    fields = ['user_id', 'title', 'ammount', 'success_or_fail', 'details']

class InklingTransactionAdmin(admin.ModelAdmin):
    fields = ['user_id', 'title', 'success_or_fail', 'details']

admin.site.register(TouchnetTransaction, TouchnetTransactionAdmin)
admin.site.register(InklingTransaction, InklingTransactionAdmin)


