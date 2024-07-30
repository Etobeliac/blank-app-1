import streamlit as st
import os
import pandas as pd

def read_script_content(script_path):
    try:
        with open(script_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Erreur lors de la lecture du fichier : {str(e)}"

def main():
    st.set_page_config(layout="wide", page_title="Classification de Domaines")

    project_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(project_dir, 'script')
    script_files = [f for f in os.listdir(script_dir) if f.endswith('.py')]

    st.title("Classification de Domaines")

    # Zone de drag and drop pour le fichier Excel
    uploaded_file = st.file_uploader("Glissez et déposez votre fichier Excel ici", type=['xlsx', 'xls'])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Aperçu des données :")
        st.dataframe(df.head())

        # Sélection de la colonne contenant les domaines
        domain_column = st.selectbox("Sélectionnez la colonne contenant les domaines :", df.columns)

        if st.button("Classifier les domaines"):
            # Ici, vous pouvez ajouter la logique de classification
            st.success("Classification terminée !")

            # Simulation de résultats
            used_domains = len(df) // 2
            not_used_domains = len(df) - used_domains

            st.write(f"Domaines classifiés : {used_domains}")
            st.write(f"Domaines non utilisés : {not_used_domains}")

            # Bouton de téléchargement (simulation)
            output = df.to_excel(index=False)
            st.download_button(
                label="Télécharger les résultats (Excel)",
                data=output,
                file_name="domaines_classes_mises_a_jour.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # Affichage du contenu du script (optionnel, vous pouvez le garder ou le supprimer)
    st.sidebar.title("Contenu du Script")
    selected_script = st.sidebar.selectbox("Sélectionnez un script :", script_files)
    if selected_script:
        script_path = os.path.join(script_dir, selected_script)
        script_content = read_script_content(script_path)
        st.sidebar.code(script_content, language='python')

if __name__ == "__main__":
    main()