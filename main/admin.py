from django.contrib import admin
from .models import Invoices, InvoicesLines, Suppliers

# Register your models here.
admin.site.register(Invoices)
admin.site.register(InvoicesLines)
admin.site.register(Suppliers)