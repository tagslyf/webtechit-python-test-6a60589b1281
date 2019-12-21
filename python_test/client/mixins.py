from django.core.exceptions import ImproperlyConfigured


class ListFilteredMixin(object):
    """
        Mixin that adds support for django-filter
    """

    filter_set = None

    def get_filter_set(self):
        if self.filter_set:
            return self.filter_set
        else:
            raise ImproperlyConfigured(
                "ListFilterMixin requires either a definition of "
                "'filter_set' or an implementation of 'get_filter()'")

    def get_filter_set_kwargs(self):
        return {
            'data': self.request.GET,
            'queryset': self.get_base_queryset(),
        }

    def get_base_queryset(self):
        return super(ListFilteredMixin, self).get_queryset()

    def get_constructed_filter(self):
        if getattr(self, 'constructed_filter', None):
            return self.constructed_filter
        else:
            f = self.get_filter_set()(**self.get_filter_set_kwargs())
            self.constructed_filter = f
            return f

    def get_queryset(self):
        return self.get_constructed_filter().qs

    def get_context_data(self, **kwargs):
        kwargs.update({'filter': self.get_constructed_filter()})
        return super(ListFilteredMixin, self).get_context_data(**kwargs)
