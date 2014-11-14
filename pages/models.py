# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from entropy.base import (
    SlugMixin, TitleMixin, TextMixin, ModifiedMixin, CreatedMixin,
    AttributeMixin, EnabledMixin
)
from templates.mixins import TemplateMixin


class Page(TitleMixin, SlugMixin, EnabledMixin, TextMixin, CreatedMixin,
           ModifiedMixin, AttributeMixin, TemplateMixin):

    # title
    # short_title
    # slug
    # enabled
    # text
    # created_at
    # created_by
    # modified_at
    # modified_by
    # attributes

    featured = models.BooleanField(default=False)
    published_at = models.DateField(null=True)

    def get_absolute_url(self):
        """
        Returns the absolute url for a single page instance

        """

        return reverse('pages_detail_page', args=(self.slug, ))

    @staticmethod
    def get_list_url():
        """
        Returns the absolute url for all page objects.
        This is a static method.

        """

        return reverse('pages_all_pages')
