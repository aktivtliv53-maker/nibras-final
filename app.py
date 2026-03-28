import streamlit as st
import plotly.graph_objects as go
import json
import os

# إعدادات المحراب السيادي
st.set_page_config(page_title="Nibras Sovereign v8.0", layout="wide")

def load_data(file_name, default_data):
    # محاولة التحميل من الملف الخارجي أولاً
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return default_data
    return default_data

# بيانات الطوارئ (تفعيل البصيرة فوراً في حال فقدان الملف)
emergency_roots = {
    "علم": {"تكرار": 854, "مقام": "علوي", "طاقة": 5},
    "نور": {"تكرار": 43, "مقام": "متوسط", "طاقة": 5},
    "كتب": {"تكرار": 319, "مقام": "أرضي", "طاقة": 4}
}

st.title("🛡️ محراب نبراس: التمكين السيادي")

# فحص الاتصال بالبيانات
roots = load_data('quran_roots_complete.json', emergency_roots)

target_word = st.text_input("أدخل الكلمة أو الجذر للرصد (جرب: علم أو نور):", "")

if target_word:
    if target_word in roots:
        st.success(f"✅ تم رصد المدار المقلوب لـ: {target_word}")
        
        # هندسة الرادار (البصيرة)
        data = roots[target_word]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[data.get('طاقة', 3), 4, 5, 3],
            theta=['طاقة', 'وعي', 'مقام', 'أثر'],
            fill='toself',
            name='بصيرة المسار'
        ))
        
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])))
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ المسار لم يُرصد في قاعدة البيانات الحالية.")

st.markdown("---")
st.caption("بعلم مكين نسخر خلاصة التمكين | نبرأس v8.0")
