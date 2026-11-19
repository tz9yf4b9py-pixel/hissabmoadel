import streamlit as st

st.set_page_config(

    page_title="Ma moyenne",

    page_icon="📚",

    layout="centered"

)

# DESIGN VIOLET ET BLANC

st.markdown("""

<style>

.stApp {

    background: #f8f6ff;

}

h1, h2, h3 {

    color: #6336b8 !important;

}

div[data-testid="stMetric"] {

    background: white;

    border: 2px solid #e6dcff;

    padding: 18px;

    border-radius: 16px;

}

div[data-testid="stMetricValue"] {

    color: #713bd1;

    font-weight: 800;

}

div[data-testid="stVerticalBlockBorderWrapper"] {

    background: white;

    border: 1px solid #e5d9ff;

    border-radius: 16px;

    padding: 12px;

}

.stButton button {

    background: #713bd1;

    color: white;

    border-radius: 12px;

}

</style>

""", unsafe_allow_html=True)

# TITRE

st.title("📚 Mon calculateur")

st.caption("Suis ta moyenne en temps réel 💜")

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

# Zone de moyenne affichée en haut

zone_moyenne = st.empty()

total_points = 0

total_coef = 0

st.subheader("📝 Mes matières")

for i, (matiere, coef_initial) in enumerate(matieres.items()):

    with st.container(border=True):

        st.markdown(f"### {matiere}")

        col1, col2 = st.columns(2)

        with col1:

            coef = st.number_input(

                "Coefficient",

                min_value=0.0,

                value=float(coef_initial),

                step=1.0,

                key=f"coef_{i}"

            )

        with col2:

            avec_td = st.toggle(

                "Activer le TD (40 %)",

                value=False,

                key=f"td_{i}"

            )

        if avec_td:

            col1, col2 = st.columns(2)

            with col1:

                td = st.number_input(

                    "Note TD /20",

                    min_value=0.0,

                    max_value=20.0,

                    step=0.25,

                    key=f"note_td_{i}"

                )

            with col2:

                examen = st.number_input(

                    "Note examen /20",

                    min_value=0.0,

                    max_value=20.0,

                    step=0.25,

                    key=f"exam_{i}"

                )

            note_finale = td * 0.4 + examen * 0.6

        else:

            examen = st.number_input(

                "Note examen /20",

                min_value=0.0,

                max_value=20.0,

                step=0.25,

                key=f"exam_{i}"

            )

            note_finale = examen

        st.caption(f"Note finale : **{note_finale:.2f}/20**")

        total_points += note_finale * coef

        total_coef += coef

# CALCUL AUTOMATIQUE

with zone_moyenne.container():

    st.metric(

        "💜 MA MOYENNE GÉNÉRALE",

        f"{total_points / total_coef:.2f}/20"

        if total_coef > 0 else "0.00/20"

    )

    if total_coef > 0:

        moyenne = total_points / total_coef

        if moyenne >= 10:

            st.success("🎉 Tu as la moyenne !")

        else:

            st.info("Continue tes efforts 💪")

st.caption(f"Total des coefficients : {total_coef:g}")