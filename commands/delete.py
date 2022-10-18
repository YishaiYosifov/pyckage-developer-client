from pydantic.error_wrappers import ValidationError
from common.util import *

import sys

def delete():
    loggedIn, token = login()
    if not loggedIn: return

    try: package = load_manifest_package()
    except (FileNotFoundError, ValidationError) as e:
        if isinstance(e, FileNotFoundError): print_formatted(error("manifest.json Not Found"))
        elif isinstance(e, ValidationError): print_formatted(error(f"Invalid manifest.json Data:\n{str(e)}"))
        return

    version = sys.argv[2] if len(sys.argv) > 2 else None

    print_formatted("[BOLD][ERROR]ARE YOU SURE YOU WANT TO DELETE THIS PACKAGE?[END] " \
                    "[WARNING]" +
                    (f"This will delete the release with version \"{version}\". " if version else "This will not only remove the latest release, but the entire package. ") +
                    "[END]" \
                    "(y/n): ", end="")
    if input() != "y":
        print_formatted(info("Cancelled."))
        return

    if not version: response = post("delete_package", access_token=token, name=package.name)
    else: response = post("delete_package_version", access_token=token, name=package.name, version=version)

    if response.status_code != 200: print_formatted(error(response.text))
    else: print_formatted(success("Package Deleted Successfully"))