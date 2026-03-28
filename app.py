import streamlit as st
import plotly.graph_objects as go

# إعدادات المحراب السيادي v9.0
st.set_page_config(page_title="Nibras Sovereign v9.0", layout="wide")

# قاعدة بيانات سيادية مدمجة (لا تحتاج لملفات خارجية)
NIBRAS_DATA = {
    "علم": {"تكرار": 854, "طاقة": 5, "وعي": 5, "مقام": 5, "أثر": 5, "تعريف": "انكشاف الحقائق بالبصيرة"},
    "نور": {"تكرار": 43, "طاقة": 5, "وعي": 5, "مقام": 4, "أثر": 5, "تعريف": "ظهور الذات في مرائي الصفات"},
    "كتب": {"تكرار": 319, "طاقة": 4, "وعي": 4, "مقام": 3, "أثر": 4, "تعريف": "تثبيت الوجود في لوح التقدير"},
    "روح": {"تكرار": 21, "طاقة": 5, "وعي": 5, "مقام": 5, "أثر": 5, "تعريف": "أمر الله الساري في الكائنات"}
}

st.title("🛡️ محراب نبراس: التمكين السيادي v9.0")
st.subheader("الرصد المباشر - البصيرة المدمجة")

target_word = st.text_input("أدخل الكلمة للرصد (جرب: علم، نور، روح):", "").strip()

if target_word:
    if target_word in NIBRAS_DATA:
        st.success(f"✅ تم الرصد السيادي للمدار: {target_word}")
        data = NIBRAS_DATA[target_word]
        
        # رسم رادار البصيرة
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[data['طاقة'], data['وعي'], data['مقام'], data['أثر'], data['طاقة']],
            theta=['طاقة', 'وعي', 'مقام', 'أثر', 'طاقة'],
            fill='toself',
            line=dict(color='#00FFCC'),
            name=f'مدار {target_word}'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            paper_bgcolor="#0E1117",
            font=dict(color="white")
        )
        st.plotly_chart(fig)
        
        st.info(f"📖 بصيرة الحرف: {data['تعريف']}")
    else:
        st.warning(f"⚠️ الكلمة '{target_word}' غير مدمجة في هذه النسخة. جرب الكلمات السيادية: علم، نور، روح.")

st.markdown("---")
st.caption("خِت فِت | بعلم مكين نسخر خلاصة التمكين")
