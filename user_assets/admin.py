from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin, SortableAdminBase
from django.contrib.admin import register, ModelAdmin, TabularInline

from .models import Asset, AssetGroup


class AssetInlineAdmin(SortableInlineAdminMixin, TabularInline):
    model = Asset
    extra = False


@register(AssetGroup)
class AssetGroupAdmin(SortableAdminBase, ModelAdmin):
    inlines = (AssetInlineAdmin,)
    list_display = ('name', 'key', 'site')
    search_fields = ('name',)
    list_filter = ('key', 'site')


@register(Asset)
class AssetAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ('name', 'group', 'site', 'published')
    search_fields = ('name',)
    list_filter = ('group', 'site', 'published')
