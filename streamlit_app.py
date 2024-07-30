import streamlit as st
import os

def read_script_content(script_path):
    try:
        with open(script_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Erreur lors de la lecture du fichier : {str(e)}"

def main():
    st.set_page_config(layout="wide", page_title="Gestionnaire de Scripts")

    project_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(project_dir, 'script')
    script_files = [f for f in os.listdir(script_dir) if f.endswith('.py')]

    st.title("Gestionnaire de Scripts Python")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.header("Liste des scripts")
        selected_script = st.selectbox("Choisissez un script :", script_files)

    with col2:
        if selected_script:
            st.header(f"Contenu de {selected_script}")
            script_path = os.path.join(script_dir, selected_script)
            script_content = read_script_content(script_path)
            st.code(script_content, language='python')

            if st.button("Exécuter le script"):
                st.info("Simulation de l'exécution du script.")
                # Ici, vous pouvez ajouter la logique pour exécuter réellement le script si nécessaire

if __name__ == "__main__":
    main()