from ipwhois import IPWhois
import socket
from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
import os
import tldextract
from bs4 import BeautifulSoup
import threading

class WhoIsInfoService:
    def __init__(self, url) -> None:
        load_dotenv()
        if not urlparse(url).scheme:
            url = "http://" + url

        self.url = url
        hostname = urlparse(url).hostname
        self.ip = socket.gethostbyname(hostname)
        extracted = tldextract.extract(url)
        self.domain = f"{extracted.domain}.{extracted.suffix}"

        # Multi-threading for faster response
        threads = []
        threads.append(threading.Thread(target=self._perform_rdap_lookup))
        threads.append(threading.Thread(target=self._perform_subdomain_lookup))
        threads.append(threading.Thread(target=self._perform_asset_domains_lookup))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def _perform_rdap_lookup(self):
        obj = IPWhois(self.ip)
        self._lookup_data = obj.lookup_rdap(depth=1)
    
    def _perform_subdomain_lookup(self):
        api_key = os.getenv("API_KEY")
        url = f"https://subdomains.whoisxmlapi.com/api/v1?apiKey={api_key}&domainName={self.domain}"
        response = requests.get(url)
        self._subdomain_data = response.json()
    
    def _perform_asset_domains_lookup(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        asset_types = {
            'javascripts': ['script'],
            'stylesheets': ['link'],
            'images': ['img'],
            'iframes': ['iframe'],
            'anchors': ['a']
        }

        domains_by_type = {
            'javascripts': set(),
            'stylesheets': set(),
            'images': set(),
            'iframes': set(),
            'anchors': set()
        }

        for asset_type, tags in asset_types.items():
            for tag in soup.find_all(tags):
                if tag.name == 'a':
                    url_attr = 'href'
                elif tag.name in ['img', 'script', 'iframe']:
                    url_attr = 'src'
                elif tag.name == 'link' and tag.attrs.get('rel') == ['stylesheet']:
                    url_attr = 'href'
                else:
                    url_attr = None

                if url_attr and url_attr in tag.attrs:
                    domain = urlparse(tag[url_attr]).netloc
                    if domain:
                        domains_by_type[asset_type].add(domain)

        for asset_type, domains in domains_by_type.items():
            domains_by_type[asset_type] = list(domains)

        self._asset_domains = {
            "asset_domains": domains_by_type
        }

    def get_asn(self):
        return self._lookup_data.get("asn", "Unknown ASN")

    def get_isp(self):
        return self._lookup_data.get("asn_description", "Unknown ISP")
    
    def get_org(self):
        return self._lookup_data.get("network", {}).get("name", "Unknown Organisation")

    def get_location(self):
        return self._lookup_data.get("asn_country_code", "Unknown Location")
    
    def get_subdomain(self):
        records = self._subdomain_data["result"]["records"]
        res = []
        for record in records:
            res.append(record["domain"])

        return res
    
    def get_asset_domains(self):
        return self._asset_domains["asset_domains"]

