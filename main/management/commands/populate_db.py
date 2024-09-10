from main.services.invoices_api_client import InvoicesApiClient
from django.core.management.base import BaseCommand
# Importa i modelli necessari
from main.models import Invoices, Suppliers, InvoicesLines
from datetime import datetime


class Command(BaseCommand):
    help = 'Popolate database with initial data'

    def handle(self, *args, **kwargs):
        TOKEN = "API TOKEN"
        COMPANY_ID = "INSERT COMANY ID"
        HOST = "https://api-v2.fattureincloud.it"
        PER_PAGE = 100
        PAGE = 10
        TYPE = "expense"
        field_list_documents = "id,type,description,date,amount_net,amount_vat,amount_gross,entity,category,rc_center,updated_at"
        field_list_suppliers = "id,name,code,vat_number,tax_code,address_city,address_province,country,updated_at"

        invoices = InvoicesApiClient(TOKEN, COMPANY_ID, HOST)

        received_documents = invoices.get_list_received_documents(
            TYPE, PAGE, PER_PAGE, fields=field_list_documents)
        documents_lines = invoices.get_received_document_lines()
        list_suppliers = invoices.get_list_suppliers(PAGE, PER_PAGE, fields=field_list_suppliers)

        for supplier in list_suppliers:
            id_code = supplier.get('id', None)
            name = supplier.get('name', None)
            code = supplier.get('code', None)
            vat_number = supplier.get('vat_number', None)
            tax_code = supplier.get('tax_code', None)
            address_city = supplier.get('address_city', None)
            address_province = supplier.get('address_province', None)
            country = supplier.get('country', None)
            updated_at_str = supplier.get('updated_at', None)
            updated_at = datetime.strptime(updated_at_str, "%Y-%m-%d %H:%M:%S")
            
            if not Suppliers.objects.filter(id_code=id_code).exists():
                Suppliers.objects.create(
                    id_code=id_code,
                    name=name,
                    code=code,
                    vat_number=vat_number,
                    tax_code=tax_code,
                    address_city=address_city,
                    address_province=address_province,
                    country=country
                )
            elif Suppliers.objects.filter(id_code=id_code).get().updated_at  < updated_at:
                Suppliers.objects.filter(id_code=id_code).update(
                    name=name,
                    code=code,
                    vat_number=vat_number,
                    tax_code=tax_code,
                    address_city=address_city,
                    address_province=address_province,
                    country=country,
                    updated_at = datetime.now()
                )

        # loop through each received_documents page
        for page in received_documents:
            # for each page loop through all the invoices
            for invoice in page['data']:
                invoice_id = invoice.get('id')
                invoice_type = invoice.get('type', None)
                description = invoice.get('description', None)
                date = invoice.get('date', None)
                amount_net = invoice.get('amount_net', None)
                amount_vat = invoice.get('amount_vat', None)
                amount_gross = invoice.get('amount_gross', None)
                supplier = invoice.get("entity", {}).get("id", None)
                supplier_name = invoice.get("entity", {}).get("name", None)
                supplier_tax_code = invoice.get(
                    "entity", {}).get("tax_code", None)
                supplier_vat_number = invoice.get(
                    "entity", {}).get("vat_number", None)
                category = invoice.get("category")
                rc_center = invoice.get("rc_center")
                updated_at_str = invoice.get("updated_at")
                updated_at = datetime.strptime(updated_at_str, "%Y-%m-%d %H:%M:%S")
                
                try:
                    supplier_instance = Suppliers.objects.get(id_code=supplier)
                except Suppliers.DoesNotExist:
                    supplier_instance = None
                # check if there is a touple with this id_code
                if not Invoices.objects.filter(id_code=invoice_id).exists():
                    Invoices.objects.create(
                        id_code=invoice_id,
                        invoices_type=invoice_type,
                        description=description,
                        date=date,
                        amount_net=amount_net,
                        amount_vat=amount_vat,
                        amount_gross=amount_gross,
                        supplier=supplier_instance,
                        supplier_name=supplier_name,
                        supplier_tax_code=supplier_tax_code,
                        supplier_vat_number=supplier_vat_number,
                        rc_center=rc_center,
                        category=category,
                        updated_at = updated_at

                    )
                elif Invoices.objects.filter(id_code=invoice_id).get().updated_at < updated_at:
                    Invoices.objects.filter(id_code=invoice_id).update(
                        invoices_type=invoice_type,
                        description=description,
                        date=date,
                        amount_net=amount_net,
                        amount_vat=amount_vat,
                        amount_gross=amount_gross,
                        supplier=supplier_instance,
                        rc_center=rc_center,
                        category=category,
                        supplier_tax_code=supplier_tax_code,
                        supplier_vat_number=supplier_vat_number,
                        updated_at = datetime.now()
                    )

        # loop through each document
        for document in documents_lines:
            data = document['data']
            id_code = data.get('id', None)
            date = data.get('date', None)
            currency = data.get('currency', {}).get('id', None)
            items_list = data.get('items_list', None)
            updated_at_str = data.get('updated_at', None)
            updated_at = datetime.strptime(updated_at_str, "%Y-%m-%d %H:%M:%S")
            
            if items_list:
                for item in items_list:
                    id_line = item.get('id', None)
                    category = item.get('category', None)
                    name = item.get('name', None)
                    qty = item.get('qty', None)
                    net_price = item.get('net_price', None)
                    vat = item.get('vat', {}).get('value', None)

                    if not InvoicesLines.objects.filter(id_line=id_line).exists():
                        InvoicesLines.objects.create(
                            id_line=id_line,
                            id_code=Invoices.objects.get(id_code=id_code),
                            date=date,
                            currency=currency,
                            rc_center=Invoices.objects.get(id_code=id_code).rc_center,
                            category=Invoices.objects.get(id_code=id_code).category,
                            name=name,
                            qty=qty,
                            net_price=net_price,
                            vat=vat,
                        )
                    elif Invoices.objects.filter(id_code=id_code).get().updated_at < updated_at:
                        InvoicesLines.objects.filter(id_line=id_line).update(
                            id_code=Invoices.objects.get(id_code=id_code),
                            date=date,
                            currency=currency,
                            name=name,
                            qty=qty,
                            net_price=net_price,
                            vat=vat,
                        )
            else:
                if not InvoicesLines.objects.filter(id_code=id_code).exists():
                    InvoicesLines.objects.create(
                        id_line=None,
                        id_code=Invoices.objects.get(id_code=id_code),
                        date=date,
                        currency=currency,
                        rc_center=Invoices.objects.get(id_code=id_code).rc_center,
                        category=Invoices.objects.get(id_code=id_code).category,
                        name=Invoices.objects.get(id_code=id_code).description,
                        qty=1,
                        net_price=Invoices.objects.get(id_code=id_code).amount_net,
                        vat=None,
                    )
                elif Invoices.objects.filter(id_code=id_code).get().updated_at < updated_at:
                    InvoicesLines.objects.filter(id_line=id_line).update(
                        date=date,
                        id_code=Invoices.objects.get(id_code=id_code),
                        currency=currency,
                    )

        self.stdout.write(self.style.SUCCESS('Database successfully popolate'))
