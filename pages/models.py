# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from entropy.mixins import (
    SlugUniqueMixin, TitleMixin, TextMixin, ModifiedMixin, CreatedMixin, EnabledMixin
)
from images.mixins import ImageMixin
from templates.mixins import TemplateMixin

try:
    from publica_admin.mixins import PublicaAdminMixin
except ImportError:
    PublicaAdminMixin = object


class Page(TitleMixin, SlugUniqueMixin, ImageMixin, EnabledMixin, TextMixin, TemplateMixin, PublicaAdminMixin):

    # title
    # short_title
    # slug
    # enabled
    # text

    class Meta:
        verbose_name = 'Content Page'
        verbose_name_plural = 'Page Content'

    def get_absolute_url(self):
        return reverse('pages_page', args=(self.slug, ))

    @staticmethod
    def get_list_url():
        return reverse('pages_pages')
