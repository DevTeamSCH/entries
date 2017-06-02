from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Entry


def logout_view(request):
    logout(request)
    return redirect("home")

class SearchMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('s')
        if search is not None:
            context['entries'] = Entry.objects.filter(title__contains=search)
        else:
            context['entries'] = Entry.objects.all()
        return context


class EntriesPaginationMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.entries, 25)

        page = self.request.GET.get('page')
        try:
            context['entries'] = paginator.page(page)
        except PageNotAnInteger:
            context['entries'] = paginator.page(1)
        except EmptyPage:
            context['entries'] = paginator.page(paginator.num_pages)

        context['page_numbers'] = range(1, paginator.num_pages+1)
        return context


class EntriesTemplateView(SearchMixin, EntriesPaginationMixin, TemplateView):
    template_name = 'entries.html'

    def get_context_data(self, **kwargs):
        self.entries = Entry.objects.all()
        context = super().get_context_data(**kwargs)
        context['indorm'] = False

        return context


class InDormitoryTemplateView(SearchMixin, EntriesPaginationMixin, TemplateView):
    template_name = 'entries.html'

    def get_context_data(self, **kwargs):
        self.entries = Entry.objects.filter(in_dorm=True)
        context = super().get_context_data(**kwargs)
        context['indorm'] = True
        return context


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ('title', 'description', 'url', 'in_dorm', 'logo')
    template_name = 'create_entry.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(EntryCreateView, self).form_valid(form)
