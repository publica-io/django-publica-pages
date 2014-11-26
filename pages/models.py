# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from entropy.mixins import (
    SlugMixin, TitleMixin, TextMixin, ModifiedMixin, CreatedMixin, EnabledMixin
)
from images.mixins import ImageMixin
from templates.mixins import TemplateMixin


class Page(TitleMixin, SlugMixin, ImageMixin, EnabledMixin, TextMixin, TemplateMixin):

    # title
    # short_title
    # slug
    # enabled
    # text

    def get_absolute_url(self):
        return reverse('pages_page', args=(self.slug, ))

    @staticmethod
    def get_list_url():
        return reverse('pages_pages')
