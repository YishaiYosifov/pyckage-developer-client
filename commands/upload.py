from pydantic.error_wrappers import ValidationError
from common.util import *

import requests
import json

def upload():
    loggedIn, token = login()
    if not loggedIn: return

    try: attributes = load_manifest_package().dict()
    except (FileNotFoundError, ValidationError) as e:
        if isinstance(e, FileNotFoundError): print_formatted(error("manifest.json Not Found"))
        elif isinstance(e, ValidationError): print_formatted(error(f"Invalid manifest.json Data:\n{str(e)}"))
        return
    attributes["access_token"] = token

    print_formatted(info("Uploading..."))
    response = requests.post(f"{BAES_URL}/upload_package", json=attributes)

    if response.status_code != 200: print_formatted(error(response.text))
    else: print_formatted(success("Package Uploaded Successfully"))