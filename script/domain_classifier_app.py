import pandas as pd
import streamlit as st
import io

# Définition des thématiques et mots-clés
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

def classify_domain(domain, categories):
    domain_lower = domain.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in domain_lower:
                return category
    return 'NON UTILISÉ'

def main():
    st.title("Classification avancée de noms de domaine")

    uploaded_file = st.file_uploader("Déposez votre fichier Excel contenant les domaines", type=["xlsx"])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        
        if 'Domain' not in df.columns:
            st.error("Le fichier doit contenir une colonne 'Domain'")
            return

        # Classification des domaines
        df['Category'] = df['Domain'].apply(lambda x: classify_domain(x, thematique_dict))

        # Séparation des domaines utilisés et non utilisés
        df_used = df[df['Category'] != 'NON UTILISÉ']
        df_not_used = df[df['Category'] == 'NON UTILISÉ']

        # Création du DataFrame final
        df_final = df_used.copy()
        df_final['Non Utilisé'] = pd.NA
        df_final = pd.concat([df_final, pd.DataFrame({'Domain': pd.NA, 'Category': pd.NA, 'Non Utilisé': df_not_used['Domain']})], ignore_index=True)

        st.subheader("Aperçu des résultats")
        st.write(df_final)

        # Statistiques
        st.subheader("Statistiques")
        total_domains = len(df)
        used_domains = len(df_used)
        not_used_domains = len(df_not_used)
        st.write(f"Total des domaines : {total_domains}")
        st.write(f"Domaines classifiés : {used_domains}")
        st.write(f"Domaines non utilisés : {not_used_domains}")

        # Téléchargement des résultats
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_final.to_excel(writer, sheet_name='Domaines classifiés', index=False)

        output.seek(0)
        
        st.download_button(
            label="Télécharger les résultats (Excel)",
            data=output,
            file_name="domaines_classes_mises_a_jour.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()