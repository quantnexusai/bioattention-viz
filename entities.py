import spacy
import warnings

def detect_entities(text):
    """Detect biomedical entities in the given text."""
    try:
        # Try to load the model directly
        try:
            nlp = spacy.load("en_core_sci_sm")
        except OSError:
            # If model not found, try to import init_model which will install it
            try:
                import init_model
                nlp = spacy.load("en_core_sci_sm")
            except (ImportError, OSError) as e:
                warnings.warn(f"Could not load scispacy model: {e}")
                # Fallback to a regular spaCy model if available
                try:
                    nlp = spacy.load("en_core_web_sm")
                except OSError:
                    # Last resort: use a blank model
                    nlp = spacy.blank("en")
                    warnings.warn("Using blank spaCy model as fallback")
        
        # Process the text
        doc = nlp(text)
        
        # Get entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    except Exception as e:
        warnings.warn(f"Error detecting entities: {e}")
        return []