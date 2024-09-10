import fattureincloud_python_sdk as invoices
from fattureincloud_python_sdk.rest import ApiException


class InvoicesApiClient():
    def __init__(self, token: str, company_id: int, host: str) -> None:
        self.company_id = company_id
        self.host = host
        self.configuration = invoices.Configuration(host)
        self.configuration.access_token = token
        self.api_client = invoices.ApiClient(self.configuration)
        self.documents_id = []

    def get_list_received_documents(self, type: str, page: int = 10, per_page: int = 100, fields: str = None):
        received_documents = invoices.ReceivedDocumentsApi(self.api_client)
        data = []
        try:
            for i in range(1, page+1):
                api_response = received_documents.list_received_documents(
                    self.company_id, type, page=i, per_page=per_page, fields=fields)
                data_dictionary = api_response.to_dict()
                data.append(data_dictionary)
                for element in data_dictionary['data']:
                    self.documents_id.append(element['id'])
        except ApiException as e:
            print(
                "Exception when calling ReceivedDocumentsApi->get_list_received_documents: %s\n" % e)
        return data

    def get_received_document_lines(self):
        documents_lines = []
        received_documents = invoices.ReceivedDocumentsApi(self.api_client)
        for document_id in self.documents_id:
            try:
                api_response = received_documents.get_received_document(
                    self.company_id, document_id)
                data_dictionary = api_response.to_dict()
                documents_lines.append(data_dictionary)
            except ApiException as e:
                print(
                    "Exception when calling ReceivedDocumentsApi->get_received_documents: %s\n" % e)
        return documents_lines

    def get_list_suppliers(self, page: int = 10, per_page: int = 100, fields: str = None):
        api_suppliers = invoices.SuppliersApi(self.api_client)
        suppliers = []
        try:
            for i in range(1, page+1):
                api_response = api_suppliers.list_suppliers(
                    self.company_id, page=i, per_page=per_page, fields=fields)
                data_dictionary = api_response.to_dict()
                for elem in data_dictionary["data"]:
                    suppliers.append(elem)
        except ApiException as e:
            print("Exception when calling SuppliersApi->get_list_suppliers: %s\n" % e)
        return suppliers
