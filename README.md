# phonebook
Simple phone book with users from Active Directory
It should be installed on some of your Linux web server

Prerequisutes to run phbook.py:
- Python v3
- Python library ldap3

## Ubuntu installation
# 1. Python installation v3
$sudo apt-get install python3

# 2. pip3 installation
$sudo apt-get install python3-pip

# 3. Edit in phbook.py only LDAP information section according to your LDAP/AD configuration
worked example provided in current branch

# 4. Run under with python3 phbook.py
$python3 phbook.py
