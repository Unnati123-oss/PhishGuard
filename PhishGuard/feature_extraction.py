
from urllib.parse import urlsplit
import ipaddress
import pandas as pd

FEATURE_COLUMNS = [
    "url_length",
    "hostname_length",
    "path_length",
    "query_length",
    "dot_count",
    "hyphen_count",
    "at_count",
    "digit_count",
    "subdomain_count",
    "uses_https",
    "uses_ip_address",
]


def extract_features(url: str) -> dict:
    parts = urlsplit(url)
    host = (parts.hostname or "").lower().rstrip(".")

    try:
        ipaddress.ip_address(host)
        uses_ip = 1
    except ValueError:
        uses_ip = 0

    labels = host.split(".") if host else []

    return {
        "url_length": len(url),
        "hostname_length": len(host),
        "path_length": len(parts.path),
        "query_length": len(parts.query),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "at_count": url.count("@"),
        "digit_count": sum(c.isdigit() for c in url),
        "subdomain_count": max(0, len(labels) - 2),
        "uses_https": int(parts.scheme == "https"),
        "uses_ip_address": uses_ip,
    }


def features_to_frame(features: dict) -> pd.DataFrame:
    return pd.DataFrame(
        [[features[column] for column in FEATURE_COLUMNS]],
        columns=FEATURE_COLUMNS,
    )
