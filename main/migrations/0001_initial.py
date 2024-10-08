# Generated by Django 5.1 on 2024-09-04 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.BigIntegerField(blank=True, default=None, null=True, unique=True)),
                ('invoices_type', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('amount_net', models.FloatField(blank=True, default=None, null=True)),
                ('amount_vat', models.FloatField(blank=True, default=None, null=True)),
                ('amount_gross', models.FloatField(blank=True, default=None, null=True)),
                ('supplier_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('category', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('rc_center', models.TextField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.CharField(blank=True, default=None, max_length=50, null=True, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=50, null=True, unique=True)),
                ('code', models.CharField(blank=True, default=None, max_length=4, null=True)),
                ('vat_number', models.CharField(blank=True, default=None, max_length=20, null=True, unique=True)),
                ('tax_code', models.CharField(blank=True, default=None, max_length=20, null=True, unique=True)),
                ('address_city', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('address_province', models.TextField(blank=True, default=None, max_length=20, null=True)),
                ('country', models.TextField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoicesLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_line', models.BigIntegerField(blank=True, default=None, null=True, unique=True)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('currency', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('rc_center', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('category', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('name', models.TextField(blank=True, default=None, max_length=50, null=True)),
                ('qty', models.FloatField(blank=True, default=None, null=True)),
                ('net_price', models.FloatField(blank=True, default=None, null=True)),
                ('vat', models.FloatField(blank=True, default=None, null=True)),
                ('created_at', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('updated_at', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('id_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.invoices', to_field='id_code')),
            ],
        ),
        migrations.AddField(
            model_name='invoices',
            name='supplier',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_id', to='main.suppliers', to_field='id_code'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='supplier_tax_code',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_tax_code', to='main.suppliers', to_field='tax_code'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='supplier_vat_number',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_vat_number', to='main.suppliers', to_field='vat_number'),
        ),
    ]
