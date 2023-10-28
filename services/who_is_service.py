from ipwhois import IPWhois
import threading
import socket
from urllib.parse import urlparse

class WhoIsService:
    def __init__(self, url) -> None:
        self.threads = []
        self.result = dict()

        hostname = urlparse(url).hostname
        self.ip = socket.gethostbyname(hostname)
        self._lookup_data = self._perform_rdap_lookup()

    def _perform_rdap_lookup(self):
        obj = IPWhois(self.ip)
        return obj.lookup_rdap(depth=1)

    def _get_asn_from_ip(self):
        self.result["asn"] = self._lookup_data.get("asn", "Unknown ASN")

    def _get_isp_from_ip(self):
        self.result["isp"] = self._lookup_data.get("asn_description", "Unknown ISP")
    
    def _get_org_from_ip(self):
        self.result["org"] = self._lookup_data.get("network", {}).get("name", "Unknown Organisation")

    def resolve_all(self):
        for func in dir(self):
            if func.startswith("_get"):
                # call methods normally
                getattr(self, func)()

        return self.result
        