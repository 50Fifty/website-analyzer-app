import pytest

from validators.url_validator import validate_url

@pytest.fixture(params=[
    "https://www.google.com",
    "http://example.com",
    "https://example.com:8080/path/to/resource?query=param",
    "ftp://files.example.com",
    "http://localhost",
    "http://192.168.1.1"
])
def valid_url(request):
    return request.param

@pytest.fixture(params=[
    "this is not a url",
    "google.com",  # Missing protocol
    "http:://doublecolon.com",  # Malformed protocol
    "https://",  # No domain
    "ftp//missingcolon.com",
    "https:// space.com",  # Space in the URL
    "https://.com",  # No domain name, just TLD
    "https://?query=withoutDomain"
])
def invalid_url(request):
    return request.param

def test_valid_url(valid_url):
    assert validate_url(valid_url) == True, f"Expected {valid_url} to be valid"

def test_invalid_url(invalid_url):
    assert validate_url(invalid_url) == False, f"Expected {invalid_url} to be invalid"
