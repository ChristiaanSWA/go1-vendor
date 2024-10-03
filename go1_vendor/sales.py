import frappe
from frappe.utils import add_days, getdate

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
    user_details = frappe.get_all("Sidebar Settings", filters={'parent': 'Go1 Navbar Settings','enabled':1}, fields=['*'],order_by="idx")
    return user_details

@frappe.whitelist()
def get_navbar_logo():
    check=frappe.get_single('Go1 Navbar Settings')
    navbar=f"{frappe.utils.get_url()}{check.application_logo}"
    return {"app_logo":navbar,"datas":check}


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
    materialreq_value = frappe.db.get_all("Item", fields=["lead_time_days"],)
    lead_times = [item['lead_time_days'] for item in materialreq_value]
    max_lead_time = max(lead_times) if lead_times else 0
    
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
        if mr.get("due_date"):
            due_date = getdate(mr["due_date"])  # Convert to date object
            updated_due_date = add_days(due_date, max_lead_time)  # Add max_lead_time
            mr["due_date"] = updated_due_date  # Update due_date with the new value
        # if mr.get('supplier'):

        
        mr["items"] = items
        mr["taxes"] = taxes
        materialreq_docs.append(mr)
   
    # frappe.log_error("materialreq_docs",materialreq_docs)

        # materilreq_docs.append()
    
        
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



#New Dashboard Charts

from frappe.utils import flt
from collections import defaultdict
from frappe import _

@frappe.whitelist()
def supplier_login():
    user=frappe.session.user
    result=frappe.db.get_all('Portal User',fields=['parent'],filters={"user":user})
    return result[0].parent if result else ''

#Number Card 1
@frappe.whitelist()
def get_purchase_order_grand_total():
    supplier=supplier_login()
    if supplier:
        query = frappe.db.sql("""
            SELECT COALESCE(AVG(grand_total), 0) AS total_grand_total
            FROM `tabPurchase Order`
            WHERE docstatus = 1
            AND MONTH(transaction_date) = MONTH(CURRENT_DATE())
            AND YEAR(transaction_date) = YEAR(CURRENT_DATE()) 
            AND supplier= %s
        """,(supplier),as_dict=True)
        total = query[0].get('total_grand_total', 0) if query else 0
        return {"total_grand_total": total}
    else:
        query = frappe.db.sql("""
            SELECT COALESCE(AVG(grand_total), 0) AS total_grand_total
            FROM `tabPurchase Order`
            WHERE docstatus = 1
            AND MONTH(transaction_date) = MONTH(CURRENT_DATE())
            AND YEAR(transaction_date) = YEAR(CURRENT_DATE()) 
            
        """,as_dict=True)
        total = query[0].get('total_grand_total', 0) if query else 0
        return {"total_grand_total": total}
    
    
    
#Number Card2
@frappe.whitelist()
def get_pending_quotation_count():
    supplier = supplier_login()
    if supplier:
        query = frappe.db.sql("""
                SELECT COUNT(Q.name) AS total_count
                FROM `tabRequest for Quotation` Q
                INNER JOIN `tabRequest for Quotation Supplier` QS ON Q.name = QS.parent
                WHERE Q.custom_actioned = 0  
                AND QS.supplier = %s
                """,(supplier),as_dict=True)
        count = query[0].get('total_count', 0) if query else 0
        return {"total_count": count}

    else:
        query =frappe.db.sql( """
                SELECT COUNT(*) AS total_count
                FROM `tabRequest for Quotation`
                WHERE custom_actioned = 0
                """,as_dict=True)
        count = query[0].get('total_count', 0) if query else 0
        return {"total_count": count}

#Number Card3
@frappe.whitelist()
def get_pending_invoice():
        supplier = supplier_login()
        if supplier:
            query = frappe.db.sql("""
                    SELECT COUNT(*) AS total_count
                    FROM `tabPurchase Invoice`
                    WHERE docstatus = 1  
                    AND status = 'Unpaid'
                    AND supplier = %s
                    """,(supplier),as_dict=True)
            count = query[0].get('total_count', 0) if query else 0
            return {"total_count": count}

        else:
            query = frappe.db.sql("""
                    SELECT COUNT(*) AS total_count
                    FROM `tabPurchase Invoice`
                    WHERE docstatus = 1  
                    AND status = 'Unpaid'
                    """,as_dict=True)
            count = query[0].get('total_count', 0) if query else 0
            return {"total_count": count}

#Number Card4
@frappe.whitelist()
def get_pending_inwards():
    supplier=supplier_login()
    if supplier:
        query = frappe.db.sql("""
            SELECT COUNT(*) AS total_count
            FROM `tabPurchase Order`
            WHERE docstatus = 1  
            AND status IN ('To Receive And Bill', 'To Receive')
            AND supplier =%s
        """,(supplier),as_dict=True)
        count = query[0].get('total_count', 0) if query else 0
        return {"total_count": count}
    else:
        query =frappe.db.sql( """
            SELECT COUNT(*) AS total_count
            FROM `tabPurchase Order`
            WHERE docstatus = 1  
            AND status IN ('To Receive And Bill', 'To Receive')
        """,as_dict=True)
        count = query[0].get('total_count', 0) if query else 0
        return {"total_count": count}
    
#Doughnut Chart1
@frappe.whitelist()
def get_purchase_order_status_analysis():
    supplier= supplier_login()
    if supplier:
        query = frappe.db.sql("""
            SELECT 
                status,
                COUNT(*) AS status_count
            FROM `tabPurchase Order`
            WHERE docstatus < 2 
            AND supplier=%s
            GROUP BY status
        """,(supplier),as_dict=True)
    

        status_data = {
        "Billed Amount": 0,
        "Amount to Bill": 0
         }
        for row in query:
            if row['status'] == 'Completed':
                        status_data["Billed Amount"] += row['status_count']
            elif row['status'] in ['To Receive and Bill', 'To Bill']:
                        status_data["Amount to Bill"] += row['status_count']

        return {"status_data": status_data}
    else:
        query = frappe.db.sql("""
            SELECT 
                status,
                COUNT(*) AS status_count
            FROM `tabPurchase Order`
            WHERE docstatus < 2 
            GROUP BY status
        """,as_dict=True)
        status_data = {
        "Billed Amount": 0,
        "Amount to Bill": 0
         }
        for row in query:
            if row['status'] == 'Completed':
                        status_data["Billed Amount"] += row['status_count']
            elif row['status'] in ['To Receive and Bill', 'To Bill']:
                        status_data["Amount to Bill"] += row['status_count']

        return {"status_data": status_data}


#Doughnut Chart2
@frappe.whitelist()
def get_quotation_status_counts():
    supplier = supplier_login()
    if supplier:
        completed_query = frappe.db.sql("""
            SELECT COUNT(Q.name) AS total_count
            FROM `tabRequest for Quotation` Q
            INNER JOIN `tabRequest for Quotation Supplier` QS ON Q.name = QS.parent
            WHERE Q.custom_actioned = 1
            AND QS.supplier=%s
        """,(supplier),as_dict=True)
        pending_query =frappe.db.sql( """
            SELECT COUNT(Q.name) AS total_count
            FROM `tabRequest for Quotation` Q 
            INNER JOIN `tabRequest for Quotation Supplier` QS ON Q.name = QS.parent
            WHERE custom_actioned = 0
            AND QS.supplier=%s

        """,(supplier),as_dict=True)

    

        completed_count = completed_query[0].get('total_count', 0) if completed_query else 0
        pending_count = pending_query[0].get('total_count', 0) if pending_query else 0

        return {
        "status_data": {
            "Completed": completed_count,
            "Pending": pending_count,
        }
    }
    else:
        completed_query = frappe.db.sql("""
            SELECT COUNT(*) AS total_count
            FROM `tabRequest for Quotation` 
            WHERE custom_actioned = 1
        """,as_dict=True)
        pending_query =frappe.db.sql( """
            SELECT COUNT(*) AS total_count
            FROM `tabRequest for Quotation` 
            WHERE custom_actioned = 0
        """,as_dict=True)

    

        completed_count = completed_query[0].get('total_count', 0) if completed_query else 0
        pending_count = pending_query[0].get('total_count', 0) if pending_query else 0

        return {
        "status_data": {
            "Completed": completed_count,
            "Pending": pending_count,
        }
    }

#Bar Chart
@frappe.whitelist()
def get_top_sold_items():
    supplier = supplier_login()
    if supplier:
        query =frappe.db.sql( """
            SELECT poi.item_code, poi.item_name, COUNT(*) as item_count
            FROM `tabPurchase Order Item` poi
            WHERE parent IN (
                SELECT name
                FROM `tabPurchase Order`
                WHERE docstatus = 1  
                AND supplier =%s
            )
            GROUP BY poi.item_code, poi.item_name
            ORDER BY item_count DESC
            LIMIT 5
        """,(supplier),as_dict=True)
        return {'message': {'items': query}}
    else:
         query =frappe.db.sql( """
            SELECT poi.item_code, poi.item_name, COUNT(*) as item_count
            FROM `tabPurchase Order Item` poi
            WHERE parent IN (
                SELECT name
                FROM `tabPurchase Order`
                WHERE docstatus = 1  
            )
            GROUP BY poi.item_code, poi.item_name
            ORDER BY item_count DESC
            LIMIT 5
        """,as_dict=True)
         return {'message': {'items': query}}
         
#Line Chart
@frappe.whitelist()
def get_monthly_grand_total():
    supplier = supplier_login()
    if supplier:
        grand_total_data = frappe.db.sql(r"""
            SELECT
                DATE_FORMAT(transaction_date, '%%b') as month,
                SUM(grand_total) as monthly_total
            FROM `tabPurchase Order`
            WHERE docstatus = 1
            AND supplier = %s
            GROUP BY DATE_FORMAT(transaction_date, '%%Y-%%m')
            ORDER BY FIELD(DATE_FORMAT(transaction_date, '%%b'), 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar')
        """, (supplier), as_dict=True)

        financial_year_order = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']
        monthly_totals = {month: 0 for month in financial_year_order}

        for record in grand_total_data:
            month = record.get('month')
            total = flt(record.get('monthly_total'))
            if month in monthly_totals:
                monthly_totals[month] += total

        return {
            "labels": list(monthly_totals.keys()),
            "data": list(monthly_totals.values())
        }
    else:
        grand_total_data = frappe.db.sql(f"""
            SELECT
                DATE_FORMAT(transaction_date, '%b') as month,
                SUM(grand_total) as monthly_total
            FROM `tabPurchase Order`
            WHERE docstatus = 1
            GROUP BY DATE_FORMAT(transaction_date, '%Y-%m')
            ORDER BY FIELD(DATE_FORMAT(transaction_date, '%b'), 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar')
        """, as_dict=True)

        financial_year_order = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar']
        monthly_totals = {month: 0 for month in financial_year_order}

        for record in grand_total_data:
            month = record.get('month')
            total = flt(record.get('monthly_total'))
            if month in monthly_totals:
                monthly_totals[month] += total

        return {
            "labels": list(monthly_totals.keys()),
            "data": list(monthly_totals.values())
        }
        
