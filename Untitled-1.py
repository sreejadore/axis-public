
import streamlit as st
import calendar
from datetime import datetime

st.set_page_config(page_title="ax/s", page_icon="🌙", layout="centered")
st.set_page_config(
    page_title="ax/s",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
/* hide streamlit default stuff */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* whole page background */
html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 20% 75%, rgba(242,134,149,0.20), transparent 24%),
        radial-gradient(circle at 70% 25%, rgba(242,232,184,0.22), transparent 22%),
        radial-gradient(circle at 55% 60%, rgba(241,204,166,0.16), transparent 26%),
        linear-gradient(180deg, #f7f3f1 0%, #f2ece7 100%);
}

/* center everything like a phone */
.block-container {
    max-width: 430px !important;
    padding-top: 0.8rem !important;
    padding-bottom: 7rem !important;
    padding-left: 0.9rem !important;
    padding-right: 0.9rem !important;
    margin: 0 auto !important;
}

/* fake phone body */
.mobile-shell {
    background: rgba(255,255,255,0.45);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.65);
    border-radius: 34px;
    min-height: 86vh;
    padding: 18px 16px 95px 16px;
    box-shadow:
        0 10px 30px rgba(0,0,0,0.08),
        inset 0 1px 0 rgba(255,255,255,0.7);
    position: relative;
    overflow: hidden;
}

/* top notch effect */
.mobile-shell::before {
    content: "";
    width: 110px;
    height: 20px;
    background: rgba(40,40,40,0.9);
    border-radius: 0 0 16px 16px;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
}

/* nice section titles */
.section-title {
    text-align: center;
    font-size: 30px;
    font-family: Georgia, serif;
    color: #6f5c52;
    margin-top: 18px;
    margin-bottom: 6px;
}

.subtitle-line {
    border: none;
    border-top: 1px solid #d7c7bf;
    margin-bottom: 20px;
}

/* inputs feel more app-like */
div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input,
div[data-baseweb="base-input"] input,
textarea {
    border-radius: 18px !important;
    border: 1px solid #e0d4cd !important;
    background: rgba(255,255,255,0.75) !important;
    padding: 14px 16px !important;
}

/* select boxes */
div[data-baseweb="select"] > div {
    border-radius: 18px !important;
    background: rgba(255,255,255,0.75) !important;
    border: 1px solid #e0d4cd !important;
}

/* regular buttons */
div.stButton > button {
    border-radius: 18px !important;
    border: none !important;
    background: linear-gradient(135deg, #f28695, #f2bfb4) !important;
    color: white !important;
    min-height: 48px !important;
    box-shadow: 0 8px 20px rgba(242,134,149,0.18) !important;
}

/* radios / labels cleaner */
label, .stRadio label, .stSelectbox label {
    color: #6f5c52 !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Session State Setup
# -----------------------
if "step" not in st.session_state:
    st.session_state.step = 0  # onboarding steps

if "page" not in st.session_state:
    st.session_state.page = "dashboard"  # app pages after onboarding

if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

if "user_data" not in st.session_state:
    st.session_state.user_data = {
        "register_username": "",
        "register_password": "",
        "confirm_password": "",
        "login_username": "",
        "login_password": "",
    }

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = {
        "age_range": "18–24",
        "height_cm": "",
        "weight_kg": "",
        "activity_level": "Moderate",
        "training_type": "Mixed",
        "main_goal": "Performance",
        "cycle_regularity": "Regular",
        "cycle_length": "",
        "cycle_phase": "Unsure",
        "birth_control": "No",
        "health_flags": [],
        "diet_pref": "No preference",
        "eating_pattern": "Regular meals",
        "restrictions": "",
        "energy_flags": [],
        "symptoms": {
            "Cramps": 2,
            "Fatigue": 2,
            "Mood swings": 2,
            "Bloating": 2,
            "Cravings": 2,
            "Sleep issues": 2,
        },
        "train_days": 3,
        "train_intensity": "Moderate",
        "training_focus": "Both",
        "sleep_quality": "Okay",
        "stress_level": "Medium",
        "weekly_feedback": True,
    }

data = st.session_state.user_data
q = st.session_state.quiz_data

# -----------------------
# Styling
# -----------------------
st.markdown("""
<style>
/* Mobile app container */
.stAppViewBlockContainer {
    max-width: 430px !important;
    margin: 0 auto !important;
    padding: 0 !important;
}

.stApp {
    background-color: #F3EAE4;
    color: #6F5C52;
}

.appViewContainer {
    padding-left: 0 !important;
    padding-right: 0 !important;
}

.main {
    padding-left: 16px !important;
    padding-right: 16px !important;
    padding-top: 16px !important;
    padding-bottom: 16px !important;
}

.main-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 82vh;
    text-align: center;
}

.big-title {
    font-size: 64px;
    font-family: Georgia, serif;
    color: #6F5C52;
    margin-bottom: 10px;
}

.logo {
    font-size: 58px;
    font-family: Georgia, serif;
    font-weight: bold;
    margin-bottom: 50px;
    color: #B89586;
}

.section-title {
    text-align: center;
    font-size: 40px;
    font-family: Georgia, serif;
    color: #6F5C52;
    margin-bottom: 8px;
}

.subtitle-line {
    border: none;
    border-top: 1.5px solid #CDB7AC;
    margin-top: 0;
    margin-bottom: 30px;
}

div.stButton > button {
    background-color: #C97A86;
    color: #2F2A28;
    border: none;
    border-radius: 999px;
    padding: 14px 30px;
    font-size: 18px;
    font-family: Georgia, serif;
    box-shadow: 0px 4px 10px rgba(80, 55, 45, 0.22);
    width: 100%;
}

div.stButton > button:hover {
    background-color: #6F978C;
    color: white;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input,
textarea {
    border-radius: 20px !important;
    border: 1px solid #D8C5BC !important;
    padding: 12px 16px !important;
    background-color: #FFF9F6 !important;
    color: #6F5C52 !important;
}

div[data-baseweb="select"] > div {
    border-radius: 20px;
    background-color: #FFF9F6;
    border: 1px solid #D8C5BC;
    color: #6F5C52;
}

label {
    font-family: Georgia, serif !important;
    color: #6F5C52 !important;
}

.nav-space {
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Helpers
# -----------------------
def bottom_nav():
    st.markdown("""
    <style>
    /* soft floating bar */
    .bottom-nav-wrap {
        position: fixed;
        bottom: 18px;
        left: 50%;
        transform: translateX(-50%);
        width: 82%;
        max-width: 520px;
        height: 88px;
        z-index: 999;
        border-radius: 34px;
        background: linear-gradient(135deg, rgba(255,255,255,0.78), rgba(242,191,180,0.22));
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(255,255,255,0.65);
        box-shadow:
            0 10px 30px rgba(242, 134, 149, 0.18),
            0 3px 10px rgba(0,0,0,0.06),
            inset 0 1px 0 rgba(255,255,255,0.7);
        overflow: visible;
    }

    /* gradient glow under bar */
    .bottom-nav-wrap::before {
        content: "";
        position: absolute;
        inset: 8px;
        border-radius: 28px;
        background:
            radial-gradient(circle at 20% 30%, rgba(242,134,149,0.14), transparent 38%),
            radial-gradient(circle at 75% 70%, rgba(242,232,184,0.22), transparent 35%),
            radial-gradient(circle at 60% 25%, rgba(241,204,166,0.18), transparent 40%);
        filter: blur(8px);
        z-index: 0;
    }

    /* real button row */
    .bottom-nav-row {
        position: fixed;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        width: 78%;
        max-width: 480px;
        z-index: 1001;
    }

    .bottom-space {
        height: 125px;
    }

    /* all nav buttons */
    .bottom-nav-row div.stButton > button {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #8a6f66 !important;
        font-size: 28px !important;
        min-height: 60px !important;
        width: 100% !important;
        padding: 0 !important;
        border-radius: 22px !important;
        transition: all 0.2s ease !important;
    }

    .bottom-nav-row div.stButton > button:hover {
        transform: scale(1.08) !important;
        color: #F28695 !important;
        background: rgba(255,255,255,0.14) !important;
    }

    .bottom-nav-row div.stButton > button:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* center plus bubble */
    .bottom-nav-row div.stButton > button[kind="secondary"] {
        width: 78px !important;
        height: 78px !important;
        min-height: 78px !important;
        margin-top: -26px !important;
        border-radius: 50% !important;
        padding: 0 !important;
        font-size: 40px !important;
        color: white !important;
        background:
            radial-gradient(circle at 72% 24%, rgba(255,255,255,0.75), rgba(255,255,255,0.0) 22%),
            radial-gradient(circle at 28% 35%, rgba(242,134,149,0.95), rgba(242,134,149,0.15) 62%),
            linear-gradient(145deg, #F28695, #F2BFB4) !important;
        border: 3px solid rgba(255,255,255,0.8) !important;
        box-shadow:
            0 10px 24px rgba(242,134,149,0.28),
            inset 0 2px 8px rgba(255,255,255,0.45) !important;
    }

    .bottom-nav-row div.stButton > button[kind="secondary"]:hover {
        transform: scale(1.06) !important;
        color: white !important;
    }

    /* optional active icon glow */
    .nav-active-glow {
        filter: drop-shadow(0 0 10px rgba(242,134,149,0.35));
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bottom-nav-wrap"></div>', unsafe_allow_html=True)
    st.markdown('<div class="bottom-nav-row">', unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns([1, 1, 0.95, 1, 1])

    with c1:
        if st.button("❤️", key="nav_cycle", use_container_width=True):
            st.session_state.page = "tracking"
            st.rerun()

    with c2:
        if st.button("📅", key="nav_calendar", use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()

    with c3:
        if st.button("＋", key="nav_plus", use_container_width=True, type="secondary"):
            st.session_state.page = "dashboard"
            st.rerun()

    with c4:
        if st.button("🍎", key="nav_nutrition", use_container_width=True):
            st.session_state.page = "nutrition"
            st.rerun()

    with c5:
        if st.button("💬", key="nav_chat", use_container_width=True):
            st.session_state.page = "chatbot"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="bottom-space"></div>', unsafe_allow_html=True)


def show_cycle_calendar():
    st.subheader("Cycle Calendar")

    now = datetime.now()
    year = now.year
    month = now.month
    cal = calendar.monthcalendar(year, month)

    st.write(f"**{calendar.month_name[month]} {year}**")

    headers = st.columns(7)
    for i, day_name in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
        headers[i].markdown(f"**{day_name}**")

    # example highlighted days
    period_days = [2, 3, 4, 5]
    workout_days = [1, 4, 8, 11, 15, 18, 22, 25]
    food_days = [7, 8, 9, 20, 21]

    for week in cal:
        cols = st.columns(7)
        for i, day in enumerate(week):
            if day == 0:
                cols[i].write("")
            else:
                text = str(day)
                if day in period_days:
                    text += " 🩸"
                if day in workout_days:
                    text += " 🏋️"
                if day in food_days:
                    text += " 🥗"
                cols[i].info(text)


# -----------------------
# Chatbot helper functions
# -----------------------
def detect_condition(q):
    """Try to detect condition from quiz data."""
    health_flags = q.get("health_flags", [])

    # You can make this smarter later
    if "Diagnosed conditions (PCOS, etc.)" in health_flags:
        return "pcos_or_other"

    return "none"


def symptom_score(q, symptom_name):
    return q.get("symptoms", {}).get(symptom_name, 0)


def build_red_flags(q):
    flags = []

    if "History of disordered eating" in q.get("health_flags", []):
        flags.append("History of disordered eating")

    if "Low energy" in q.get("energy_flags", []):
        flags.append("Low energy")

    if "Fatigued during workouts" in q.get("energy_flags", []):
        flags.append("Fatigued during workouts")

    if q.get("sleep_quality") == "Poor":
        flags.append("Poor sleep")

    if symptom_score(q, "Fatigue") >= 4:
        flags.append("High fatigue")

    if symptom_score(q, "Cramps") >= 4:
        flags.append("High pain/cramps")

    return flags


def get_training_guidance(q, condition_label="none"):
    phase = q.get("cycle_phase", "Unsure")
    goal = q.get("main_goal", "")
    train_days = q.get("train_days", 0)
    intensity = q.get("train_intensity", "Moderate")
    fatigue = symptom_score(q, "Fatigue")
    cramps = symptom_score(q, "Cramps")
    sleep_issues = symptom_score(q, "Sleep issues")
    energy_flags = q.get("energy_flags", [])
    cycle_regularity = q.get("cycle_regularity", "Unsure")

    guidance = []
    caution = []

    # Red flag adjustments
    if "Low energy" in energy_flags or fatigue >= 4 or sleep_issues >= 4:
        caution.append("Your recovery looks limited right now, so reduce intensity or volume today.")
    if cramps >= 4:
        caution.append("Pain is high, so keep movement gentle or lower intensity if needed.")

    # PCOS path
    if condition_label == "pcos":
        guidance.append("For PCOS, consistency matters more than cycle timing.")
        guidance.append("Aim for at least 2 non-consecutive strength days per week.")
        guidance.append("A mix of resistance training plus cardio works well.")
        guidance.append("If tolerated, vigorous exercise or HIIT can be helpful, but only if it feels sustainable.")
        guidance.append("Use energy, sleep, and soreness to decide whether today should be harder or lighter.")
        return guidance, caution

    # Endometriosis path
    if condition_label == "endometriosis":
        guidance.append("For endometriosis, use symptom-driven training instead of pushing intensity.")
        guidance.append("Prioritize moderate exercise, core/lumbopelvic stability, and adequate recovery.")
        guidance.append("Avoid high-impact or very intense sessions if they make pain worse.")
        guidance.append("Yoga, mobility, pelvic-floor-informed exercise, and walking can be useful on harder days.")
        return guidance, caution

    # Irregular cycles without a clear condition
    if cycle_regularity != "Regular":
        guidance.append("Since your cycles are not regular, use symptom-based training instead of strict cycle syncing.")
        guidance.append("Keep training frequency consistent, then adjust daily intensity based on energy and symptoms.")
        guidance.append("Focus on progressive overload over weeks, not exact calendar days.")
        return guidance, caution

    # Regular cycle guidance
    if phase == "Menstrual":
        guidance.append("During the menstrual phase, keep training flexible.")
        guidance.append("Technique work, moderate loads, mobility, or lighter lifting can work well.")
        guidance.append("If symptoms are mild, you can still train. If cramps or fatigue are high, back off.")
    elif phase == "Follicular":
        guidance.append("Follicular phase can be a good time to build intensity if you feel strong.")
        guidance.append("Progressive overload, strength work, and skill work fit well here.")
    elif phase == "Ovulation":
        guidance.append("Ovulation may be a strong phase for power, speed, and heavier lifting if you feel good.")
        guidance.append("This can be a good time for higher intensity sessions.")
    elif phase == "Luteal":
        guidance.append("In the luteal phase, keep training consistent but be more flexible with volume and recovery.")
        guidance.append("Moderate-to-high intensity can still work, but fatigue may be higher later in the phase.")
    else:
        guidance.append("Use symptoms and recovery to guide training when phase is unclear.")

    if goal == "Muscle gain":
        guidance.append("For muscle gain, keep resistance training regular and prioritize recovery.")
    elif goal == "Fat loss":
        guidance.append("For fat loss, keep exercise consistent but avoid pushing hard if energy is already low.")
    elif goal == "Performance":
        guidance.append("For performance, match training intensity with recovery and fueling.")
    elif goal == "Symptom relief":
        guidance.append("For symptom relief, prioritize consistency, low stress, and symptom-guided adjustments.")

    if train_days >= 5 and (fatigue >= 4 or "Low energy" in energy_flags):
        caution.append("You train often and are reporting fatigue/low energy, so a deload or lighter day may help.")

    return guidance, caution


def get_nutrition_guidance(q, condition_label="none"):
    phase = q.get("cycle_phase", "Unsure")
    goal = q.get("main_goal", "")
    cravings = symptom_score(q, "Cravings")
    fatigue = symptom_score(q, "Fatigue")
    bloating = symptom_score(q, "Bloating")
    diet_pref = q.get("diet_pref", "No preference")
    energy_flags = q.get("energy_flags", [])

    tips = []

    if "Low energy" in energy_flags or fatigue >= 4:
        tips.append("Prioritize regular meals and do not use an aggressive calorie deficit right now.")
        tips.append("Include carbs plus protein around training to support energy.")

    if phase == "Menstrual":
        tips.append("Focus on hydration, iron-supportive foods, and easy-to-digest balanced meals.")
        tips.append("Magnesium-rich foods may help if cramps are bothering you.")
    elif phase == "Follicular":
        tips.append("Use balanced meals and fuel training well as intensity builds.")
    elif phase == "Ovulation":
        tips.append("Support performance with enough carbs, protein, and hydration.")
    elif phase == "Luteal":
        tips.append("In the luteal phase, higher satiety meals and planned snacks can help manage hunger and cravings.")
        tips.append("Magnesium-rich foods may be especially helpful here.")

    if cravings >= 4:
        tips.append("Because cravings are high, include structured snacks instead of trying to ignore hunger.")
    if bloating >= 4:
        tips.append("If bloating is high, choose simpler meals and stay hydrated.")

    if condition_label == "pcos":
        tips.append("For PCOS, consistent meals, resistance training support, and sustainable nutrition habits matter most.")
    elif condition_label == "endometriosis":
        tips.append("For endometriosis, choose a pattern that supports recovery and avoids making symptoms worse.")

    if goal == "Muscle gain":
        tips.append("Aim for protein at each meal and enough total food to recover from training.")
    elif goal == "Fat loss":
        tips.append("Use only a modest deficit, especially if symptoms or fatigue are elevated.")
    elif goal == "Performance":
        tips.append("Fuel around training, especially with carbs and protein.")

    if diet_pref == "Vegetarian":
        tips.append("Pay extra attention to iron, zinc, and protein intake.")
    elif diet_pref == "Vegan":
        tips.append("Pay extra attention to iron, B12, zinc, omega-3s, and protein intake.")

    return tips


def answer_user_question(user_message, q, condition_label="none"):
    msg = user_message.lower()

    training_guidance, cautions = get_training_guidance(q, condition_label)
    nutrition_guidance = get_nutrition_guidance(q, condition_label)
    red_flags = build_red_flags(q)

    intro = "Here's a suggestion based on your quiz profile and the rule-based plan:"

    # condition-specific keyword routing
    if "pcos" in msg:
        condition_label = "pcos"
        training_guidance, cautions = get_training_guidance(q, condition_label)
        nutrition_guidance = get_nutrition_guidance(q, condition_label)
        return {
            "title": "PCOS Support",
            "response": training_guidance[:4] + nutrition_guidance[:3],
            "cautions": cautions,
            "red_flags": red_flags,
        }

    if "endometriosis" in msg:
        condition_label = "endometriosis"
        training_guidance, cautions = get_training_guidance(q, condition_label)
        nutrition_guidance = get_nutrition_guidance(q, condition_label)
        return {
            "title": "Endometriosis Support",
            "response": training_guidance[:4] + nutrition_guidance[:3],
            "cautions": cautions,
            "red_flags": red_flags,
        }

    if any(word in msg for word in ["workout", "training", "lift", "exercise", "gym"]):
        return {
            "title": "Training Advice",
            "response": training_guidance,
            "cautions": cautions,
            "red_flags": red_flags,
        }

    if any(word in msg for word in ["food", "nutrition", "eat", "meal", "protein", "carb", "calorie"]):
        return {
            "title": "Nutrition Advice",
            "response": nutrition_guidance,
            "cautions": cautions,
            "red_flags": red_flags,
        }

    if any(word in msg for word in ["fatigue", "tired", "exhausted", "low energy"]):
        return {
            "title": "Low Energy Guidance",
            "response": [
                "Your plan should shift toward recovery today.",
                "Reduce intensity or total volume if needed.",
                "Use regular meals and include carbs + protein.",
                "Avoid aggressive dieting when fatigue is high.",
            ],
            "cautions": cautions,
            "red_flags": red_flags,
        }

    if any(word in msg for word in ["cramps", "pain", "period pain"]):
        return {
            "title": "Pain / Cramp Guidance",
            "response": [
                "Use symptom-guided training today rather than forcing a hard session.",
                "Lighter movement, walking, mobility, or easier strength work may be better.",
                "Hydration and magnesium-rich foods may help support symptom management.",
            ],
            "cautions": cautions,
            "red_flags": red_flags,
        }

    return {
        "title": "Personalized Guidance",
        "response": [intro] + training_guidance[:3] + nutrition_guidance[:3],
        "cautions": cautions,
        "red_flags": red_flags,
    }


# -----------------------
# App Pages
# -----------------------
def dashboard_page():
    st.markdown('<div class="mobile-shell">', unsafe_allow_html=True)

    # page-specific styling
    st.markdown("""
    <style>
    .top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 18px;
        margin-bottom: 14px;
    }

    .hello-text {
        font-size: 28px;
        font-family: Georgia, serif;
        color: #6f5c52;
        font-weight: 600;
    }

    .mini-chip {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.68);
        border: 1px solid rgba(255,255,255,0.75);
        color: #7d685e;
        font-size: 14px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
    }

    .hero-card {
        position: relative;
        border-radius: 30px;
        padding: 22px 20px;
        min-height: 250px;
        margin-bottom: 16px;
        background:
            radial-gradient(circle at 20% 70%, rgba(242,134,149,0.32), transparent 26%),
            radial-gradient(circle at 70% 25%, rgba(242,232,184,0.34), transparent 22%),
            radial-gradient(circle at 58% 78%, rgba(241,204,166,0.24), transparent 25%),
            linear-gradient(145deg, rgba(255,255,255,0.62), rgba(242,191,180,0.22));
        border: 1px solid rgba(255,255,255,0.75);
        box-shadow:
            0 12px 26px rgba(242, 134, 149, 0.12),
            inset 0 1px 0 rgba(255,255,255,0.85);
        overflow: hidden;
    }

    .hero-card::after {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 30px;
        background: linear-gradient(180deg, rgba(255,255,255,0.18), transparent 42%);
        pointer-events: none;
    }

    .hero-title {
        font-size: 22px;
        font-family: Georgia, serif;
        color: #6f5c52;
        margin-bottom: 6px;
        position: relative;
        z-index: 2;
    }

    .hero-big {
        font-size: 52px;
        line-height: 1;
        font-family: Georgia, serif;
        color: white;
        font-weight: 600;
        margin-bottom: 18px;
        position: relative;
        z-index: 2;
    }

    .calendar-row {
        display: flex;
        justify-content: space-between;
        text-align: center;
        margin-top: 14px;
        position: relative;
        z-index: 2;
    }

    .day-col {
        flex: 1;
        color: rgba(255,255,255,0.92);
        font-size: 13px;
        font-family: Arial, sans-serif;
    }

    .day-num {
        margin-top: 8px;
        font-size: 18px;
        color: rgba(255,255,255,0.95);
    }

    .active-day {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        margin: 8px auto 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        background:
            radial-gradient(circle at 72% 24%, rgba(255,255,255,0.7), rgba(255,255,255,0.0) 25%),
            linear-gradient(145deg, #F28695, #ee6b82);
        box-shadow: 0 6px 14px rgba(242,134,149,0.28);
    }

    .section-label {
        font-size: 18px;
        font-family: Georgia, serif;
        color: #6f5c52;
        margin: 8px 0 10px 4px;
    }

    .glass-card {
        background: rgba(255,255,255,0.56);
        border: 1px solid rgba(255,255,255,0.72);
        border-radius: 24px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.04);
    }

    .small-muted {
        color: #8a7468;
        font-size: 13px;
    }

    .main-line {
        color: #5f4e46;
        font-size: 17px;
        font-weight: 600;
        margin-top: 4px;
        margin-bottom: 8px;
    }

    .pill {
        display: inline-block;
        padding: 7px 12px;
        border-radius: 999px;
        margin: 6px 6px 0 0;
        font-size: 13px;
        color: #6f5c52;
        background: rgba(255,255,255,0.78);
        border: 1px solid #ead9d1;
    }
    </style>
    """, unsafe_allow_html=True)

    q = st.session_state.quiz_data

    st.markdown("""
        <div class="top-row">
            <div class="hello-text">Dashboard</div>
            <div class="mini-chip">ax/s</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="hero-card">
        <div class="hero-title">{q.get("cycle_phase", "Current")} phase</div>
        <div class="hero-big">August&nbsp;&nbsp;23</div>

        <div class="calendar-row">
            <div class="day-col">Tue<div class="day-num">20</div></div>
            <div class="day-col">Wed<div class="day-num">21</div></div>
            <div class="day-col">Thu<div class="day-num">22</div></div>
            <div class="day-col">Fri<div class="active-day">23</div></div>
            <div class="day-col">Sat<div class="day-num">24</div></div>
            <div class="day-col">Sun<div class="day-num">25</div></div>
            <div class="day-col">Mon<div class="day-num">26</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Today</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass-card">
        <div class="small-muted">Cycle sync</div>
        <div class="main-line">Phase: {q.get("cycle_phase", "Unsure")}</div>
        <span class="pill">Goal: {q.get("main_goal", "Not set")}</span>
        <span class="pill">Training: {q.get("training_type", "Mixed")}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="small-muted">Workout plan</div>
        <div class="main-line">Lower body + core</div>
        <span class="pill">45 min</span>
        <span class="pill">Moderate intensity</span>
        <span class="pill">Recovery-aware</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="small-muted">Nutrition</div>
        <div class="main-line">Protein + hydration focus</div>
        <span class="pill">Balanced meals</span>
        <span class="pill">Magnesium support</span>
        <span class="pill">Snack if needed</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    bottom_nav()


def tracking_page():
    st.markdown('<div class="section-title">Menstrual Tracking</div>', unsafe_allow_html=True)
    st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

    st.selectbox("Current phase", ["Menstrual", "Follicular", "Ovulation", "Luteal", "Unsure"])
    st.multiselect("Symptoms today", ["Cramps", "Fatigue", "Mood swings", "Bloating", "Cravings", "Sleep issues"])
    st.selectbox("Flow level", ["Light", "Medium", "Heavy", "N/A"])
    st.text_area("Notes")

    if st.button("Save Entry", key="save_tracking"):
        st.success("Tracking entry saved.")

    bottom_nav()


def nutrition_page():
    st.markdown('<div class="section-title">Nutrition</div>', unsafe_allow_html=True)
    st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

    st.write("### Today's Plan")
    st.write("- Breakfast: protein + fiber")
    st.write("- Lunch: carbs + protein + healthy fats")
    st.write("- Snack: yogurt / fruit / nuts")
    st.write("- Dinner: balanced meal with iron or magnesium support")

    st.write("### Key Nutrients")
    st.info("Protein")
    st.info("Iron")
    st.info("Magnesium")
    st.info("Hydration")

    bottom_nav()


def chatbot_page():
    st.markdown('<div class="section-title">Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for chat_item in st.session_state.chat_history:
        if chat_item["role"] == "user":
            st.write(f"**You:** {chat_item['content']}")
        else:
            st.write(f"**Bot:** {chat_item['content']}")

    # Input area
    msg = st.text_input("Ask something about your training, nutrition, or symptoms", key="chat_input")
    
    if st.button("Send", key="send_chat"):
        if msg.strip():
            # Get condition
            condition = detect_condition(q)
            
            # Get bot response
            response_data = answer_user_question(msg, q, condition)
            
            # Add to history
            st.session_state.chat_history.append({"role": "user", "content": msg})
            
            # Format and display bot response
            bot_response = f"**{response_data['title']}**\n\n"
            for item in response_data["response"]:
                bot_response += f"- {item}\n"
            
            if response_data["cautions"]:
                bot_response += "\n**Cautions:**\n"
                for caution in response_data["cautions"]:
                    bot_response += f"- {caution}\n"
            
            if response_data["red_flags"]:
                bot_response += "\n**Flags to note:**\n"
                for flag in response_data["red_flags"]:
                    bot_response += f"- {flag}\n"
            
            st.session_state.chat_history.append({"role": "bot", "content": bot_response})
            st.rerun()

    bottom_nav()


# -----------------------
# Onboarding Screens
# -----------------------
if not st.session_state.quiz_done:

    # Step 0: Welcome
    if st.session_state.step == 0:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.markdown('<div class="big-title">Welcome!</div>', unsafe_allow_html=True)
        st.markdown('<div class="logo">ax/s</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Register", use_container_width=True):
                st.session_state.step = 1
                st.rerun()
        with col2:
            if st.button("Login", use_container_width=True):
                st.session_state.step = 2
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    # Step 1: Register
    elif st.session_state.step == 1:
        st.markdown('<div class="section-title">Register</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        data["register_username"] = st.text_input("Username", value=data["register_username"])
        data["register_password"] = st.text_input("Password", value=data["register_password"], type="password")
        data["confirm_password"] = st.text_input("Confirm Password", value=data["confirm_password"], type="password")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_register"):
                st.session_state.step = 0
                st.rerun()
        with col2:
            if st.button("Continue", key="continue_register"):
                if not data["register_username"] or not data["register_password"] or not data["confirm_password"]:
                    st.error("Please fill in all fields.")
                elif data["register_password"] != data["confirm_password"]:
                    st.error("Passwords do not match.")
                else:
                    st.session_state.step = 3
                    st.rerun()

    # Step 2: Login
    elif st.session_state.step == 2:
        st.markdown('<div class="section-title">Login</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        data["login_username"] = st.text_input("Username", value=data["login_username"])
        data["login_password"] = st.text_input("Password", value=data["login_password"], type="password")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_login"):
                st.session_state.step = 0
                st.rerun()
        with col2:
            if st.button("Continue", key="continue_login"):
                if not data["login_username"] or not data["login_password"]:
                    st.error("Please enter username and password.")
                else:
                    st.session_state.step = 3
                    st.rerun()

    # Step 3: Basics
    elif st.session_state.step == 3:
        st.markdown('<div class="section-title">About You</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        q["age_range"] = st.selectbox("Age range", ["Under 18", "18–24", "25–34", "35–44", "45+"])
        col1, col2 = st.columns(2)
        with col1:
            q["height_cm"] = st.text_input("Height (optional)", value=q["height_cm"], placeholder="ex: 165 cm")
        with col2:
            q["weight_kg"] = st.text_input("Weight (optional)", value=q["weight_kg"], placeholder="ex: 60 kg")

        q["activity_level"] = st.radio("Activity level", ["Low", "Moderate", "High"], horizontal=True)
        q["training_type"] = st.selectbox("Training type", ["Strength", "Cardio", "Mixed", "None"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_q1"):
                st.session_state.step = 0
                st.rerun()
        with col2:
            if st.button("Next", key="next_q1"):
                st.session_state.step = 4
                st.rerun()

    # Step 4: Goals + Cycle
    elif st.session_state.step == 4:
        st.markdown('<div class="section-title">Goals & Cycle</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        q["main_goal"] = st.selectbox(
            "Main priority",
            ["Fat loss", "Muscle gain", "Performance", "Hormone balance / cycle health", "Symptom relief"]
        )
        q["cycle_regularity"] = st.radio("Are your cycles:", ["Regular", "Irregular", "Unsure"], horizontal=True)
        q["cycle_length"] = st.text_input("Average cycle length (optional)", value=q["cycle_length"], placeholder="ex: 28")
        q["cycle_phase"] = st.selectbox("Current phase", ["Unsure", "Menstrual", "Follicular", "Ovulation", "Luteal"])
        q["birth_control"] = st.radio("Hormonal birth control?", ["Yes", "No"], horizontal=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_q2"):
                st.session_state.step = 3
                st.rerun()
        with col2:
            if st.button("Next", key="next_q2"):
                st.session_state.step = 5
                st.rerun()

    # Step 5: Health + Food + Energy
    elif st.session_state.step == 5:
        st.markdown('<div class="section-title">Health & Habits</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        q["health_flags"] = st.multiselect(
            "Have you experienced any of these?",
            [
                "Missed periods",
                "Very irregular cycles",
                "Diagnosed conditions (PCOS, etc.)",
                "History of disordered eating",
            ],
            default=q["health_flags"]
        )

        q["diet_pref"] = st.selectbox("Dietary preference", ["No preference", "Vegetarian", "Vegan", "Other"])
        q["eating_pattern"] = st.radio(
            "Typical eating pattern",
            ["Regular meals", "Skipping meals", "Snacking a lot"],
            horizontal=True
        )
        q["restrictions"] = st.text_input("Any restrictions?", value=q["restrictions"], placeholder="dairy-free, gluten-free, etc.")
        q["energy_flags"] = st.multiselect(
            "Do you often feel any of these?",
            ["Low energy", "Fatigued during workouts", "Hungry all the time / not hungry at all"],
            default=q["energy_flags"]
        )

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_q3"):
                st.session_state.step = 4
                st.rerun()
        with col2:
            if st.button("Next", key="next_q3"):
                st.session_state.step = 6
                st.rerun()

    # Step 6: Symptoms
    elif st.session_state.step == 6:
        st.markdown('<div class="section-title">Symptoms</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        for symptom in q["symptoms"]:
            q["symptoms"][symptom] = st.slider(symptom, 1, 5, q["symptoms"][symptom])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_q4"):
                st.session_state.step = 5
                st.rerun()
        with col2:
            if st.button("Next", key="next_q4"):
                st.session_state.step = 7
                st.rerun()

    # Step 7: Training + Lifestyle
    elif st.session_state.step == 7:
        st.markdown('<div class="section-title">Training & Lifestyle</div>', unsafe_allow_html=True)
        st.markdown('<hr class="subtitle-line">', unsafe_allow_html=True)

        q["train_days"] = st.slider("How many days/week do you train?", 0, 7, q["train_days"])
        q["train_intensity"] = st.radio("Intensity", ["Light", "Moderate", "Intense"], horizontal=True)
        q["training_focus"] = st.radio("Main focus", ["Strength", "Endurance", "Both"], horizontal=True)
        q["sleep_quality"] = st.radio("Sleep quality", ["Good", "Okay", "Poor"], horizontal=True)
        q["stress_level"] = st.radio("Stress level", ["Low", "Medium", "High"], horizontal=True)
        q["weekly_feedback"] = st.checkbox("I'm open to adjusting my plan weekly based on feedback", value=q["weekly_feedback"])

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Back", key="back_q5"):
                st.session_state.step = 6
                st.rerun()
        with col2:
            if st.button("Finish", key="finish_quiz"):
                st.session_state.quiz_done = True
                st.session_state.page = "dashboard"
                st.rerun()

# -----------------------
# Main App After Quiz
# -----------------------
else:
    if st.session_state.page == "dashboard":
        dashboard_page()
    elif st.session_state.page == "tracking":
        tracking_page()
    elif st.session_state.page == "nutrition":
        nutrition_page()
    elif st.session_state.page == "chatbot":
        chatbot_page()




st.set_page_config(
    page_title="ax/s", 
    page_icon="🌙", 
    layout="centered",
    initial_sidebar_state="collapsed"
)
