from django.contrib import admin
from .models import TouchnetTransaction, InklingTransaction


class TouchnetTransactionAdmin(admin.ModelAdmin):
    readonly_fields = ['user_id', 'first_name', 'last_name', 'title', 'amount', 'success_or_fail', 'details']
    list_display = ('date_created', 'user_id', 'first_name', 'last_name', 'title', 'amount', 'success_or_fail',
                    'details')
    search_fields = ['date_created', 'user_id', 'last_name']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class InklingTransactionAdmin(admin.ModelAdmin):
    readonly_fields = fields = ['date_created', 'user_id', 'type', 'first_name', 'last_name', 'title',
                                'success_or_fail', 'details']
    list_display = ('date_created', 'type', 'user_id', 'first_name', 'last_name', 'title', 'success_or_fail',
                    'details')
    search_fields = ['date_created', 'user_id', 'last_name']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.disable_action('delete_selected')
admin.site.register(TouchnetTransaction, TouchnetTransactionAdmin)
admin.site.register(InklingTransaction, InklingTransactionAdmin)