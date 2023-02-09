"""module for regex"""
import re
def mailCheck(a):
    x = re.findall("[A-Za-z0-9\.]+[@][Ll][Tt][Tt][Ss][\.][a-z]{3}",a)
    if x:
        return True
    else:
        return False