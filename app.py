import streamlit as st
import plotly.graph_objects as go

# نبراس v11.0 - كود الإنقاذ الذاتي
st.set_page_config(page_title="Nibras Sovereign", layout="wide")

# دمج البيانات السيادية داخل الكود (لضمان عمل الرابط فوراً)
SOVEREIGN_ROOTS = {
    "علم": {"تكرار": 854, "طاقة": 5, "وعي": 5, "مقام": 5, "أثر": 5},
    "نور": {"تكرار": 43, "طاقة": 5, "وعي": 5, "مقام": 4, "أثر": 5},
    "كتب": {"تكرار": 319, "طاقة": 4, "وعي": 4, "مقام": 3, "أثر": 4},
    "روح": {"تكرار": 21, "طاقة": 5, "وعي": 5, "مقام": 5, "أثر": 5}
}

st.title("🛡️ محراب نبراس: التمكين المباشر")

# واجهة الرصد
target = st.text_input("أدخل الكلمة للرصد (جرب: علم، نور، روح):", "").strip()

if target:
    if target in SOVEREIGN_ROOTS:
        st.success(f"✅ تم رصد المدار السيادي لـ: {target}")
        val = SOVEREIGN_ROOTS[target]
        
        # رسم رادار البصيرة
        fig = go.Figure(data=go.Scatterpolar(
            r=[val['طاقة'], val['وعي'], val['مقام'], val['أثر'], val['طاقة']],
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
        st.warning(f"⚠️ الكلمة '{target}' قيد المعالجة في المدارات المقلوبة.")

st.markdown("---")
st.caption("خِت فِت | العودة للمنبع السيادي v11.0")
