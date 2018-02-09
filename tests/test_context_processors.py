#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.test import TestCase, RequestFactory

from user_assets.models import AssetGroup, Asset
from user_assets.context_processors import add_assets


class TestAddAssets(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_without_assets(self):
        request = self.factory.get('/')
        context = add_assets(request)
        self.assertEqual(context, {'user_assets': {}})

    def test_with_unpublished_asset(self):
        group = AssetGroup.objects.create(name='Test', key='test')
        Asset.objects.create(name='Test', content='test content', group=group, published=False)
        request = self.factory.get('/')
        context = add_assets(request)
        self.assertEqual(context, {'user_assets': {}})

    def test_with_one_asset(self):
        group = AssetGroup.objects.create(name='Test', key='test')
        asset = Asset.objects.create(name='Test', content='test content', group=group,
                                     published=True)
        request = self.factory.get('/')
        context = add_assets(request)
        self.assertEqual(context, {'user_assets': {group.key: asset.content}})

    def test_with_site_group_asset(self):
        site_1 = Site.objects.get(id=1)
        site_2 = Site.objects.create(name='example2.com', domain='example2.com')
        group_1 = AssetGroup.objects.create(name='Test', key='test', site=site_1)
        Asset.objects.create(name='Test', content='test content', group=group_1, published=True)
        group_2 = AssetGroup.objects.create(name='Test', key='test', site=site_2)
        asset_2 = Asset.objects.create(name='Test', content='test content', group=group_2,
                                       published=True)
        request = self.factory.get('/')
        request.site = site_2
        context = add_assets(request)
        self.assertEqual(context, {'user_assets': {group_2.key: asset_2.content}})

    def test_with_site_asset(self):
        site_1 = Site.objects.get(id=1)
        site_2 = Site.objects.create(name='example2.com', domain='example2.com')
        group_1 = AssetGroup.objects.create(name='Test', key='test', site=site_1)
        Asset.objects.create(name='Test', content='test content', group=group_1, published=True)
        group_2 = AssetGroup.objects.create(name='Test', key='test')
        asset_2 = Asset.objects.create(name='Test', content='test content', group=group_2,
                                       published=True, site=site_2)
        request = self.factory.get('/')
        request.site = site_2
        context = add_assets(request)
        self.assertEqual(context, {'user_assets': {group_2.key: asset_2.content}})

    def test_asset_order(self):
        group = AssetGroup.objects.create(name='Test', key='test')
        asset_1 = Asset.objects.create(name='Test', content='test content 2', group=group,
                                       published=True, order=2)
        asset_2 = Asset.objects.create(name='Test', content='test content 1', group=group,
                                       published=True, order=1)
        request = self.factory.get('/')
        context = add_assets(request)
        self.assertEqual(context, {'user_assets': {
            group.key: asset_2.content + '\n' + asset_1.content
        }})

    def test_num_queries(self):
        group_1 = AssetGroup.objects.create(name='Test', key='test')
        group_2 = AssetGroup.objects.create(name='Test', key='test')
        Asset.objects.create(name='Test', content='test content', group=group_1, published=True)
        Asset.objects.create(name='Test', content='test content', group=group_2, published=True)
        request = self.factory.get('/')
        with self.assertNumQueries(2):
            add_assets(request)
