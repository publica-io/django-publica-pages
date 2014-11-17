#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-publica-pages
------------

Tests for `django-publica-pages` models module.
"""

import os
import shutil
import unittest

from pages import models
from templates.models import Template



class TestPublica_pages(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass




class WidgetsTestCase(unittest.TestCase):
    def setUp(self):

        self.t1, _ = Template.objects.get_or_create(
            name='pages/page_object.html', content='test')

        models.Page.objects.create(
            title='This is my long page title',
            short_title='Page Short Title',
            slug='this-is-my-long-page-title',
            enabled=True,
            text='here goes the long text like a lorem ipsum or something',
            featured=True,
            template=self.t1,
            preview_template=self.t1
        )

    def test_page_creation(self):
        page = models.Page.objects.get(slug='this-is-my-long-page-title')

        self.assertEqual(page.title, 'This is my long page title')
        self.assertEqual(page.short_title, 'Page Short Title')
        self.assertEqual(page.slug, 'this-is-my-long-page-title')
        self.assertEqual(page.enabled, True)
        self.assertEqual(
            page.text,
            'here goes the long text like a lorem ipsum or something'
        )
        self.assertEqual(page.featured, True)
