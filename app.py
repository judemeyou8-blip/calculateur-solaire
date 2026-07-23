import streamlit as st
import pandas as pd

# Configuration de la page pour un affichage optimal sur smartphone
st.set_page_config(
    page_title="SolairePro - Dimensionnement & Normes",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un look "App Mobile" moderne et professionnel
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    /* Bannière d'en-tête immersive */
    .hero-banner {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.9)), 
                    url('https://images.unsplash.com/photo-1509391365360-e835f377e169?q=80&w=1200&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 25px 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .app-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #fb923c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    .app-subtitle {
        color: #cbd5e1;
        font-size: 13px;
        font-weight: 400;
        margin: 0;
        letter-spacing: 0.2px;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        color: white;
        font-weight: 700;
        border-radius: 12px;
        height: 52px;
        border: none;
        font-size: 15px;
        box-shadow: 0 4px 12px rgba(249, 115, 22, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ea580c 0%, #c2410c 100%);
        box-shadow: 0 6px 16px rgba(249, 115, 22, 0.4);
    }
    .metric-card {
        background-color: white;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02), 0 2px 4px -2px rgba(0,0,0,0.02);
        margin-bottom: 12px;
        text-align: center;
        border-left: 4px solid #0284c7;
        border: 1px solid #f1f5f9;
    }
    .norme-box {
        background-color: #f0f9ff;
        padding: 14px;
        border-radius: 10px;
        border-left: 4px solid #0284c7;
        margin-bottom: 12px;
        font-size: 13.5px;
        color: #0369a1;
        border: 1px solid #e0f2fe;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête avec bannière visuelle moderne
st.markdown("""
    <div class="hero-banner">
        <div class="app-title">☀️ SolairePro</div>
        <div class="app-subtitle">Plateforme d'ingénierie et de dimensionnement photovoltaïque</div>
    </div>
""", unsafe_allow_html=True)

# Navigation par onglets (uniquement Calculateur et Normes)
tab1, tab2 = st.tabs(["⚡ Calculateur", "📜 Normes & Sécurité"])

with tab1:
    # Étape 1 : Choix de la typologie des équipements
    st.markdown("### 📋 Équipements électriques & Charges")
    st.markdown("<small style='color: #64748b;'>Sélectionnez et ajustez les appareils à intégrer dans le dimensionnement :</small>", unsafe_allow_html=True)

    default_appliances = [
        {"nom": "Ampoule LED", "icone": "💡", "puissance": 10, "demarrage": 1.0, "quantite": 5, "heures": 5},
        {"nom": "Téléviseur LED / Solaire", "icone": "📺", "puissance": 60, "demarrage": 1.0, "quantite": 1, "heures": 4},
        {"nom": "Réfrigérateur / Congélateur", "icone": "🧊", "puissance": 150, "demarrage": 3.0, "quantite": 1, "heures": 8},
        {"nom": "Ventilateur", "icone": "🌀", "puissance": 65, "demarrage": 1.5, "quantite": 2, "heures": 6},
        {"nom": "Routeur Wi-Fi / Box", "icone": "🛜", "puissance": 15, "demarrage": 1.0, "quantite": 1, "heures": 24},
        {"nom": "Pompe à eau (1/2 CV)", "icone": "💧", "puissance": 375, "demarrage": 4.0, "quantite": 0, "heures": 1},
        {"nom": "Climatiseur Inverter", "icone": "❄️", "puissance": 900, "demarrage": 2.5, "quantite": 0, "heures": 3},
    ]

    user_data = []
    for i, item in enumerate(default_appliances):
        with st.expander(f"{item['icone']}  {item['nom']}  —  ({item['puissance']}W)"):
            col1, col2 = st.columns(2)
            with col1:
                qte = st.number_input(f"Quantité", min_value=0, max_value=20, value=item['quantite'], key=f"qte_{i}")
                pow_val = st.number_input(f"Puissance unitaire (W)", min_value=1, max_value=5000, value=item['puissance'], key=f"pow_{i}")
            with col2:
                hrs = st.number_input(f"Heures d'utilisation / jour", min_value=0.0, max_value=24.0, value=float(item['heures']), step=0.5, key=f"hrs_{i}")
                dem = st.number_input(f"Facteur de démarrage", min_value=1.0, max_value=6.0, value=float(item['demarrage']), step=0.1, key=f"dem_{i}")
            
            user_data.append({
                "Appareil": f"{item['icone']} {item['nom']}",
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
    st.markdown("### ⚙️ Paramètres de l'installation")

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
        
        conso_totale_wh = df["Énergie (Wh/j)"].sum()
        conso_avec_pertes = conso_totale_wh * 1.20 # 20% de pertes globales

        puissance_continue_max = (df["Puissance (W)"] * df["Quantité"]).sum()
        max_pic_appareil = (df["Puissance Pic (W)"]).max() if not df.empty else 0
        puissance_pic_totale = puissance_continue_max - max_pic_appareil + max_pic_appareil if not df.empty else 0

        puissance_panneaux_wc = conso_avec_pertes / ensoleillement
        capacite_batterie_wh = (conso_avec_pertes * autonomie_jours) / dod
        capacite_batterie_ah = capacite_batterie_wh / tension_systeme

        st.markdown("---")
        st.markdown("## 📊 Rapport de Synthèse")

        st.success(f"**Énergie Journalière :** {conso_totale_wh:,.0f} Wh/j *(avec pertes : {conso_avec_pertes:,.0f} Wh)*")

        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.markdown(f"""
                <div class="metric-card">
                    <h4>☀️ Panneaux Solaires</h4>
                    <h2 style='color: #d97706;'>{puissance_panneaux_wc:,.0f} Wc</h2>
                    <p><small>Champ photovoltaïque minimal</small></p>
                </div>
            """, unsafe_allow_html=True)

        with col_res2:
            st.markdown(f"""
                <div class="metric-card">
                    <h4>🔋 Parc Batteries</h4>
                    <h2 style='color: #2563eb;'>{capacite_batterie_ah:,.0f} Ah</h2>
                    <p><small>Sous {tension_systeme}V ({type_batterie.split()[0]})</small></p>
                </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="metric-card">
                <h4>⚡ Onduleur Recommandé</h4>
                <h2 style='color: #dc2626;'>{puissance_pic_totale * 1.25:,.0f} VA</h2>
                <p><small>Sécurité pics de démarrage incluse</small></p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📝 Détail des charges sélectionnées")
        active_df = df[df["Quantité"] > 0][["Appareil", "Puissance (W)", "Quantité", "Heures/Jour", "Énergie (Wh/j)"]]
        if not active_df.empty:
            st.dataframe(active_df, hide_index=True)
        else:
            st.info("Aucun appareil sélectionné.")

with tab2:
    st.markdown("### 📜 Normes & Bonnes Pratiques en Installation Solaire")
    st.markdown("<small style='color: #64748b;'>Règles de l'art et conformité technique pour des installations sécurisées et durables.</small>", unsafe_allow_html=True)
    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="norme-box">
            <b>1. Protection et Section des Câbles (DC / AC)</b><br>
            • Utilisation impérative de câbles solaires spécifiques résistants aux UV (ex: H1Z2Z2-K).<br>
            • Chute de tension maximale tolérée de <b>3%</b> entre les panneaux et le régulateur ou l'onduleur.<br>
            • Dimensionnement des sections selon l'intensité maximale pour éliminer tout risque d'échauffement.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="norme-box">
            <b>2. Protections Électriques & Appareillage</b><br>
            • <b>Côté DC :</b> Pose obligatoire d'un interrupteur-sectionneur et de fusibles ou disjoncteurs adaptés.<br>
            • <b>Parafoudres :</b> Intégration de protections contre les surtensions transitoires (foudre) sur les lignes DC et AC.<br>
            • <b>Côté AC :</b> Coffret de protection divisionnaire avec disjoncteurs magnétothermiques et différentiel 30mA.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="norme-box">
            <b>3. Mise à la Terre et Sécurité des Personnes</b><br>
            • Interconnexion équipotentielle des châssis de panneaux, des structures porteuses et des masses des équipements.<br>
            • Résistance de prise de terre visée : <b>inférieure à 10 ohms</b>.<br>
            • Consigne stricte : ne jamais débrancher un connecteur DC en charge sous rayonnement direct.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="norme-box">
            <b>4. Local Technique & Ventilation des Batteries</b><br>
            • Implantation des parcs de batteries dans un espace sec, tempéré et ventilé pour dissiper les calories.<br>
            • Surveillance indispensable via un BMS actif pour les technologies lithium afin d'éviter tout emballement thermique.
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 12px;'>SolairePro - Conçu pour les ingénieurs et installateurs terrain</p>", unsafe_allow_html=True)
    
