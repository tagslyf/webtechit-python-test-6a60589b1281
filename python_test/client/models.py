from django.db import models
from django.urls import reverse


class Client(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    suburb = models.CharField(max_length=255, db_index=True,
                              null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, db_index=True)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})
