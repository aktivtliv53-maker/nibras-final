import streamlit as st
import plotly.graph_objects as go
import json
import os

# نبراس السيادي v10.3 - الرابط الشعبي الموحد
st.set_page_config(page_title="Nibras Final", layout="wide")

def load_data(file_name):
    # المسار المعتمد بعد تنظيم كوبيلوت (داخل مجلد data)
    path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

# تحميل البيانات (الجذور)
roots = load_data('quran_roots_complete.json')

st.title("🛡️ محراب نبراس: الرصد الشعبي")

target = st.text_input("أدخل الجذر للرصد (جرب: علم، نور):", "").strip()

if target:
    if roots and target in roots:
        st.success(f"✅ تم رصد المدار: {target}")
        val = roots[target]
        fig = go.Figure(data=go.Scatterpolar(
            r=[val.get('طاقة', 3), 4, 5, 4, val.get('طاقة', 3)],
            theta=['طاقة', 'وعي', 'مقام', 'أثر', 'طاقة'],
            fill='toself',
            line=dict(color='#00FFCC')
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ المسار غير مرصود في قاعدة بيانات المجلد data.")

st.caption("خِت فِت | التمكين عبر التنظيم السيادي")
