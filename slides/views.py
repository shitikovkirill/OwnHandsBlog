import time
import datetime
import socket
import json

from django.views import generic
from django.http import HttpResponse
from django.shortcuts import (render, render_to_response, redirect, get_object_or_404)
from django.core.mail import (send_mail, BadHeaderError)
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.conf import settings
from django.db.models import (Q, Count)

from .models import *


class HomepageView(generic.ListView):
    queryset = Category.objects.all()
    template_name = 'slides/home.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context_data = super(HomepageView, self).get_context_data(**kwargs)
        return context_data


class PageView(generic.ListView):
    queryset = []
    template_name = 'slides/page.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context_data = {}
        return context_data
