import gzip
import json
import os

from typing import Optional

here = os.path.dirname(os.path.abspath(__file__))

with gzip.open(os.path.join(here, "abbrv.json.gz")) as infile:
    annotations = json.load(infile)

class MedicalAbbreviation:
    def __init__(self, abbreviation: str, meaning: str):
        self.abbreviation = abbreviation
        self.meaning = meaning

    def __str__(self):
        return self.abbreviation
    
    def __repr__(self):
        return "<MedicalAbbreviation: %s>" % (self)

    def __hash__(self):
        return hash(self.abbreviation)
    

def exists(s: str) -> bool:
    if not s:
        return False
    return bool(annotations.get(s, False))

def get_version() -> str:
    return annotations.get("_version")

def find(s: str) -> Optional[MedicalAbbreviation]:
    if not s:
        return
    meaning = annotations.get(s)
    if meaning is None:
        return
    return MedicalAbbreviation(s, meaning)