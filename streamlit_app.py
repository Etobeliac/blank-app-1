import streamlit as st
import os

def read_script_content(script_path):
    try:
        with open(script_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content if content else "# Ce fichier est vide."
    except FileNotFoundError:
        return f"# Le fichier '{script_path}' n'a pas été trouvé."
    except Exception as e:
        return f"# Une erreur s'est produite lors de la lecture du fichier : {str(e)}"

def main():
    st.set_page_config(layout="wide")

    # Obtenir le chemin absolu du répertoire du projet
    project_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(project_dir, 'script')
    
    # Afficher des informations de débogage
    st.sidebar.write("### Informations de débogage")
    st.sidebar.write(f"Répertoire du projet: {project_dir}")
    st.sidebar.write(f"Répertoire des scripts: {script_dir}")
    st.sidebar.write(f"Contenu du répertoire des scripts: {os.listdir(script_dir)}")
    
    # Obtenir la liste des fichiers Python dans le répertoire 'script'
    script_files = [f for f in os.listdir(script_dir) if f.endswith('.py') and f != 'streamlit_app.py']
    
    st.sidebar.write(f"Fichiers Python trouvés: {script_files}")

    # Création de deux colonnes
    col1, col2 = st.columns([1, 3])

    # Colonne de gauche pour la sélection du script
    with col1:
        st.header("Sélectionnez un script")
        if script_files:
            selected_script = st.selectbox("", script_files)
            st.write(f"Script sélectionné: {selected_script}")
        else:
            st.warning("Aucun script Python trouvé dans le répertoire 'script'.")
            return

    # Colonne de droite pour afficher le contenu du script
    with col2:
        st.header("Page d'Accueil des Scripts")
        if selected_script:
            st.subheader(f"Contenu de {selected_script}")
            script_path = os.path.join(script_dir, selected_script)
            st.write(f"Chemin complet du script: {script_path}")
            script_content = read_script_content(script_path)
            st.code(script_content, language='python')

            if st.button("Exécuter le script"):
                st.info("Simulation de l'exécution du script.")

if __name__ == "__main__":
    main()