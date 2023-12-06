import json
from model import Base, Docs, ShowStudent, BaseStudent


def AddDocuments( doc10, doc7, doc5, doc3, doc1, superdoc):
    base = ShowStudent('creds.json')
    document = Docs(doc10, doc7, doc5, doc3, doc1, superdoc)
    base["documents"].append(document.data)
    BaseStudent( base, 'creds.json')

