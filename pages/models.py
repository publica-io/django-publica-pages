# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models

from entropy.base import (
    SlugMixin, TitleMixin, TextMixin, ModifiedMixin, CreatedMixin,
    PublishingStatusMixin, AttributeMixin
)
from entropy.fields import EnabledField


class Page(SlugMixin, TitleMixin, TextMixin, ModifiedMixin, CreatedMixin,
           PublishingStatusMixin, AttributeMixin):

    enabled = EnabledField()
    featured = models.BooleanField(default=False)
    published_date = models.DateField(null=True)

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
