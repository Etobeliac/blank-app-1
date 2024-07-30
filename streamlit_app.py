import streamlit as st

# Dictionnaire contenant les scripts disponibles et leur contenu
scripts = {
    "domain_classifier_app.py": """
import streamlit as st

def main():
    st.title("Classification de noms de domaine")

    st.file_uploader("Déposez votre fichier Excel ici", type=["xlsx"])

    st.button("Classifier les domaines")

    st.success("Ceci est un message de succès")

if __name__ == "__main__":
    main()
    """,
    "autre_script.py": "# Contenu de l'autre script ici",
    "encore_un_script.py": "# Contenu du troisième script ici"
}

def main():
    st.set_page_config(layout="wide")

    # Création de deux colonnes
    col1, col2 = st.columns([1, 3])

    # Colonne de gauche pour la sélection du script
    with col1:
        st.header("Sélectionnez un script")
        selected_script = st.selectbox("", list(scripts.keys()))

    # Colonne de droite pour afficher le contenu du script
    with col2:
        st.header("Page d'Accueil des Scripts")
        st.subheader(f"Contenu de {selected_script}")
        st.code(scripts[selected_script], language='python')

        # Bouton pour exécuter le script (simulation)
        if st.button("Exécuter le script"):
            st.info("Simulation de l'exécution du script. Dans une vraie application, le script serait exécuté ici.")

if __name__ == "__main__":
    main()