import spacy
from spacy.tokens import Doc
import en_core_sci_sm

def get_entities(text, use_scispacy=True):
    try:
        if use_scispacy:
            nlp = en_core_sci_sm.load()
            doc = nlp(text)
            return [(ent.text, ent.label_) for ent in doc.ents]
    except Exception:
        print("scispacy model failed, falling back to basic tokenization.")
    
    # Fallback: Basic tokenization
    doc = Doc(spacy.blank("en"), words=text.split())
    return [(token.text, "TOKEN") for token in doc]

if __name__ == "__main__":
    text = "TP53 mutations are associated with breast cancer."
    entities = get_entities(text)
    print(entities)