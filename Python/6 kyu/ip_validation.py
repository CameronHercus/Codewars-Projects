def is_valid_IP(strng):
    """6 kyu - IP Validation"""
    ip_list = strng.split(".")
    ip_set = {str(i) for i in range(0, 256)}
    if len(ip_list) != 4:
        return False
    for i in ip_list:
        if not i.isnumeric() or i not in ip_set:
            return False            
    return True

print(is_valid_IP('12.255.56.1'))