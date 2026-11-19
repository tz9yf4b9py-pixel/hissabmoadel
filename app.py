import streamlit as st

st.set_page_config(page_title="Calculateur de moyenne", page_icon="📚")

st.title("📚 Calculateur de moyenne")

st.write("Entre tes notes pour calculer ta moyenne universitaire.")

matieres = {

    "Comptabilité": 3,

    "Économie 1": 3,

    "Économie 2": 2,

    "Statistiques": 2,

    "Mathématiques": 2,

    "Informatique": 1,

    "Histoire": 1,

    "Droit": 1,

    "Science politique": 1,

    "Anglais": 1

}

notes = {}

for matiere, coef in matieres.items():

    notes[matiere] = st.number_input(

        f"{matiere} (Coefficient {coef})",

        min_value=0.0,

        max_value=20.0,

        value=0.0,

        step=0.25,

        key=matiere

    )

if st.button("Calculer ma moyenne"):

    total = sum(notes[m] * c for m, c in matieres.items())

    moyenne = total / sum(matieres.values())

    st.success(f"Ta moyenne est : {moyenne:.2f}/20")

    if moyenne >= 10:

        st.balloons()

        st.write("🎉 Félicitations ! Tu as la moyenne.")

    else:

        st.write("Continue tes efforts ! 💪")