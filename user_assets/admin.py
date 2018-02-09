from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib.admin import register, ModelAdmin, TabularInline

from .models import Asset, AssetGroup


class AssetInlineAdmin(SortableInlineAdminMixin, TabularInline):
    model = Asset
    extra = False


@register(AssetGroup)
class AssetGroupAdmin(ModelAdmin):
    inlines = (AssetInlineAdmin,)
    list_display = ('name', 'key', 'site')
    search_fields = ('name',)
    list_filter = ('key', 'site')


@register(Asset)
class AssetAdmin(SortableAdminMixin, ModelAdmin):
    pass
