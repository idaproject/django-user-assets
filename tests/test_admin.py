from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from user_assets.models import Asset, AssetGroup


class TestAssetGroupAdmin(TestCase):
    def setUp(self):
        User.objects.create_superuser('temporary', 'temporary@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

    def test_changelist(self):
        res = self.client.get(reverse('admin:user_assets_assetgroup_changelist'))
        self.assertEqual(res.status_code, 200)

    def test_change(self):
        group = AssetGroup.objects.create(name='test', key='test')
        res = self.client.get(reverse('admin:user_assets_assetgroup_change', args=[group.id]))
        self.assertEqual(res.status_code, 200)


class TestAssetAdmin(TestCase):
    def setUp(self):
        User.objects.create_superuser('temporary', 'temporary@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

    def test_changelist(self):
        res = self.client.get(reverse('admin:user_assets_asset_changelist'))
        self.assertEqual(res.status_code, 200)

    def test_change(self):
        group = AssetGroup.objects.create(name='test', key='test')
        asset = Asset.objects.create(name='test', content='test', group=group)
        res = self.client.get(reverse('admin:user_assets_asset_change', args=[asset.id]))
        self.assertEqual(res.status_code, 200)
