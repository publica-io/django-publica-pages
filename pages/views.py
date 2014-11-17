# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

from .models import Page


class Pages(ListView):
    model = Page
    template_name = 'pages/page_list.html'

    def get_queryset(self):
        return super(Pages, self).get_queryset().filter(enabled=True)


class Page(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

    def get_queryset(self):
        return super(Page, self).get_queryset().filter(enabled=True)


pages = Pages.as_view()
page = Page.as_view()
