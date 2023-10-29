from urllib.parse import urlparse

import re

def validate_url(url):
    # Regular expression to validate a URL
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain name
        r'localhost|'  # Localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP Address
        r'(?::\d+)?'  # Optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(pattern, url) is not None
