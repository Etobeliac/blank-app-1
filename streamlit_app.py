import streamlit as st
import os

def read_script_content(script_name):
    try:
        with open(script_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "# Le fichier n'a pas été trouvé."
    except Exception as e:
        return f"# Une erreur s'est produite lors de la lecture du fichier : {str(e)}"

def main():
    st.set_page_config(layout="wide")

    # Création de deux colonnes
    col1, col2 = st.columns([1, 3])

    # Obtenir la liste des fichiers Python dans le répertoire courant
    script_files = [f for f in os.listdir('.') if f.endswith('.py')]

    # Colonne de gauche pour la sélection du script
    with col1:
        st.header("Sélectionnez un script")
        selected_script = st.selectbox("", script_files)

    # Colonne de droite pour afficher le contenu du script
    with col2:
        st.header("Page d'Accueil des Scripts")
        st.subheader(f"Contenu de {selected_script}")
        script_content = read_script_content(selected_script)
        st.code(script_content, language='python')

        # Bouton pour exécuter le script (simulation)
        if st.button("Exécuter le script"):
            st.info("Simulation de l'exécution du script. Dans une vraie application, le script serait exécuté ici.")

if __name__ == "__main__":
    main()