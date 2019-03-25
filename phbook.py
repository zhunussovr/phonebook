#
# This is the simplest script to retrieve user information from
# LDAP or AD server and save it into JSON file
#
import sys, json
from ldap3 import Server, Connection, AUTO_BIND_NO_TLS, SUBTREE

## LDAP server information, please add info in single quotes
ldap_server = 'XX.XX.XX.XX' # Insert name or IP adress of your LDAP/AD server
ldap_port = 389	#port for ldap server
ldap_user = 'domain\\user' #ldap user domain\\user
ldap_passwd = 'user_password' # password for ldap user
ldap_baseDN = 'OU=Users,DC=domain,DC=local' # Base DN where you're going to search users

# Function to retrieve users information from LDAP/AD server
def get_ldap_info():
    with Connection(Server(ldap_server, port=ldap_port, use_ssl=False),
                    auto_bind=AUTO_BIND_NO_TLS,
                    user=ldap_user, password=ldap_passwd) as c:
        c.search(search_base=ldap_baseDN,
                 search_filter='(&(objectClass=user))',
                 search_scope=SUBTREE,
                 attributes=['name', 'telephoneNumber', 'mobile', 'mail', 'title', 'department' ],
                 get_operational_attributes=True)       
    with open('contactlist.json','w',encoding='utf-8') as outfile:
        output = []
        for i in range(len(c.response)):
            mobile = str(c.response[i]['attributes']['mobile'])
            phone = str(c.response[i]['attributes']['telephoneNumber'])
            email = str(c.response[i]['attributes']['mail'])
            title = str(c.response[i]['attributes']['title'])
            department = str(c.response[i]['attributes']['department'])
            if mobile == "[]" : mobile = "No data"
            if phone == "[]" : phone = "No data"
            if title == "[]" : title = "No data"
            if email == "[]" : email = "No data"
            if department == "[]" : department = "No data"
            data = {
                "uname" : str(c.response[i]['attributes']['name']),
                "umobile" : mobile,
                "uphone" : phone,
                "uemail" : email,
                "utitle" : title,
                "udepartment" : department
            }
            output.append(data)
        json.dump(output, outfile,  ensure_ascii=False, indent=4)

get_ldap_info()