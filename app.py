import streamlit as st
import plotly.graph_objects as go
import json
import os

# نبراس السيادي v13.0 - الصياد الماهر والبنية الكاملة
st.set_page_config(page_title="Nibras Sovereign", layout="wide")

def hunt_file(file_name):
    """صياد ملفات ذكي يبحث في كل المدارات الممكنة"""
    paths_to_scan = [
        os.path.join(os.path.dirname(__file__), 'data', file_name), # المجلد الجديد (الاحترافي)
        os.path.join(os.path.dirname(__file__), file_name),        # الجذر (الماين)
        file_name,                                                 # المسار المباشر
        f"./data/{file_name}"                                     # المسار النسبي
    ]
    for path in paths_to_scan:
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                continue
    return None

# تحميل "البصيرة" (الجذور والمعجم)
roots_data = hunt_file('quran_roots_complete.json')
lexicon_data = hunt_file('nibras_lexicon.json')

st.title("🛡️ محراب نبراس: التمكين الكامل")
st.markdown("---")

# واجهة الرصد السيادية
target = st.text_input("أدخل الجذر للرصد (مثال: علم، نور، روح):", "").strip()

if target:
    if roots_data and target in roots_data:
        st.success(f"✅ تم رصد المدار السيادي لـ: {target}")
        val = roots_data[target]
        
        # رسم رادار البصيرة (الهندسة الرمزية)
        fig = go.Figure(data=go.Scatterpolar(
            r=[val.get('طاقة', 3), val.get('وعي', 4), val.get('مقام', 5), val.get('أثر', 4), val.get('طاقة', 3)],
            theta=['طاقة', 'وعي', 'مقام', 'أثر', 'طاقة'],
            fill='toself',
            fillcolor='rgba(0, 255, 204, 0.3)',
            line=dict(color='#00FFCC', width=2)
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 5], gridcolor="#444"),
                angularaxis=dict(gridcolor="#444")
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white", size=14),
            showlegend=False,
            margin=dict(l=40, r=40, t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # عرض بصيرة المعجم إذا وجدت
        if lexicon_data and target in lexicon_data:
            with st.expander("📖 بصيرة المعجم السيادي", expanded=True):
                st.info(lexicon_data[target])
    else:
        if not roots_data:
            st.error("❌ الصياد لم يجد ملف 'quran_roots_complete.json'. تأكد من وجوده في مجلد data.")
        else:
            st.warning(f"⚠️ المدار '{target}' غير مرصود حالياً في قاعدة البيانات.")

st.markdown("---")
st.caption("خِت فِت | بنية مكتملة v13.0")
