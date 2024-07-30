import streamlit as st

def main():
    st.title("Classification de noms de domaine")

    uploaded_file = st.file_uploader("Déposez votre fichier Excel ici", type=["xlsx"])

    if st.button("Classifier les domaines"):
        if uploaded_file is not None:
            st.success("Fichier téléchargé avec succès. La classification commencerait ici.")
        else:
            st.warning("Veuillez d'abord télécharger un fichier Excel.")

    st.info("Ceci est une application de démonstration Streamlit.")

if __name__ == "__main__":
    main()