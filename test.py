
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_asset_domains(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Define tags associated with each asset type
    asset_types = {
        'javascripts': ['script'],
        'stylesheets': ['link'],
        'images': ['img'],
        'iframes': ['iframe'],
        'anchors': ['a']
    }

    # Storage for domains per asset type
    domains_by_type = {
        'javascripts': set(),
        'stylesheets': set(),
        'images': set(),
        'iframes': set(),
        'anchors': set()
    }

    for asset_type, tags in asset_types.items():
        for tag in soup.find_all(tags):
            # Determine the appropriate attribute for the tag
            if tag.name == 'a':
                url_attr = 'href'
            elif tag.name in ['img', 'script', 'iframe']:
                url_attr = 'src'
            elif tag.name == 'link' and tag.attrs.get('rel') == ['stylesheet']:  # Ensure it's a CSS stylesheet
                url_attr = 'href'
            else:
                url_attr = None

            if url_attr and url_attr in tag.attrs:
                domain = urlparse(tag[url_attr]).netloc
                if domain:
                    domains_by_type[asset_type].add(domain)

    # Convert sets to lists for final output
    for asset_type, domains in domains_by_type.items():
        domains_by_type[asset_type] = list(domains)

    return {
        "asset_domains": domains_by_type
    }


if __name__ == '__main__':
    url = 'https://www.pentesteracademy.com'
    print(get_asset_domains(url))