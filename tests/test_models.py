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

from django.contrib.contenttypes.models import ContentType

from pages import models
from templates.models import Template
from menus.models import Menu, MenuItem, Link
from menus.factories import MenuFactory, LinkFactory, MenuItemFactory


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

        self.page, _ = models.Page.objects.get_or_create(
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

        self.t1, _ = Template.objects.get_or_create(
            name='pages/page_object.html', content='test')

        self.page, _ = models.Page.objects.get_or_create(
            title='This is my long page title',
            short_title='Page Short Title',
            slug='this-is-my-long-page-title',
            enabled=True,
            text='here goes the long text like a lorem ipsum or something',
            featured=True,
            template=self.t1,
            preview_template=self.t1
        )

        self.assertEqual(self.page.title, 'This is my long page title')
        self.assertEqual(self.page.short_title, 'Page Short Title')
        self.assertEqual(self.page.slug, 'this-is-my-long-page-title')
        self.assertEqual(self.page.enabled, True)
        self.assertEqual(
            self.page.text,
            'here goes the long text like a lorem ipsum or something'
        )
        self.assertEqual(self.page.featured, True)


class TestMenuTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Will crete a menu,
        Will create a page and link it to content type
        display menu using the template tag.
        :return:
        '''

        self.t1, _ = Template.objects.get_or_create(
            name='pages/page_test.html', content='test')

        self.page, _ = models.Page.objects.get_or_create(
            title='This is my long page title',
            short_title='Page Short Title',
            slug='this-is-my-long-page-title',
            enabled=True,
            text='here goes the long text like a lorem ipsum or something',
            featured=True,
            template=self.t1,
            preview_template=self.t1
        )

        self.link = Link(title='Title1',
                         content_type=ContentType.objects.get_for_model(self.page)
        )

        self.menu = MenuFactory(title='Title1', slug='Slug1', enabled=True)
        self.menu_item = MenuItemFactory(menu=self.menu, link=self.link,
                                                   order=0, is_featured=True,
                                                   parent=None)

        def test_nothing(self):
            pass
