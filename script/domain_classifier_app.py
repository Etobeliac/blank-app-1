import streamlit as st
import pandas as pd
import io
import os

def main():
    st.set_page_config(layout="wide", page_title="Classification de Domaines")

    project_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(project_dir, 'script')
    script_files = [f for f in os.listdir(script_dir) if f.endswith('.py')]

    st.title("Classification de Domaines")

    # Zone de texte pour coller les noms de domaine
    domain_input = st.text_area("Collez vos noms de domaine ici (un par ligne)", height=200)

    if domain_input:
        # Conversion du texte en DataFrame
        domains = [domain.strip() for domain in domain_input.split('\n') if domain.strip()]
        df = pd.DataFrame({'Domaine': domains})

        st.write("Aperçu des données :")
        st.dataframe(df.head())

        if st.button("Classifier les domaines"):
            # Ici, vous pouvez ajouter la logique de classification
            st.success("Classification terminée !")

            # Simulation de résultats
            used_domains = len(df) // 2
            not_used_domains = len(df) - used_domains

            st.write(f"Domaines classifiés : {used_domains}")
            st.write(f"Domaines non utilisés : {not_used_domains}")

            # Préparation du fichier Excel pour le téléchargement
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Domaines classifiés', index=False)
            output.seek(0)

            # Bouton de téléchargement
            st.download_button(
                label="Télécharger les résultats (Excel)",
                data=output,
                file_name="domaines_classes_mises_a_jour.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # Sélection du script dans la barre latérale (sans afficher le contenu)
    st.sidebar.title("Contenu du Script")
    st.sidebar.selectbox("Sélectionnez un script :", script_files)

if __name__ == "__main__":
    main()