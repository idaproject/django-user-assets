from django.db.models import Prefetch, Q

from .models import AssetGroup, Asset


def add_assets(request):
    context = {'user_assets': {}}
    filter_expression = Q(site=None)
    if hasattr(request, 'site'):
        filter_expression |= Q(site=request.site)
    prefetch = Prefetch('asset_set',
                        queryset=Asset.objects.filter(filter_expression, published=True))
    groups = AssetGroup.objects\
        .filter(filter_expression) \
        .prefetch_related(prefetch)
    for group in groups:
        if len(group.asset_set.all()):
            group_content = '\n'.join([asset.content for asset in group.asset_set.all()])
            context['user_assets'][group.key] = group_content
    return context
