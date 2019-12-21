from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .filters import ClientFilter
from .mixins import ListFilteredMixin
from .models import Client


class ClientList(ListFilteredMixin, ListView):
    model = Client
    filter_set = ClientFilter

    def get_queryset(self):
        qs = super().get_queryset()

        order_by = self.request.GET.get('order_by')
        if order_by:
            ordering = self.request.GET.get('ordering')
            if ordering == 'des':
                order_by = f'-{order_by}'

            return qs.order_by(order_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get('name')
        email = self.request.GET.get('email')
        phone_number = self.request.GET.get('phone_number')
        suburb = self.request.GET.get('suburb')

        context.update(filter_by={
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'suburb': suburb
        })

        order_by = self.request.GET.get('order_by')
        if order_by:
            ordering = self.request.GET.get('ordering')
            context.update(order_by=order_by, ordering=ordering)

        return context


class ClientDetail(DetailView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    fields = ['name', 'email', 'street', 'suburb', 'postcode', 'state',
              'contact_person', 'phone_number']


class ClientUpdate(UpdateView):
    model = Client
    fields = ['name', 'street', 'suburb', 'postcode', 'state', 'email',
              'contact_person', 'phone_number']
