import streamlit as st
import datetime
from datetime import timedelta
import pandas as pd

# ==========================================
# Phase 14: BEAUTIFUL CUTE & AESTHETIC PASTELL UI
# ==========================================

st.markdown(
    """
    <style>
    /* Beautiful Aesthetic Pastel Background */
    .stApp {
        background: linear-gradient(135deg, #fff0f6 0%, #e6f7ff 100%);
    }
    
    /* Cute & Elegant Main Header with Smooth Floating Motion */
    .main-header {
        font-size: 2.8rem !important;
        font-weight: bold;
        color: #d81b60; /* Soft Premium Pink Deep */
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(216, 27, 96, 0.1);
        animation: cuteFloat 3s ease-in-out infinite alternate;
    }
    
    /* Elegant Soft Subtitle */
    .sub-header {
        font-size: 1.1rem;
        color: #7d7f9a; 
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Cute Section Titles with Left Border Accent */
    .section-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #ad1457;
        margin-top: 15px;
        margin-bottom: 15px;
        padding-left: 8px;
        border-left: 4px solid #ff85a2;
    }

    /* Cute Floating Lady Mascot Wrapper */
    .ladies-avatar {
        font-size: 75px;
        text-align: center;
        display: block;
        margin: 5px 0;
        animation: cuteFloatAlt 2.5s ease-in-out infinite alternate;
    }
    
    /* Beautiful Cute Rounded Pastel Cards */
    .metric-card {
        background-color: rgba(255, 255, 255, 0.85);
        border: 2px solid #ffe3ec;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 6px 12px rgba(255, 182, 193, 0.15);
        transition: all 0.3s ease-in-out;
    }
    .metric-card:hover {
        border-color: #ff85a2;
        transform: translateY(-4px) scale(1.02);
        box-shadow: 0 10px 20px rgba(255, 182, 193, 0.25);
    }
    
    /* --- CUTE SMOOTH MOTION ANIMATIONS --- */
    @keyframes cuteFloat {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-6px); }
    }
    @keyframes cuteFloatAlt {
        0% { transform: translateY(0px) scale(1); }
        100% { transform: translateY(-10px) scale(1.04); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SIDEBAR NAVIGATION (Cute Pink Accent) ---
st.sidebar.markdown("<h2 style='color: #d81b60; text-align: center;'>🌸 Health Center</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Go to Page:", [
    "🏠 Home Dashboard", 
    "📝 Daily Health Log", 
    "🩺 Symptom Assessment",
    "📊 Historical Logs",
    "💧 Hydration Metrics",
    "💡 Cute Health Insights"
])

# Initialize Session Data
if 'user_symptoms' not in st.session_state:
    st.session_state['user_symptoms'] = []
if 'water_glasses' not in st.session_state:
    st.session_state['water_glasses'] = 0
if 'history_logs' not in st.session_state:
    st.session_state['history_logs'] = [
        {"Date": "2026-05-10", "Symptoms Logged": "Cramps/Abdominal Pain", "Energy Level": "🧘‍♂️ Medium"},
        {"Date": "2026-06-01", "Symptoms Logged": "No Symptoms", "Energy Level": "🚀 Excellent"}
    ]

# ==========================================
# PAGE 1: HOME & CYCLE PREDICTOR
# ==========================================
if "🏠" in page:
    st.markdown('<h1 class="main-header">🌸 Women\'s Health Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your beautiful personal space for biological cycle tracking.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ladies-avatar">🙋‍♀️</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="section-title">🗓️ Cycle Predictor Engine</p>', unsafe_allow_html=True)
    last_period = st.date_input("Select the start date of your last period:", datetime.date.today())
    cycle_length = st.slider("Select your average cycle length (in days):", 21, 45, 28)

    next_period = last_period + timedelta(days=cycle_length)
    ovulation_day = next_period - timedelta(days=14)

    st.success("🔮 **Your Predictions are Ready Beautiful:**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="metric-card" style="border-left: 5px solid #ff85a2;"><h5>📅 Expected Period Date</h5><h3 style="color: #d81b60; margin-top:10px;">{next_period.strftime("%d %B, %Y")}</h3></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card" style="border-left: 5px solid #bce6ff;"><h5>🥚 Estimated Ovulation Day</h5><h3 style="color: #00838F; margin-top:10px;">{ovulation_day.strftime("%d %B, %Y")}</h3></div>', unsafe_allow_html=True)

# ==========================================
# PAGE 2: DAILY HEALTH LOG
# ==========================================
elif "📝" in page:
    st.markdown('<h1 class="main-header">📝 Daily Symptom Logger</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Log how you feel today to stay on top of your health.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ladies-avatar">👩‍💻</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="section-title">✍️ How are you feeling today?</p>', unsafe_allow_html=True)
    selected_symptoms = st.multiselect(
        "Select any symptoms:",
        ["No Symptoms", "Cramps/Abdominal Pain", "Headache", "Fatigue/Low Energy", "Bloating", "Acne breakouts", "Mood Swings"]
    )
    st.session_state['user_symptoms'] = selected_symptoms

    energy_level = st.select_slider("Your Energy Level:", options=["🏃‍♂️ Very Low", "🚶‍♂️ Low", "🧘‍♂️ Medium", "⚡ High", "🚀 Excellent"])

    if st.button("Save Daily Log"):
        st.balloons()
        new_log = {
            "Date": str(datetime.date.today()),
            "Symptoms Logged": ", ".join(selected_symptoms) if selected_symptoms else "None",
            "Energy Level": energy_level
        }
        st.session_state['history_logs'].append(new_log)
        st.success("✨ Logs saved beautifully! Head over to 'Historical Logs' to see your data.")

# ==========================================
# PAGE 3: SYMPTOM SEVERITY CHECKER
# ==========================================
elif "🩺" in page:
    st.markdown('<h1 class="main-header">🩺 Symptom Assessment</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Take a quick assessment to track pain thresholds safely.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ladies-avatar">👩‍⚕️</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="section-title">🔍 Quick Self-Assessment</p>', unsafe_allow_html=True)
    pain_level = st.radio("1. How severe are your cramps today?", ["None", "Mild (Manageable)", "Moderate (Affects daily tasks)", "Severe (Unbearable)"])
    meds = st.selectbox("2. Did you take any pain-relief medication today?", ["No", "Yes, it helped", "Yes, but pain is still there"])
    days = st.number_input("3. For how many days have you been feeling heavy pain?", min_value=0, max_value=10, value=0)

    if st.button("Analyze Severity"):
        if pain_level == "Severe (Unbearable)" or days > 3:
            st.error("🚨 **Recommendation:** Pain levels seem a bit high. We strongly advise taking complete rest or consulting a professional doctor.")
        elif pain_level == "Moderate (Affects daily tasks)":
            st.warning("⚠️ **Recommendation:** Take proper rest, drink warm fluids like chamomile tea, and stay away from stress.")
        else:
            st.success("✅ **Recommendation:** Everything looks completely normal. Rest up and stay cozy!")

# ==========================================
# PAGE 4: CYCLE HISTORY LOGS
# ==========================================
elif "📊" in page:
    st.markdown('<h1 class="main-header">📊 Your Historical Logs</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your beautifully organized past records and tracking data.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ladies-avatar">🤸‍♀️</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="section-title">📋 Medical History Table</p>', unsafe_allow_html=True)
    df = pd.DataFrame(st.session_state['history_logs'])
    st.dataframe(df, use_container_width=True)

# ==========================================
# PAGE 5: HYDRATION TRACKER
# ==========================================
elif "💧" in page:
    st.markdown('<h1 class="main-header">💧 Hydration Metrics</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Keep your skin glowing and body hydrated throughout your cycle.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ladies-avatar">🧘‍♀️</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="section-title">🥛 Tracker Counter</p>', unsafe_allow_html=True)
    st.subheader("Target: 8 Glasses per day")
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    with col_btn1:
        if st.button("➕ Glass"): st.session_state['water_glasses'] += 1
    with col_btn2:
        if st.button("➖ Glass") and st.session_state['water_glasses'] > 0: st.session_state['water_glasses'] -= 1
    with col_btn3:
        if st.button("🔄 Reset"): st.session_state['water_glasses'] = 0

    current_glasses = st.session_state['water_glasses']
    st.progress(min(current_glasses / 8, 1.0))
    st.metric(label="Glasses Logged", value=f"{current_glasses} / 8")

    if current_glasses >= 8:
        st.balloons()
        st.success("🏆 Goal Achieved Gorgeous! Optimal hydration level reached.")

# ==========================================
# PAGE 6: SMART HEALTH INSIGHTS
# ==========================================
elif "💡" in page:
    st.markdown('<h1 class="main-header">💡 Cute Health Insights</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Personalized, caring health tips tailored to your body\'s needs.</p>', unsafe_allow_html=True)
    st.markdown('<div class="ladies-avatar">👸</div>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('<p class="section-title">💡 Personalized Advice for You</p>', unsafe_allow_html=True)
    symptoms = st.session_state['user_symptoms']

    if symptoms:
        if "No Symptoms" in symptoms:
            st.snow()
            st.success("🎉 You're doing amazing! Keep up the healthy habits.")
        else:
            st.warning("⚠️ Sweet tips for your logged symptoms:")
            if "Cramps/Abdominal Pain" in symptoms:
                st.write("🌋 **For Cramps:** Grab a warm heating pad. **Food choice:** Bananas or warm dark chocolate.")
            if "Headache" in symptoms or "Fatigue/Low Energy" in symptoms:
                st.write("💧 **For Fatigue:** Drink extra fluids. **Food choice:** Spinach or a handful of healthy seeds.")
            if "Bloating" in symptoms:
                st.write("🥣 **For Bloating:** Avoid extra salt. Try comforting warm ginger or peppermint tea.")
            if "Mood Swings" in symptoms:
                st.write("🧘‍♀️ **For Mood Swings:** Take deep breaths and do a light 5-minute stretching routine.")
    else:
        st.info("Log your symptoms on the 'Daily Health Log' page first to see your custom tips!")