import streamlit as st

st.set_page_config(

    page_title="Calculateur de moyenne",

    page_icon="📚",

    layout="centered"

)

st.title("📚 Calculateur de moyenne")

st.write("Personnalise tes coefficients et tes notes.")

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

total_points = 0

total_coef = 0

st.subheader("Tes matières")

for i, (matiere, coef_initial) in enumerate(matieres.items()):

    with st.expander(matiere, expanded=True):

        coef = st.number_input(

            "Coefficient",

            min_value=0.0,

            value=float(coef_initial),

            step=1.0,

            key=f"coef_{i}"

        )

        avec_td = st.checkbox(

            "Activer la note de TD (40 %)",

            value=False,

            key=f"td_{i}"

        )

        examen = st.number_input(

            "Note d'examen /20",

            min_value=0.0,

            max_value=20.0,

            step=0.25,

            key=f"exam_{i}"

        )

        if avec_td:

            td = st.number_input(

                "Note de TD /20",

                min_value=0.0,

                max_value=20.0,

                step=0.25,

                key=f"note_td_{i}"

            )

            note_finale = td * 0.4 + examen * 0.6

        else:

            note_finale = examen

        st.caption(f"Note finale : {note_finale:.2f}/20")

        total_points += note_finale * coef

        total_coef += coef

st.divider()

if st.button("🧮 Calculer ma moyenne", use_container_width=True):

    if total_coef > 0:

        moyenne = total_points / total_coef

        st.metric("Ta moyenne générale", f"{moyenne:.2f}/20")

        if moyenne >= 10:

            st.success("🎉 Tu as la moyenne !")

            st.balloons()

        else:

            st.warning("Il te reste des efforts à faire 💪")

    else:

        st.error("Le total des coefficients doit être supérieur à zéro.")