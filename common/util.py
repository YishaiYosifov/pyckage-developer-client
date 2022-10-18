from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError
from requests.models import Response
from common.package import Package
from datetime import datetime
from typing import Any

import requests
import json
import os

BAES_URL = "http://192.168.1.159:5000"

class Colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    PURPLE = "\033[95m"

    WARNING = "\033[93m"
    ERROR = "\033[91m"
    INFO = "\033[96m"

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    END = "\033[0m"
FORMAT_COLORS = {color:value for color, value in Colors.__dict__.items() if not color.startswith("__")}

def print_formatted(text : str, end : str | None = "\n") -> str:
    text = f"[INFO]{datetime.now().strftime('%H:%M:%S')}[END] [WARNING]-[END] " + text
    for color, value in FORMAT_COLORS.items(): text = text.replace(f"[{color}]", value)
    print(text, end=end)

    return text

def info(text) -> str: return f"[INFO]INFO:[END] [BOLD]{text}[END]"
def error(text) -> str: return f"[ERROR]ERROR:[END] [BOLD]{text}[END]"
def success(text) -> str: return f"[GREEN]SUCCESS:[END] [BOLD]{text}[END]"

def login() -> tuple[bool, str]:
    try: token = requests.post(f"{BAES_URL}/login", json={"username": os.getenv("PYCKAGE_USERNAME"), "password": os.getenv("PYCKAGE_PASSWORD")}).text
    except (ConnectionError, MaxRetryError):
        print_formatted(error("could not login, connection error"))
        return (False, None)
    
    print_formatted(info("Logged In"))
    return (True, token)

def load_manifest_package() -> Package:
    with open("manifest.json", "r") as f: manifest = json.load(f)
    return Package.parse_obj(manifest)

def post(target : str, **data : Any) -> Response: return requests.post(f"{BAES_URL}/{target}", json=data)
def get(target : str, **data : Any) -> Response: return requests.get(f"{BAES_URL}/{target}", json=data)