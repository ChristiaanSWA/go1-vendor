import frappe



@frappe.whitelist()
def get_sales():
    quotation=frappe.get_meta('Request for Quotation')
    return quotation

@frappe.whitelist()
def get_purchase():
    meta=frappe.get_meta('Purchase Order')
    return meta

@frappe.whitelist()
def get_supplier():
    supplier=frappe.get_meta('Supplier Quotation')
    return supplier

@frappe.whitelist()
def get_invoice():
    invoice=frappe.get_meta('Purchase Invoice')
    return invoice

@frappe.whitelist()
def get_navbar_routes():
    check=frappe.get_single('Go1 Navbar Settings')
    user_details = frappe.get_all("Sidebar Settings", filters={'parent': 'Go1 Navbar Settings','enabled':1}, fields=['*'])
    return user_details
@frappe.whitelist()
def get_issues():
    issue = frappe.db.get_all("Issue", fields=['*'])
    return issue

@frappe.whitelist()
def get_username():
   current_user=frappe.session.user
   user_detail = frappe.get_all("User", filters={'name': current_user}, fields=['full_name'])
   return user_detail[0].full_name

@frappe.whitelist()
def get_requestquotation():
    materialreq = frappe.db.get_all("Request for Quotation", fields=['*'])
    materialreq_items = frappe.db.get_all("Request for Quotation Item", fields=["*"])
    materialreq_suppiler= frappe.db.get_all("Request for Quotation Supplier", fields=["*"])
    materialreq_docs = []
    
    for mr in materialreq:
        items = []
        suppilers=[]
        for item in materialreq_items:
            if item["parent"] == mr["name"]:
                items.append(item)
        for item in materialreq_suppiler:
            if item["parent"] == mr["name"]:
                suppilers.append(item)
        mr["items"] = items
        mr["suppliers"] = suppilers
        materialreq_docs.append(mr)
    return materialreq_docs


@frappe.whitelist()
def get_purchaseorder():
    materialreq = frappe.db.get_all("Purchase Order", fields=['*'])
    materialreq_items = frappe.db.get_all("Purchase Order Item", fields=["*"])
    materialreq_suppiler= frappe.db.get_all("Purchase Taxes and Charges", fields=["*"])
    materialreq_docs = []
    
    for mr in materialreq:
        items = []
        taxes=[]
        for item in materialreq_items:
            if item["parent"] == mr["name"]:
                items.append(item)
        for item in materialreq_suppiler:
            if item["parent"] == mr["name"]:
                taxes.append(item)
        mr["items"] = items
        mr["taxes"] = taxes
        materialreq_docs.append(mr)
    return materialreq_docs

@frappe.whitelist()
def get_supplierquotation():
    materialreq = frappe.db.get_all("Supplier Quotation", fields=['*'])
    materialreq_items = frappe.db.get_all("Supplier Quotation Item", fields=["*"])
    materialreq_suppiler= frappe.db.get_all("Purchase Taxes and Charges", fields=["*"])
    materialreq_docs = []
    
    for mr in materialreq:
        items = []
        taxes = []
        for item in materialreq_items:
            if item["parent"] == mr["name"]:
                items.append(item)
        for item in materialreq_suppiler:
            if item["parent"] == mr["name"]:
                taxes.append(item)
        mr["items"] = items
        mr["taxes"] = taxes
        materialreq_docs.append(mr)
    return materialreq_docs

@frappe.whitelist()
def get_purchaseinvoice():
    materialreq = frappe.db.get_all("Purchase Invoice", fields=['*'])
    materialreq_items = frappe.db.get_all("Purchase Invoice Item", fields=["*"])
    materialreq_suppiler= frappe.db.get_all("Purchase Taxes and Charges", fields=["*"])
    materialreq_docs = []
    
    for mr in materialreq:
        items = []
        taxes=[]
        for item in materialreq_items:
            if item["parent"] == mr["name"]:
                items.append(item)
        for item in materialreq_suppiler:
            if item["parent"] == mr["name"]:
                taxes.append(item)
        mr["items"] = items
        mr["taxes"] = taxes
        materialreq_docs.append(mr)
    return materialreq_docs
# Address api
 
# @frappe.whitelist()
# def get_address():
#     users_data = getcustomer()
#     address_list = []
#     addresses = frappe.db.get_all("Address", fields=['*'])
 
#     for address in addresses:
#         links = frappe.db.get_all("Dynamic Link", fields=['*'], filters={'parent': address['name']})
#         address['links'] = links
#         address_list.append(address)
 
#     address_data = []
#     for address in address_list:
#         for link in address['links']:
#             if link['link_name'] in users_data:
#                 address_data.append(address)
 
#     return address_data
 
   
