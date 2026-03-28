import streamlit as st
import plotly.graph_objects as go
import json
import os

# نبراس v12.0 - البروتوكول الشامل (مقاومة الانهيار)
st.set_page_config(page_title="Nibras Sovereign", layout="wide")

def safe_load(file_name):
    # مصفوفة البحث: يبحث في المجلد الجديد، ثم القديم، ثم يتوقف بسلام
    paths = [
        os.path.join(os.path.dirname(__file__), 'data', file_name),
        os.path.join(os.path.dirname(__file__), file_name)
    ]
    for path in paths:
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                continue
    return None

# محاولة تحميل البيانات دون إيقاف النظام
roots = safe_load('quran_roots_complete.json')

st.title("🛡️ محراب نبراس: التمكين السيادي")

# فحص الحالة التقنية للمحراب بصمت
if roots is None:
    st.warning("⚠️ النظام يعمل بوضع 'البصيرة الداخلية' (الملفات الخارجية غير متصلة).")
    # بيانات داخلية أساسية لضمان عدم توقف التطبيق
    roots = {"علم": {"تكرار": 854, "طاقة": 5, "وعي": 5, "مقام": 5, "أثر": 5}}

target = st.text_input("أدخل الجذر للرصد (جرب: علم):", "").strip()

if target:
    if target in roots:
        st.success(f"✅ تم رصد المدار: {target}")
        val = roots[target]
        fig = go.Figure(data=go.Scatterpolar(
            r=[val.get('طاقة', 3), val.get('وعي', 4), val.get('مقام', 5), val.get('أثر', 4), val.get('طاقة', 3)],
            theta=['طاقة', 'وعي', 'مقام', 'أثر', 'طاقة'],
            fill='toself',
            line=dict(color='#00FFCC')
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            paper_bgcolor="#0E1117",
            font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🔄 المدار مطلوب رصده في التحديث القادم.")

st.markdown("---")
st.caption("خِت فِت | v12.0 بروتوكول استعادة النظام")
