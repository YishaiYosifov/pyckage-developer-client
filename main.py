from common.util import print_formatted, error
from dotenv import load_dotenv

from commands import *

import sysconfig
import requests
import zipfile
import sys
import os
import io

SITEPACKAGES = sysconfig.get_paths()["purelib"]

COMMANDS = {"install": "install a package. Arguments: [package name]", "upload": "upload a package", "delete": "delete a package/release. Arguments: [version : optional]"}
COMMAND_HELP = "\n".join([f"[GREEN]{command}[END] - {description}" for command, description in COMMANDS.items()])

def main():
    errorMessage = None

    try:
        command = sys.argv[1]
        if not command in COMMANDS: errorMessage = f"Unknwon Command: {command}"
    except IndexError: errorMessage = f"Missing Command"

    if errorMessage:
        print_formatted(f"{error(errorMessage)}\n\nCommands:\n{COMMAND_HELP}")
        return

    globals()[command]()
    """loggedIn, token = login()
    if not loggedIn: return

    token = requests.post(f"{BAES_URL}/login", json={"username": os.getenv("PYCKAGE_USERNAME"), "password": os.getenv("PYCKAGE_PASSWORD")}).text
    download = requests.get(f"{BAES_URL}/get_download", json={"access_token": token, "repository": "Merubokkusu/Discord-S.C.U.M", "version": "v0.3.1"}).text

    packageZip = zipfile.ZipFile(io.BytesIO(requests.get(download).content))
    packageZip.extractall(f"{SITEPACKAGES}\\install-temp")
    os.system(f"{sys.executable} {SITEPACKAGES}\\install-temp\\{packageZip.infolist()[0].filename}setup.py install")"""

if __name__ == "__main__":
    os.system("")

    load_dotenv()
    main()