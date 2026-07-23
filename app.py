import streamlit as st
import pandas as pd

# Configuration de la page pour un affichage optimal sur smartphone
st.set_page_config(
    page_title="SolairePro - Dimensionnement & Normes",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un look "App Mobile" moderne et visuel
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    /* Style du titre avec dégradé Bleu et Orange */
    .app-title {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 32px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1d4ed8 0%, #f97316 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .app-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 14px;
        margin-top: 5px;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #f97316;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #ea580c;
        color: white;
    }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        text-align: center;
        border-left: 4px solid #1d4ed8;
    }
    .norme-box {
        background-color: #eff6ff;
        padding: 12px;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin-bottom: 10px;
        font-size: 14px;
        color: #1e3a8a;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête stylisé
st.markdown('<div class="app-title">☀️ SolairePro</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Dimensionnement intelligent & Conformité technique</div>', unsafe_allow_html=True)
st.markdown("---")

# Navigation par onglets
tab1, tab2 = st.tabs(["⚡ Calculateur", "📜 Normes & Sécurité"])

with tab1:
    # Étape 1 : Choix de la typologie des équipements avec visuels
    st.markdown("### 📋 Équipements électriques & Visuels")
    st.markdown("<small>Sélectionnez et ajustez les charges à intégrer dans le dimensionnement :</small>", unsafe_allow_html=True)

    # Base de données enrichie avec des émojis illustratifs puissants
    default_appliances = [
        {"nom": "Ampoule LED", "icone": "💡", "puissance": 10, "demarrage": 1.0, "quantite": 5, "heures": 5},
        {"nom": "Téléviseur LED", "icone": "📺", "puissance": 80, "demarrage": 1.0, "quantite": 1, "heures": 4},
        {"nom": "Réfrigérateur / Congélateur", "icone": "🧊", "puissance": 150, "demarrage": 3.0, "quantite": 1, "heures": 8},
        {"nom": "Ventilateur", "icone": "🌀", "puissance": 65, "demarrage": 1.5, "quantite": 2, "heures": 6},
        {"nom": "Routeur Wi-Fi / Box", "icone": "🛜", "puissance": 15, "demarrage": 1.0, "quantite": 1, "heures": 24},
        {"nom": "Pompe à eau (1/2 CV)", "icone": "💧", "puissance": 375, "demarrage": 4.0, "quantite": 0, "heures": 1},
        {"nom": "Climatiseur (1 CV)", "icone": "❄️", "puissance": 1000, "demarrage": 3.5, "quantite": 0, "heures": 3},
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
        conso_avec_pertes = conso_totale_wh * 1.20 # 20% de pertes globales (onduleur/câbles)

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
    st.markdown("<small>Règles de l'art et conformité technique pour des installations sécurisées et durables.</small>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="norme-box">
            <b>1. Protection et Section des Câbles (DC / AC)</b><br>
            • Les câbles photovoltaïques (côté panneaux) doivent résister aux UV et aux intempéries (ex: câbles solaires type H1Z2Z2-K).<br>
            • La chute de voltage entre les panneaux et le régulateur/onduleur ne doit pas dépasser <b>3%</b>.<br>
            • Dimensionner les sections de câbles en fonction de l'intensité maximale (Ampères) pour éviter tout échauffement ou risque d'incendie.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="norme-box">
            <b>2. Protections Électriques & Appareillage</b><br>
            • <b>Côté DC (Continu) :</b> Installer obligatoirement un interrupteur-sectionneur DC et des fusibles ou disjoncteurs adaptés entre les panneaux et le régulateur/onduleur.<br>
            • <b>Parafoudres :</b> Recommandé d'installer des parafoudres DC et AC pour protéger le matériel contre les surtensions dues à la foudre.<br>
            • <b>Côté AC (Alternatif) :</b> Prévoir un tableau de protection divisionnaire avec disjoncteurs magnétothermiques et interrupteurs différentiels (30mA).
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="norme-box">
            <b>3. Mise à la Terre et Sécurité des Personnes</b><br>
            • Relier les châssis métalliques des panneaux solaires, les supports et les masses des équipements à une prise de terre dédiée.<br>
            • Résistance de terre conseillée : <b>inférieure à 10 ohms</b> pour garantir le déclenchement des protections en cas de défaut d'isolement.<br>
            • Ne jamais manipuler les connexions DC sous charge en plein ensoleillement (risque d'arc électrique dangereux).
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="norme-box">
            <b>4. Ventilation et Emplacement des Batteries</b><br>
            • Les batteries (surtout plomb/AGM) doivent être installées dans un local sec, tempéré et <b>correctement ventilé</b> pour évacuer les dégagements de gaz (hydrogène en fin de charge).<br>
            • Les batteries au lithium doivent être équipées d'un BMS (Battery Management System) fonctionnel pour surveiller la température et les tensions par cellule.
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 12px;'>SolairePro - Conçu pour les ingénieurs et installateurs terrain</p>", unsafe_allow_html=True)
    
