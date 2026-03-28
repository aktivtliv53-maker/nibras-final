import streamlit as st
import json
import re
from pathlib import Path
from collections import Counter
import plotly.graph_objects as go
from datetime import datetime

# =========================================================
# 1. إعدادات المحراب السيادي (v6.4.1 الأسطورية)
# =========================================================
st.set_page_config(
    page_title="Nibras Sovereign v6.4 — الأسطورية",
    page_icon="🜂",
    layout="wide"
)

# الأنماط البصرية المتقدمة (CSS)
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background: #0a0f0a; }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #2e7d32, #aed581); }
    .orbit-card-أزل { background: #1a1a1a; border-right: 5px solid #ffd700; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .orbit-card-سيادة { background: #1a1a1a; border-right: 5px solid #00ccff; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .orbit-card-تمكين { background: #1a1a1a; border-right: 5px solid #4caf50; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .orbit-card-وعي { background: #1a1a1a; border-right: 5px solid #9c27b0; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .orbit-card-فطرة { background: #1a1a1a; border-right: 5px solid #ff9800; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .orbit-card-يسر { background: #1a1a1a; border-right: 5px solid #00bcd4; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .energy-number { font-size: 40px; font-weight: bold; color: #4caf50; text-align: center; }
    .mentor-box { background: #001f24; border: 1px solid #00afcc; padding: 20px; border-radius: 15px; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

ORBIT_COLORS = {"أزل": "#ffd700", "سيادة": "#00ccff", "تمكين": "#4caf50", "وعي": "#9c27b0", "فطرة": "#ff9800", "يسر": "#00bcd4"}

# =========================================================
# 2. وظائف التحميل والتطبيع (الأمان السيادي)
# =========================================================
def safe_load_json(filename):
    file_path = Path(".") / filename
    if file_path.exists():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f), str(file_path)
        except: return None, None
    return None, None

def normalize_arabic(text):
    if not text: return ""
    text = re.sub(r'[\u0617-\u061A\u064B-\u0652\u0670]', '', text) # إزالة التشكيل
    replacements = {"أ":"ا", "إ":"ا", "آ":"ا", "ة":"ه", "ى":"ي", "ؤ":"و", "ئ":"ي"}
    for k, v in replacements.items(): text = text.replace(k, v)
    return text.strip()

# تحميل الملفات الخارجية
letters_raw, path_l = safe_load_json("sovereign_letters_v1.json")
lexicon_raw, path_x = safe_load_json("nibras_lexicon.json")

# بناء فهرس الحروف
letters_idx = {normalize_arabic(item["letter"]): item for item in letters_raw if "letter" in item} if letters_raw else {}

# =========================================================
# 3. محرك التحليل الراداري والجذري
# =========================================================
def analyze_path(text, l_idx, x_raw):
    norm = normalize_arabic(text)
    res = {"mass": 0.0, "speed": 0.0, "orbit": "غير_مرصود", "energy": 0.0, "insight": "لا توجد بصيرة.", "direction": "غير محدد", "count": 0, "matched_roots": []}
    
    # تحليل الحروف
    clean_text = norm.replace(" ", "")
    for char in clean_text:
        meta = l_idx.get(char)
        if meta:
            res["mass"] += float(meta.get("mass", 0))
            res["speed"] += float(meta.get("speed", 0))
            res["count"] += 1
            res["direction"] = meta.get("direction", "غير محدد")

    # تحليل الجذور والمدارات
    if isinstance(x_raw, list):
        words = norm.split()
        for word in words:
            for block in x_raw:
                orbit_name = block.get("orbit", "مجهول")
                for r in block.get("roots", []):
                    r_name = normalize_arabic(r.get("name", ""))
                    if r_name == word or (len(word) >= 3 and r_name == word[:3]):
                        res["orbit"] = orbit_name
                        res["energy"] += float(r.get("weight", 0))
                        res["insight"] = r.get("insight", "")
                        res["matched_roots"].append(r_name)
                        break

    res["total"] = round((res["mass"] + res["speed"]) * 0.5 + res["energy"] * 2, 2)
    return res

# =========================================================
# 4. واجهة المستخدم (المحراب)
# =========================================================
st.title("🜂 محراب نبراس السيادي v6.4")
st.sidebar.title("🛠️ لوحة الرصد")
st.sidebar.write(f"الحروف المفهرسة: {len(letters_idx)}")
st.sidebar.write(f"حالة المدارات: {'✅ متصل' if lexicon_raw else '❌ مفقود'}")

col1, col2, col3 = st.columns(3)
with col1: t1 = st.text_area("📍 المسار الأول", height=100, key="v1")
with col2: t2 = st.text_area("📍 المسار الثاني", height=100, key="v2")
with col3: t3 = st.text_area("📍 المسار الثالث", height=100, key="v3")

if st.button("🚀 إطلاق الرصد السيادي المقارن", use_container_width=True):
    inputs = [t1, t2, t3]
    results = []
    
    res_cols = st.columns(3)
    for i, txt in enumerate(inputs):
        if txt.strip():
            res = analyze_path(txt, letters_idx, lexicon_raw)
            results.append(res)
            with res_cols[i]:
                orbit_class = f"orbit-card-{res['orbit']}" if res['orbit'] in ORBIT_COLORS else "orbit-card-وعي"
                st.markdown(f"""<div class='{orbit_class}'><h3 style='text-align:center;'>المسار {i+1}</h3>
                <div class='energy-number'>{res['total']}</div>
                <p style='text-align:center;'><b>المدار:</b> {res['orbit']}</p></div>""", unsafe_allow_html=True)
                st.caption("🌊 الكتلة والسرعة")
                st.progress(min((res['mass']+res['speed'])/200, 1.0))
        else: results.append(None)

    # الرادار البياني
    if any(results):
        st.markdown("---")
        fig = go.Figure()
        for i, r in enumerate(results):
            if r:
                fig.add_trace(go.Scatterpolar(
                    r=[r['mass'], r['speed'], r['energy']*10, r['count'], r['total']/10],
                    theta=['الكتلة','السرعة','طاقة الجذور','عدد الحروف','القوة الكلية'],
                    fill='toself', name=f"المسار {i+1} ({r['orbit']})"
                ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

        # المستشار
        best = max([r for r in results if r], key=lambda x: x["total"])
        st.markdown(f"<div class='mentor-box'><h3>🧠 المستشار السيادي</h3>"
                    f"<p><b>المسار الغالب:</b> مدار {best['orbit']}</p>"
                    f"<p><b>البصيرة:</b> {best['insight']}</p></div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("رونبي، السويد | 58-58")
st.sidebar.write("خِت فِت.")