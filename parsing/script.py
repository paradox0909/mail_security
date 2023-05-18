import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = [] 

with open('/var/log/apache2/access.log', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            if match not in emails:  
                emails.append(match)  
                print(match)

