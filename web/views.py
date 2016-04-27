from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry


def home(request):
    entries = Entry.objects.all()

    context = {
        'valami': 'Szaki',
        'entries': entries
    }
    return render(request, 'entries.html', context)


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ('title', 'description', 'url', 'logo')
    template_name = 'create_entry.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(EntryCreateView, self).form_valid(form)
