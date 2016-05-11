from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import login
from .models import Entry


def custom_login(request, *args, **kwargs):
    response = login(request, *args, **kwargs)

    if request.user.is_authenticated():
        messages.info(request, "Welcome ...")

    return response


class EntriesTemplateView(TemplateView):
    template_name = 'entries.html'

    def get_context_data(self, **kwargs):
        entries = Entry.objects.all()
        context = {
            'entries': entries,
            'indorm': False,
        }
        return context


class InDormitoryTemplateView(TemplateView):
    template_name = 'entries.html'

    def get_context_data(self, **kwargs):
        entries = Entry.objects.filter(in_dorm=True)
        context = {
            'entries': entries,
            'indorm': True,
        }
        return context


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ('title', 'description', 'url', 'in_dorm', 'logo')
    template_name = 'create_entry.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(EntryCreateView, self).form_valid(form)
