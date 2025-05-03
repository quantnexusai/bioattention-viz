import spacy

def detect_entities(text):
    nlp = spacy.load("en_core_sci_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities