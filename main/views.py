from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Invoices, Suppliers, InvoicesLines
from django.utils.dateparse import parse_date
from datetime import datetime


def home(request):
    return render(request, 'home.html')


def invoice(request):
    invoices = None
    error_message = None

    if request.method == "GET" and 'invoice_id_code' in request.GET:
        invoice_id_code = request.GET.get('invoice_id_code', None)
        name_field = request.GET.get('supplier_name', None)
        supplier_name = None
        for invoice in Invoices.objects.all():
            if name_field.lower() in invoice.supplier_name.lower():
                supplier_name = invoice.supplier_name

        if invoice_id_code or supplier_name:
            try:
                if invoice_id_code:
                    invoices = [Invoices.objects.get(id_code=invoice_id_code)]
                elif supplier_name:
                    invoices = Invoices.objects.filter(
                        supplier_name=supplier_name)
            except Invoices.DoesNotExist:
                error_message = "Invoice not found."
        else:
            error_message = "Please enter an Invoice ID Code or Supplier Name."

    return render(request, 'invoice.html', {'invoices': invoices, 'error_message': error_message})


def supplier(request):
    suppliers = None
    error_message = None
    if request.method == "GET" and 'supplier_id_code' in request.GET:
        supplier_id_code = request.GET.get('supplier_id_code')
        name_field = request.GET.get('supplier_name', None)
        supplier_name = None
        for supplier in Suppliers.objects.all():
            if name_field.lower() in supplier.name.lower():
                supplier_name = supplier.name
        if supplier_id_code or supplier_name:
            try:
                if supplier_id_code:
                    suppliers = [Suppliers.objects.get(
                        id_code=supplier_id_code)]
                elif supplier_name:
                    suppliers = Suppliers.objects.filter(name=supplier_name)
            except Suppliers.DoesNotExist:
                error_message = "Supplier not found."
        else:
            error_message = "Please enter an Invoice ID Code or Supplier Name."
    return render(request, 'supplier.html', {'suppliers': suppliers, 'error_message': error_message})


def details_invoice(request, id_code):
    invoice = get_object_or_404(Invoices, id_code=id_code)
    lines = InvoicesLines.objects.filter(id_code=id_code)
    return render(request, 'details_invoice.html', {'invoice': invoice, "lines": lines})


def details_supplier(request, id_code):
    supplier = get_object_or_404(Suppliers, id_code=id_code)
    return render(request, 'details_supplier.html', {'supplier': supplier})


def edit_invoice(request):
    if request.method == "POST":
        id_code = request.POST.get('id_code')
        invoices_type = request.POST.get('invoices_type')
        description = request.POST.get('description')
        amount_net = request.POST.get('amount_net')
        amount_vat = request.POST.get('amount_vat')
        amount_gross = request.POST.get('amount_gross')
        if amount_gross == "":
            amount_gross = None
        supplier = request.POST.get('supplier')
        try:
            invoice = Invoices.objects.get(id_code=id_code)
            invoice.invoices_type = invoices_type
            invoice.description = description
            invoice.amount_net = amount_net
            invoice.amount_vat = amount_vat
            invoice.amount_gross = amount_gross
            invoice.supplier = Suppliers.objects.get(id_code=supplier)
            invoice.manually_changed = True
            invoice.updated_at = datetime.now()

            invoice.save()
            return redirect('details_invoice', id_code)
        except Invoices.DoesNotExist:
            return HttpResponse("Invoice not found.", status=404)
    return HttpResponse("Invalid request method.", status=405)


def edit_lines(request):
    if request.method == 'POST':
        currency = request.POST.get('currency')
        rc_center = request.POST.get('rc_center')
        category = request.POST.get('category')
        id_line = request.POST.get('id_line')
        try:
            line = InvoicesLines.objects.get(id_line=id_line)
            line.currency = currency
            line.rc_center = rc_center
            line.category = category
            line.manually_changed = True
            invoice = line.id_code
            invoice.updated_at = datetime.now()
            line.save()

            return redirect('details_invoice', line.id_code)
        except InvoicesLines.DoesNotExist:
            return HttpResponse("Invoice not found.", status=404)
    return HttpResponse("Invalid request method.", status=405)


def add_lines(request):
    if request.method == 'POST':
        print(request.POST)
        id_code = request.POST.get('id_code')
        date = datetime.today()
        currency = request.POST.get('currency')
        rc_center = request.POST.get('rc_center')
        category = request.POST.get('category')
        name = request.POST.get('name')
        qty = request.POST.get('qty')
        net_price = request.POST.get('net_price')
        vat = request.POST.get('vat')
        manually_changed = True

        InvoicesLines.objects.create(
            id_line=None,
            id_code=Invoices.objects.get(id_code=id_code),
            date=date,
            currency=currency,
            rc_center=rc_center,
            category=category,
            name=name,
            qty=qty,
            net_price=net_price,
            vat=vat,
            manually_changed=manually_changed
        )
        return redirect('details_invoice', id_code)
    return HttpResponse("Invalid request method.", status=405)
