<!-- @frappe.whitelist(allow_guest = True)
def login(usr,pwd):
    try:
        frappe.local.login_manager.authenticate(usr, pwd)
        frappe.local.login_manager.post_login()
        login_response = {
            'message': frappe.local.response['message']
        }
        token = get_auth_token(usr)
        if token:
            has_role = frappe.db.get_all('Has Role',filters={'parent': usr, 'role': "Vendor"}) if frappe.db.get_all('Has Role',filters={'parent': usr, 'role': "Vendor"}) else frappe.db.get_all('Has Role',filters={'parent': usr, 'role': "Waiter"})
            if not has_role:
                # frappe.local.response.http_status_code = 500
                frappe.local.response.status = "Failed"
                frappe.local.response.message = "You dont have access."
                return
            login_response['api_key'] = token['api_key']
            login_response['api_secret'] = token['api_secret']
            login_response['status'] = "success"
        return login_response
    except frappe.exceptions.AuthenticationError:
        authentication_exception()
    except Exception:
        other_exception("Error in customer login")
 
        
        
        def get_auth_token(user):
        api_key = frappe.db.get_value("User", user, "api_key")
        if api_key:
            api_secret = frappe.utils.password.get_decrypted_password("User", user, fieldname='api_secret')
            return  {"api_secret": api_secret, "api_key": api_key}
 -->
