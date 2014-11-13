# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

try:
    # Only import from platforms if it is a dependancy
    from publica_platforms import views as platforms_views

    # Use platform mixin if platforms is found as a dependancy
    PlatformListMixin = platforms_views.PlatformListMixin
    PlatformDetailMixin = platforms_views.PlatformDetailMixin
except ImportError:
    PlatformDetailMixin = PlatformListMixin = object

from .models import Page


class AllPages(PlatformListMixin, ListView):
    model = Page
    template_name = 'pages/page_list.html'

    def get_queryset(self):
        return super(AllPages, self).get_queryset().filter(enabled=True)


class DetailPage(PlatformDetailMixin, DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

    def get_queryset(self):
        return super(DetailPage, self).get_queryset().filter(enabled=True)


all_pages = AllPages.as_view()
detail = DetailPage.as_view()
