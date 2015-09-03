# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

from aldryn_apphooks_config.utils import setup_config
from aldryn_apphooks_config.models import AppHookConfig
from app_data import AppDataForm
from parler.models import TranslatableModel
from parler.models import TranslatedFields

from .settings import get_setting


class BlogConfig(TranslatableModel, AppHookConfig):
    """
    Adds some translatable, per-app-instance fields.
    """
    translations = TranslatedFields(
        app_title=models.CharField(_('application title'), max_length=234),
    )

    def get_app_title(self):
        return getattr(self, 'app_title', _('untitled'))


class BlogConfigForm(AppDataForm):
    default_published = forms.BooleanField(label=_('Post published by default'), required=False,
                                           initial=get_setting('DEFAULT_PUBLISHED'))
    use_placeholder = forms.BooleanField(label=_('Use placeholder and plugins for article body'),
                                         required=False,
                                         initial=get_setting('USE_PLACEHOLDER'))
    use_abstract = forms.BooleanField(label=_('Use abstract field'),
                                      required=False,
                                      initial=get_setting('USE_ABSTRACT'))
    set_author = forms.BooleanField(label=_('Set author'),
                                    required=False,
                                    help_text=_('Set author by default'),
                                    initial=get_setting('AUTHOR_DEFAULT'))
    paginate_by = forms.IntegerField(label=_('Paginate size'),
                                     required=False,
                                     initial=get_setting('PAGINATION'),
                                     help_text=_('When paginating list views, '
                                                 'how many articles per page?'))
setup_config(BlogConfigForm, BlogConfig)