from django.db.models import Prefetch

from .models import AssetGroup, Asset


def add_assets(request):
    context = {}
    groups = AssetGroup.objects.prefetch_related(Prefetch(
        'asset_set',
        queryset=Asset.objects.filter(published=True)
    )).all()
    for group in groups:
        if len(group.asset_set.all()):
            context[group.key] = ''.join([asset.content for asset in group.asset_set.all()])
    return context
