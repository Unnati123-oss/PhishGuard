
from urllib.parse import urlsplit
import ipaddress


def normalize_url(raw_url: str) -> str:
    url = raw_url.strip()

    if not url:
        raise ValueError("Please enter a URL.")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    return url


def validate_url(raw_url: str) -> str:
    url = normalize_url(raw_url)
    parts = urlsplit(url)

    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise ValueError("Enter a valid HTTP or HTTPS URL.")

    try:
        _ = parts.port
    except ValueError as exc:
        raise ValueError("Invalid port.") from exc

    host = parts.hostname.rstrip(".")

    try:
        ipaddress.ip_address(host)
    except ValueError:
        labels = host.split(".")

        if len(host) > 253 or any(not label for label in labels):
            raise ValueError("Invalid hostname format.")

        for label in labels:
            if (
                len(label) > 63
                or not label[0].isalnum()
                or not label[-1].isalnum()
                or any(not (c.isalnum() or c == "-") for c in label)
            ):
                raise ValueError("Invalid hostname format.")

    return url
