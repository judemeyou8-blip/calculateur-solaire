import streamlit as st
import pandas as pd

# Configuration de la page pour un affichage optimal sur smartphone
st.set_page_config(
    page_title="SolairePro Bénin - Dimensionnement",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un look "App Mobile" épuré et moderne
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff9f1c;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e88d12;
        color: white;
    }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête de l'application
st.markdown("<h2 style='text-align: center; color: #2d3748;'>☀️ SolairePro Bénin</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #718096;'>Outil intelligent de dimensionnement pour kits domestiques</p>", unsafe_allow_html=True)
st.markdown("---")

# Étape 1 : Choix de la typologie des équipements
st.markdown("### 1. 📋 Vos équipements électriques")
st.markdown("<small>Sélectionnez et ajustez les appareils que vous souhaitez alimenter :</small>", unsafe_allow_html=True)

# Base de données par défaut des appareils au Bénin
default_appliances = [
    {"nom": "Ampoule LED", "puissance": 10, "demarrage": 1.0, "quantite": 5, "heures": 5},
    {"nom": "Téléviseur LED", "puissance": 80, "demarrage": 1.0, "quantite": 1, "heures": 4},
    {"nom": "Réfrigérateur / Congélateur", "puissance": 150, "demarrage": 3.0, "quantite": 1, "heures": 8},
    {"nom": "Ventilateur", "puissance": 65, "demarrage": 1.5, "quantite": 2, "heures": 6},
    {"nom": "Routeur Wi-Fi / Box", "puissance": 15, "demarrage": 1.0, "quantite": 1, "heures": 24},
    {"nom": "Pompe à eau (1/2 CV)", "puissance": 375, "demarrage": 4.0, "quantite": 0, "heures": 1},
    {"nom": "Climatiseur (1 CV)", "puissance": 1000, "demarrage": 3.5, "quantite": 0, "heures": 3},
]

# Formulaire dynamique pour chaque appareil
user_data = []
for i, item in enumerate(default_appliances):
    with st.expander(f"🔹 {item['nom']} ({item['puissance']}W)"):
        col1, col2 = st.columns(2)
        with col1:
            qte = st.number_input(f"Quantité", min_value=0, max_value=20, value=item['quantite'], key=f"qte_{i}")
            pow_val = st.number_input(f"Puissance (W)", min_value=1, max_value=5000, value=item['puissance'], key=f"pow_{i}")
        with col2:
            hrs = st.number_input(f"Heures/jour", min_value=0.0, max_value=24.0, value=float(item['heures']), step=0.5, key=f"hrs_{i}")
            dem = st.number_input(f"Facteur démarrage", min_value=1.0, max_value=6.0, value=float(item['demarrage']), step=0.1, key=f"dem_{i}")
        
        user_data.append({
            "Appareil": item['nom'],
            "Puissance (W)": pow_val,
            "Quantité": qte,
            "Heures/Jour": hrs,
            "Facteur Démarrage": dem,
            "Énergie (Wh/j)": pow_val * qte * hrs,
            "Puissance Pic (W)": pow_val * qte * dem
        })

df = pd.DataFrame(user_data)

# Étape 2 : Paramètres système avancés
st.markdown("---")
st.markdown("### 2. ⚙️ Paramètres de l'installation")

col_p1, col_p2 = st.columns(2)
with col_p1:
    tension_systeme = st.selectbox("Tension Système (V)", [12, 24, 48], index=2)
with col_p2:
    autonomie_jours = st.slider("Autonomie (jours sans soleil)", min_value=1, max_value=3, value=1)

col_p3, col_p4 = st.columns(2)
with col_p3:
    type_batterie = st.selectbox("Technologie Batterie", ["Lithium (DoD 80%)", "Plomb/AGM (DoD 50%)"])
    dod = 0.8 if "Lithium" in type_batterie else 0.5
with col_p4:
    ensoleillement = st.slider("Ensoleillement équivalent (h/j)", min_value=3.0, max_value=6.0, value=4.5, step=0.1)

# Bouton de calcul principal
st.markdown("---")
if st.button("🚀 LANCER LE DIMENSIONNEMENT TECHNIQUE"):
    
    # Calculs énergétiques
conso_totale_wh = df["Énergie (Wh/j)"].sum()
    # Ajout de 20% de pertes de conversion (onduleur + câblage)
conso_avec_pertes = conso_totale_wh * 1.20

    # Puissance continue max et puissance pic
puissance_continue_max = (df["Puissance (W)"] * df["Quantité"]).sum()
    # Le pic max prend en compte le gros appareil qui démarre + les autres en fonctionnement continu
max_pic_appareil = (df["Puissance Pic (W)"]).max()
puissance_pic_totale = puissance_continue_max - df["Puissance Pic (W)"].max() + max_pic_appareil if not df.empty else 0

    # Dimensionnement Panneaux Solaires (Wc)
puissance_panneaux_wc = conso_avec_pertes / ensoleillement

    # Dimensionnement Batterie (Wh puis Ah)
capacite_batterie_wh = (conso_avec_pertes * autonomie_jours) / dod
capacite_batterie_ah = capacite_batterie_wh / tension_systeme

    # Affichage des résultats sous forme de rapport professionnel
st.markdown("---")
st.markdown("## 📊 Rapport de Dimensionnement")

    # KPIs visuels
st.success(f"**Consommation Journalière Totale :** {conso_totale_wh:,.0f} Wh/jour *(avec pertes : {conso_avec_pertes:,.0f} Wh)*")

col_res1, col_res2 = st.columns(2)
with col_res1:
    st.markdown(f"""
        <div class="metric-card">
            <h4>☀️ Panneaux Solaires</h4>
            <h2 style='color: #d69e2e;'>{puissance_panneaux_wc:,.0f} Wc</h2>
            <p><small>Champ photovoltaïque minimal</small></p>
        </div>
    """, unsafe_allow_html=True)

with col_res2:
    st.markdown(f"""
        <div class="metric-card">
            <h4>🔋 Parc Batteries</h4>
            <h2 style='color: #3182ce;'>{capacite_batterie_ah:,.0f} Ah</h2>
            <p><small>Sous {tension_systeme}V ({type_batterie})</small></p>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <div class="metric-card">
        <h4>⚡ Onduleur Recommandé</h4>
        <h2 style='color: #e53e3e;'>{puissance_pic_totale * 1.25:,.0f} VA</h2>
        <p><small>Incluant le coefficient de sécurité pour les pics de démarrage</small></p>
    </div>
""", unsafe_allow_html=True)

# Tableau récapitulatif détaillé pour le client
st.markdown("### 📝 Détail des charges sélectionnées")
active_df = df[df["Quantité"] > 0][["Appareil", "Puissance (W)", "Quantité", "Heures/Jour", "Énergie (Wh/j)"]]
if not active_df.empty:
    st.dataframe(active_df, hide_index=True)
else:
    st.info("Aucun appareil sélectionné.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #a0aec0; font-size: 12px;'>SolairePro Bénin - Conçu pour les ingénieurs et installateurs terrain</p>", unsafe_allow_html=True)
                          
