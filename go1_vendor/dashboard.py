import frappe

@frappe.whitelist()
def get_purchase_order_grand_total():
    query = """
        SELECT COALESCE(AVG(grand_total), 0) AS total_grand_total
        FROM `tabPurchase Order`
        WHERE docstatus = 1
          AND MONTH(transaction_date) = MONTH(CURRENT_DATE())
          AND YEAR(transaction_date) = YEAR(CURRENT_DATE()) 
    """
    
    result = frappe.db.sql(query, as_dict=True)
    
    total = result[0].get('total_grand_total', 0) if result else 0
    return {"total_grand_total": total}



# @frappe.whitelist()
# def get_purchase_order_status_analysis():
#     query = """
#         SELECT 
#             status,
#             COUNT(*) AS status_count
#         FROM `tabPurchase Order`
#         WHERE docstatus < 2 
#         GROUP BY status
#     """
#     result = frappe.db.sql(query, as_dict=True)
    
#     status_data = {row['status']: row['status_count'] for row in result}
#     return {"status_data": status_data}

@frappe.whitelist()
def get_purchase_order_status_analysis():
    # Query to get the count of purchase orders based on their statuses
    query = """
        SELECT 
            status,
            COUNT(*) AS status_count
        FROM `tabPurchase Order`
        WHERE docstatus < 2 
        GROUP BY status
    """
    result = frappe.db.sql(query, as_dict=True)
    
    # Calculate the required data
    status_data = {
        "Billed Amount": 0,
        "Amount to Bill": 0
    }

    # Iterate through the result to populate status_data
    for row in result:
        if row['status'] == 'Completed':
            status_data["Billed Amount"] += row['status_count']
        elif row['status'] in ['To Receive and Bill', 'To Bill']:
            status_data["Amount to Bill"] += row['status_count']

    return {"status_data": status_data}



from frappe.utils import flt
from collections import defaultdict

@frappe.whitelist()
def get_monthly_grand_total():
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

from frappe import _

@frappe.whitelist()
def get_status_counts():
    statuses = ["Pending", "Received", "Ordered"]
    status_counts = {status: 0 for status in statuses}


    material_requests = frappe.get_all('Material Request', fields=['status'])

    for request in material_requests:
        if request.status in status_counts:
            status_counts[request.status] += 1

    return {
        "status_data": status_counts
    }



@frappe.whitelist()
def get_purchase_count():
    query = """
        SELECT COUNT(*) AS total_count
        FROM `tabPurchase Order`
        WHERE docstatus = 1  
        AND status = 'To Receive and Bill'
    """
    
    result = frappe.db.sql(query, as_dict=True)
    
    count = result[0].get('total_count', 0) if result else 0
    return {"total_count": count}

@frappe.whitelist()
def get_pending_invoice():
    query = """
        SELECT COUNT(*) AS total_count
        FROM `tabPurchase Invoice`
        WHERE docstatus = 1  
        AND status = 'Unpaid'
    """
    
    result = frappe.db.sql(query, as_dict=True)
    
    count = result[0].get('total_count', 0) if result else 0
    return {"total_count": count}

@frappe.whitelist()
def get_pending_inwards():
    query = """
        SELECT COUNT(*) AS total_count
        FROM `tabPurchase Order`
        WHERE docstatus = 1  
        AND status IN ('To Receive And Bill', 'To Receive')
    """
    
    result = frappe.db.sql(query, as_dict=True)
    
    count = result[0].get('total_count', 0) if result else 0
    return {"total_count": count}


@frappe.whitelist()
def get_top_sold_items():
    query = """
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
    """
    items = frappe.db.sql(query, as_dict=True)
    return {'message': {'items': items}}


@frappe.whitelist()
def get_pending_quotation_count():
    query = """
        SELECT COUNT(*) AS total_count
        FROM `tabRequest for Quotation`
        WHERE custom_actioned = 0  
    """
    
    result = frappe.db.sql(query, as_dict=True)
    
    count = result[0].get('total_count', 0) if result else 0
    return {"total_count": count}
