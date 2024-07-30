import streamlit as st
import pandas as pd

def classify_domain(domain, categories):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in domain.lower():
                return category
    return 'NON UTILISÉ'

st.title("Classification de Domaines")

# Dictionnaire des thématiques
thematique_dict = {
    'ANIMAUX': ['animal', 'pet', 'zoo', 'farm', 'deer', 'chiens', 'chats', 'animaux'],
    'CUISINE': ['cook', 'recipe', 'cuisine', 'food', 'bon plan', 'equipement', 'minceur', 'produit', 'restaurant'],
    'ENTREPRISE': ['business', 'enterprise', 'company', 'corporate', 'formation', 'juridique', 'management', 'marketing', 'services'],
    'FINANCE / IMMOBILIER': ['finance', 'realestate', 'investment', 'property', 'assurance', 'banque', 'credits', 'immobilier'],
    'INFORMATIQUE': ['tech', 'computer', 'software', 'IT', 'high tech', 'internet', 'jeux-video', 'marketing', 'materiel', 'smartphones'],
    'MAISON': ['home', 'house', 'garden', 'interior', 'deco', 'demenagement', 'equipement', 'immo', 'jardin', 'maison', 'piscine', 'travaux'],
    'MODE / FEMME': ['fashion', 'beauty', 'cosmetics', 'woman', 'beaute', 'bien-etre', 'lifestyle', 'mode', 'shopping'],
    'SANTE': ['health', 'fitness', 'wellness', 'medical', 'hospital', 'grossesse', 'maladie', 'minceur', 'professionnels', 'sante', 'seniors'],
    'SPORT': ['sport', 'fitness', 'football', 'soccer', 'basketball', 'tennis', 'autre sport', 'basket', 'combat', 'foot', 'musculation', 'velo'],
    'TOURISME': ['travel', 'tourism', 'holiday', 'vacation', 'bon plan', 'camping', 'croisiere', 'location', 'tourisme', 'vacance', 'voyage'],
    'VEHICULE': ['vehicle', 'car', 'auto', 'bike', 'bicycle', 'moto', 'produits', 'securite', 'voiture']
}

# Zone de texte pour coller les noms de domaine
domain_input = st.text_area("Collez vos noms de domaine ici (un par ligne)", height=200)

if domain_input and st.button("Classifier les domaines"):
    domains = [domain.strip() for domain in domain_input.split('\n') if domain.strip()]
    
    # Classification des domaines
    classified_domains = [(domain, classify_domain(domain, thematique_dict)) for domain in domains]

    # Création du DataFrame
    df = pd.DataFrame(classified_domains, columns=['Domain', 'Category'])

    # Séparation des domaines utilisés et non utilisés
    df_used = df[df['Category'] != 'NON UTILISÉ']
    df_not_used = df[df['Category'] == 'NON UTILISÉ']

    # Ajout des domaines non utilisés dans une nouvelle colonne
    df_final = df_used.copy()
    df_final['Non Utilisé'] = pd.NA
    df_final = pd.concat([df_final, pd.DataFrame({'Domain': pd.NA, 'Category': pd.NA, 'Non Utilisé': df_not_used['Domain']})], ignore_index=True)

    st.write("Résultats de la classification :")
    st.dataframe(df_final)