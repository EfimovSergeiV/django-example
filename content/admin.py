from django.contrib import admin
from content.models import VoteModel, ChoiceModel


class InlineChoiceModel(admin.TabularInline):
    model = ChoiceModel
    extra = 0


class VoteModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'start_date', 'end_date', 'is_active')
    readonly_fields = ('start_date', 'end_date')
    actions = ['activate', 'deactivate']
    inlines = [InlineChoiceModel,]

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description = 'Активировать'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description = 'Деактивировать'


admin.site.register(VoteModel, VoteModelAdmin)