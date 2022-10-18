from pydantic import BaseModel

class Package(BaseModel):
    name : str
    version : str = "v0.1.0"

    description : str = "No Description Given"
    description_file : str = "README.md"

    author_email : str = None

    requirements : list = []
    repository : str
    license : str

    classifiers : list
    entry_points : dict = {}