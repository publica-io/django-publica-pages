# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import Page


class WidgetsTestCase(TestCase):
    def setUp(self):
        Page.objects.create(
            title='This is my long page title',
            short_title='Page Short Title',
            slug='this-is-my-long-page-title',
            enabled=True,
            text='here goes the long text like a lorem ipsum or something',
            featured=True,
        )

    def test_page_creation(self):
        page = Page.objects.get(slug='this-is-my-long-page-title')

        self.assertEqual(page.title, 'This is my long page title')
        self.assertEqual(page.short_title, 'Page Short Title')
        self.assertEqual(page.slug, 'this-is-my-long-page-title')
        self.assertEqual(page.enabled, True)
        self.assertEqual(
            page.text,
            'here goes the long text like a lorem ipsum or something'
        )
        self.assertEqual(page.featured, True)
