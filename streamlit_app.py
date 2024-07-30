import streamlit as st
import os

def read_script_content(script_name):
    try:
        with open(script_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content if content else "# Ce fichier est vide."
    except FileNotFoundError:
        return "# Le fichier n'a pas été trouvé."
    except Exception as e:
        return f"# Une erreur s'est produite lors de la lecture du fichier : {str(e)}"

def main():
    st.set_page_config(layout="wide")

    col1, col2 = st.columns([1, 3])

    current_script = os.path.basename(__file__)
    script_files = [f for f in os.listdir('.') if f.endswith('.py') and f != current_script]

    with col1:
        st.header("Sélectionnez un script")
        if script_files:
            selected_script = st.selectbox("", script_files)
        else:
            st.warning("Aucun script Python trouvé dans le répertoire.")
            return

    with col2:
        st.header("Page d'Accueil des Scripts")
        st.subheader(f"Contenu de {selected_script}")
        script_content = read_script_content(selected_script)
        st.code(script_content, language='python')

        if st.button("Exécuter le script"):
            st.info("Simulation de l'exécution du script. Dans une vraie application, le script serait exécuté ici.")
            # Implémentez ici la logique d'exécution sécurisée si nécessaire

if __name__ == "__main__":
    main()