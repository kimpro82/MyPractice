# Get domain from e-mail address by re.sub()
# 2023.02.12

import re

email = "404@not.found"
domain = re.sub(r"[\w\.-_*]+@", "", email)

print(domain)