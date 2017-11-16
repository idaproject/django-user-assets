from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib.admin import site, ModelAdmin, TabularInline

from .models import Asset, AssetGroup


class AssetInlineAdmin(SortableInlineAdminMixin, TabularInline):
    model = Asset
    extra = False


class AssetGroupAdmin(ModelAdmin):
    inlines = (AssetInlineAdmin,)


class AssetAdmin(SortableAdminMixin, ModelAdmin):
    pass


site.register(AssetGroup, AssetGroupAdmin)
site.register(Asset, AssetAdmin)
