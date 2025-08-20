import streamlit as st
import joblib
import pandas as pd

# ======================
# Charger le modèle ML
# ======================
model_loaded = joblib.load("model_diamnd2.joblib")

# ======================
# Configuration Streamlit
# ======================
st.set_page_config(
    page_title="💎 Prédiction du Prix des Diamants",
    layout="wide",
    page_icon="💍"
)

# ======================
# En-tête
# ======================
st.title("💎 Estimation du Prix des Diamants")
st.markdown(
    """
    ### Bienvenue !  
    Cet outil utilise un modèle d’**intelligence artificielle** pour estimer le prix de votre diamant.  
    Remplissez les caractéristiques dans le panneau à gauche et obtenez une estimation instantanée.  
    """
)

# ======================
# Sidebar pour saisie utilisateur
# ======================
st.sidebar.header("📌 Paramètres du diamant")

carat = st.sidebar.number_input("Carat (poids en carats)", min_value=0.1, max_value=5.0, step=0.01, value=1.0)
x = st.sidebar.number_input("Longueur (mm)", min_value=0.1, max_value=15.0, step=0.1, value=5.0)
y = st.sidebar.number_input("Largeur (mm)", min_value=0.1, max_value=15.0, step=0.1, value=5.0)
z = st.sidebar.number_input("Hauteur (mm)", min_value=0.1, max_value=15.0, step=0.1, value=3.0)

# ======================
# Préparation des données
# ======================
input_data = pd.DataFrame({
    "carat": [carat],
    "x": [x],
    "y": [y],
    "z": [z]
})

# ======================
# Zone principale avec cartes
# ======================
st.markdown("---")
st.subheader("🔎 Résultat de la prédiction")

if st.button("✨ Prédire le Prix"):
    prediction = model_loaded.predict(input_data)[0]

    st.success("✅ Estimation terminée avec succès !")

    st.markdown(
        f"""
        <div style='background-color:#f0f9ff; padding:20px; border-radius:12px; text-align:center;'>
            <h2 style='color:#0077b6;'>💰 Prix estimé du diamant</h2>
            <h1 style='color:#023e8a;'> {prediction:,.0f} $ </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# ======================
# Footer
# ======================
st.markdown("---")
st.caption("💍 Application de prédiction réalisée avec **Python & Streamlit**")
