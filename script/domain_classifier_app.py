import streamlit as st
import pandas as pd
import io
import os

def read_excel(file):
    return pd.read_excel(file)

def classify_domain(domain, categories):
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in domain.lower():
                return category
    return 'NON UTILISÉ'

def main():
    st.set_page_config(layout="wide", page_title="Classification de Domaines")

    st.title("Classification de Domaines")

    # Chargement du fichier de thématiques
    template_file = st.file_uploader("Téléchargez le fichier TEMPLATE THEMATIQUES.xlsx", type="xlsx")
    if template_file is not None:
        df_template = read_excel(template_file)

        # Extraction des thématiques et des menus
        thematique_dict = {}
        current_thematique = None

        for index, row in df_template.iterrows():
            if pd.notna(row['THEMATIQUE FR']):
                current_thematique = row['THEMATIQUE FR']
                thematique_dict[current_thematique] = []
            if pd.notna(row['MENU FR']) and current_thematique:
                thematique_dict[current_thematique].append(row['MENU FR'])

        # Ajout des sous-catégories comme mots-clés
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

            st.write("Aperçu des résultats :")
            st.dataframe(df_final)

            # Préparation du fichier Excel pour le téléchargement
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_final.to_excel(writer, sheet_name='Domaines classifiés', index=False)
            output.seek(0)

            # Bouton de téléchargement
            st.download_button(
                label="Télécharger les résultats (Excel)",
                data=output,
                file_name="domaines_classes_mises_a_jour.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()