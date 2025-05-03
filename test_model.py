from model import BioBERTAttention

def main():
    bio_model = BioBERTAttention()
    sample_text = "TP53 mutations are associated with breast cancer."
    tokens, attentions = bio_model.get_attention_weights(sample_text, layer=0, head=0)
    print("Tokens:", tokens)
    print("Attention Shape:", attentions.shape)

if __name__ == "__main__":
    main()