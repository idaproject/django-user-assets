# -*- coding: utf-8 -*-
from django.core.validators import validate_slug
from django.db import models


class AssetGroup(models.Model):
    name = models.CharField('Название', max_length=100)
    key = models.CharField('Ключ', max_length=20, validators=[validate_slug], db_index=True)

    class Meta:
        verbose_name = "Група кодов"
        verbose_name_plural = "Группы кодов"

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField('Название', max_length=100)
    group = models.ForeignKey(AssetGroup, verbose_name='Группа кодов')
    content = models.TextField('Контент')
    order = models.PositiveIntegerField(default=0, db_index=True)
    published = models.BooleanField('Опубликован', default=False, db_index=True)

    class Meta:
        verbose_name = "Код"
        verbose_name_plural = "Коды"
        ordering = ('order',)

    def __str__(self):
        return self.name
