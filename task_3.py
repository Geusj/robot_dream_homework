import re

record = "+380996378547, 0996378547, 380996378547, 552656589"
find_phones = re.findall(r"(?:\+38|38|0)\d{9}(?=[, ]|$)", record)
print(f"This customer from Ukraine {find_phones}")
