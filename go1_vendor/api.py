import frappe
from frappe import _

# Request for quotation
@frappe.whitelist()
def get_quotation():
    my_data=get_test()
    
    
    filters={}
    if my_data:
        filters={'supplier': my_data}
    quotations = frappe.db.get_all("Request for Quotation", fields=['*'], filters=filters)
    supplier_item =frappe.db.get_all("Request for Quotation Supplier", fields=['*'])
   
    quotation_docs = []

    for quotation in quotations:
        # items = []
        suppliers=[]
        # for item in quotation_items:
        #     if item["parent"] == quotation["name"]:
        #         items.append(item)
        # quotation["items"] = items
        for supplier in supplier_item:
            if supplier["parent"]==quotation["name"]:
                suppliers.append(supplier)
        quotation["suppliers"] = supplier
        quotation_docs.append(quotation)

    return quotation_docs
# Purchase order
@frappe.whitelist()
def get_purchaseorder():
    my_data=get_test()
    
    
    filters={}
    if my_data:
        filters={'supplier': my_data}
    quotations = frappe.db.get_all("Purchase Order", fields=['*'], filters=filters)
    supplier_item =frappe.db.get_all("Purchase Order Item", fields=['*'])
    quotation_docs = []

    for quotation in quotations:
        suppliers=[]
        for supplier in supplier_item:
            if supplier["parent"]==quotation["name"]:
                suppliers.append(supplier)
        quotation["suppliers"] = supplier
        quotation_docs.append(quotation)

    return quotation_docs
# supplier quotation
@frappe.whitelist()
def get_supplierquotation():
    # users_data = getcustomer()
    my_data=get_test()
    
    
    filters={}
    if my_data:
        filters={'supplier': my_data}
    quotations = frappe.db.get_all("Supplier Quotation", fields=['*'], filters=filters)
    supplier_item =frappe.db.get_all("Supplier Quotation Item", fields=['*'])
    quotation_docs = []

    for quotation in quotations:
        suppliers=[]
        for supplier in supplier_item:
            if supplier["parent"]==quotation["name"]:
                suppliers.append(supplier)
        quotation["suppliers"] = supplier
        quotation_docs.append(quotation)

    return quotation_docs
# Purchase invoice
@frappe.whitelist()
def get_purchaseinvoice():
    my_data=get_test()
    
    
    filters={}
    if my_data:
        filters={'supplier': my_data}
    quotations = frappe.db.get_all("Purchase Invoice", fields=['*'], filters=filters)
    supplier_item =frappe.db.get_all("Purchase Invoice Item", fields=['*'])
    
    quotation_docs = []

    for quotation in quotations:
        suppliers=[]
        for supplier in supplier_item:
            if supplier["parent"]==quotation["name"]:
                suppliers.append(supplier)
        quotation["suppliers"] = supplier
        quotation_docs.append(quotation)

    return quotation_docs

@frappe.whitelist()
def get_userid():
    return frappe.session.user


# @frappe.whitelist()
# def getcustomer():
#     user_check = get_userid()
#     suppliers = frappe.db.get_all("Supplier", fields=['name'])
#     supplier_portal_details = []
#     suppliers_details = []
#     filters={}
#     for supplier in suppliers:
#         if user_check=="administrator":
#             filters={}
#         else:
#             filters={'parent': supplier['name']}
#         portal_users = frappe.db.get_all("Portal User", filters=filters, fields=['user'])
#         for portal_user in portal_users:
#             if portal_user['user'] == user_check:
#                 supplier_portal_details.append({
#                     'supplier': supplier,
#                     'portal_users': portal_users
#                 })

#     for detail in supplier_portal_details:
#         suppliers_details.append(detail['supplier']['name'])

#     return suppliers_details

@frappe.whitelist()
def get_test():
    user_check=get_userid()
    if user_check!="administrator":
        filters={'user': user_check}
        supplier = frappe.db.get_all("Portal User", filters=filters, fields=['parent'])
    
    return supplier[0].parent if supplier else ''