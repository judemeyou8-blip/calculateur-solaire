import streamlit as st
import pandas as pd

# Configuration de la page pour un affichage optimal sur smartphone
st.set_page_config(
    page_title="SolairePro - Accueil, Dimensionnement & Normes",
    page_icon="☀️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un look "App Mobile" moderne, inspiré des standards industriels actuels
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
        padding: 35px 20px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .app-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 30px;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #fb923c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
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
    /* Cartes équipements style E-commerce technique */
    .catalog-card {
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03), 0 2px 4px -1px rgba(0,0,0,0.02);
        overflow: hidden;
        margin-bottom: 16px;
        border: 1px solid #e2e8f0;
        transition: transform 0.2s ease;
    }
    .catalog-img-container {
        position: relative;
        width: 100%;
        height: 120px;
        overflow: hidden;
        background-color: #f1f5f9;
    }
    .catalog-img-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .catalog-badge {
        position: absolute;
        top: 8px;
        right: 8px;
        background-color: rgba(15, 23, 42, 0.85);
        color: #38bdf8;
        font-size: 10px;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 20px;
        backdrop-filter: blur(4px);
    }
    .catalog-content {
        padding: 12px;
    }
    .catalog-title {
        font-size: 13.5px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 4px;
    }
    .catalog-desc {
        font-size: 11.5px;
        color: #64748b;
        margin: 0;
        line-height: 1.4;
    }
    .news-card {
        background-color: white;
        padding: 14px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
        margin-bottom: 12px;
        border-left: 4px solid #f97316;
        border: 1px solid #f1f5f9;
        font-size: 13px;
        color: #334155;
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

# Navigation par onglets
tab0, tab1, tab2 = st.tabs(["🏠 Accueil & Équipements", "⚡ Calculateur", "📜 Normes & Sécurité"])

with tab0:
    st.markdown("### 🛠️ Catalogue & Équipements Modernes")
    st.markdown("<small style='color: #64748b;'>Sélection de composants industriels et résidentiels de dernière génération :</small>", unsafe_allow_html=True)
    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

    # Grille d'équipements sur 2 colonnes avec des visuels haut de gamme ciblés
    col_e1, col_e2 = st.columns(2)
    
    with col_e1:
        # 1. Panneau Solaire
        st.markdown("""
            <div class="catalog-card">
                <div class="catalog-img-container">
                    <img src="https://images.unsplash.com/photo-1508817583692-057a6833c948?q=80&w=600&auto=format&fit=crop">
                    <span class="catalog-badge">Tier 1</span>
                </div>
                <div class="catalog-content">
                    <div class="catalog-title">Panneau Monocristallin</div>
                    <p class="catalog-desc">Modules haute efficacité (>21%) à cellules 182mm/210mm demi-coupées.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. Régulateur / Onduleur Hybride
        st.markdown("""
            <div class="catalog-card">
                <div class="catalog-img-container">
                    <img src="https://images.unsplash.com/photo-1624397640307-ebdce12484f1?q=80&w=600&auto=format&fit=crop">
                    <span class="catalog-badge">MPPT</span>
                </div>
                <div class="catalog-content">
                    <div class="catalog-title">Onduleur & Régulateur</div>
                    <p class="catalog-desc">Conversion pure sinusoïde avec suivi MPPT ultra-rapide et Wi-Fi intégré.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 3. Téléviseur / Appareil Solaire CC
        st.markdown("""
            <div class="catalog-card">
                <div class="catalog-img-container">
                    <img src="https://images.unsplash.com/photo-1593784991095-a205069470b6?q=80&w=600&auto=format&fit=crop">
                    <span class="catalog-badge">Basse Conso</span>
                </div>
                <div class="catalog-content">
                    <div class="catalog-title">Équipements & Télé DC</div>
                    <p class="catalog-desc">Appareils à haut rendement énergétique optimisés pour l'autoconsommation directe.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_e2:
        # 4. Stockage Lithium Avancé
        st.markdown("""
            <div class="catalog-card">
                <div class="catalog-img-container">
                    <img src="https://images.unsplash.com/photo-1617788138017-80ad40651399?q=80&w=600&auto=format&fit=crop">
                    <span class="catalog-badge">LiFePO4</span>
                </div>
                <div class="catalog-content">
                    <div class="catalog-title">Batterie Lithium LiFePO4</div>
                    <p class="catalog-desc">Stockage modulaire sécurisé, BMS intelligent et durée de vie > 6000 cycles.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 5. Disjoncteur & Coffrets de Protection DC/AC
        st.markdown("""
            <div class="catalog-card">
                <div class="catalog-img-container">
                    <img src="https://images.unsplash.com/photo-1558449028-b53a39d100fc?q=80&w=600&auto=format&fit=crop">
                    <span class="catalog-badge">Sécurité IP65</span>
                </div>
                <div class="catalog-content">
                    <div class="catalog-title">Disjoncteurs & Coffrets DC</div>
                    <p class="catalog-desc">Sectionneurs, parafoudres et protections modulaires conformes aux normes.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 6. Pompage Solaire / Accessoires
        st.markdown("""
            <div class="catalog-card">
                <div class="catalog-img-container">
                    <img src="https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?q=80&w=600&auto=format&fit=crop">
                    <span class="catalog-badge">Pro</span>
                </div>
                <div class="catalog-content">
                    <div class="catalog-title">Câblage & Accessoires</div>
                    <p class="catalog-desc">Câbles solaires anti-UV H1Z2Z2-K et connecteurs étanches MC4 professionnels.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📰 Actualités & Tendances du Solaire")
    
    st.markdown("""
        <div class="news-card">
            <b>🚀 Essor des onduleurs hybrides intelligents</b><br>
            Les nouvelles gammes intègrent un pilotage cloud et mobile permettant d'ajuster dynamiquement la charge des batteries selon les prévisions météorologiques locales.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="news-card">
            <b>🔋 Standardisation du LiFePO4 en résidentiel</b><br>
            Les parcs de batteries au plomb cèdent définitivement la place aux racks lithium modulaires, garantissant une profondeur de décharge (DoD) de 80% à 90% sans perte de performance.
        </div>
    """, unsafe_allow_html=True)

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
