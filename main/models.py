from django.db import models
from datetime import datetime


class Suppliers(models.Model):
    id_code = models.CharField(
        unique=True, max_length=50, default=None, blank=True, null=True)
    name = models.CharField(max_length=50,
                            default=None, blank=True, null=True)
    code = models.CharField(max_length=4, default=None, blank=True, null=True)
    vat_number = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    tax_code = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    address_city = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    address_province = models.TextField(
        max_length=20, default=None, blank=True, null=True)
    country = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now)
    manually_changed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id_code)


class Invoices(models.Model):
    id_code = models.BigIntegerField(
        unique=True, default=None, blank=True, null=True)
    invoices_type = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    description = models.TextField(
        max_length=200, default=None, blank=True, null=True)
    date = models.DateField(default=None, blank=True, null=True)
    amount_net = models.FloatField(default=None, blank=True, null=True)
    amount_vat = models.FloatField(default=None, blank=True, null=True)
    amount_gross = models.FloatField(default=None, blank=True, null=True)
    supplier = models.ForeignKey(Suppliers, to_field="id_code",
                                 on_delete=models.CASCADE, default=None, blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now)
    supplier_name = models.TextField(
        max_length=100, default=None, blank=True, null=True)
    supplier_tax_code = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    supplier_vat_number = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    category = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    rc_center = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    manually_changed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id_code)


class InvoicesLines(models.Model):
    id_code = models.ForeignKey(
        Invoices, to_field="id_code", on_delete=models.CASCADE)
    id_line = models.BigIntegerField(
        unique=True, default=None, blank=True, null=True)
    date = models.DateField(default=None, blank=True, null=True)
    currency = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    # add to database mannually
    rc_center = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    category = models.TextField(
        max_length=50, default=None, blank=True, null=True)
    name = models.TextField(max_length=50, default=None, blank=True, null=True)
    qty = models.FloatField(default=None, blank=True, null=True)
    net_price = models.FloatField(default=None, blank=True, null=True)
    vat = models.FloatField(default=None, blank=True, null=True)
    manually_changed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id_code)
