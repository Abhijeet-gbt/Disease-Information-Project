import streamlit as st

# ---------------- HOME PAGE ---------------- #

st.set_page_config(page_title="Disease Information Project")

st.title("🩺 Disease Information and Precautions")
st.write("### Created by Abhijeet Jagtap")

st.write("""
Welcome to the Disease Information Project.

This project provides:
- Information about diseases
- Causes of diseases
- Common symptoms
- Important precautions

Select any disease from the sidebar and click the button to view details.
""")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("Diseases")

disease = st.sidebar.selectbox(
    "Select Disease",
    ["Diabetes", "Stomach Cancer", "Malaria", "Typhoid"]
)

show = st.sidebar.button("Show Information")

# ---------------- DIABETES ---------------- #

if show:

    if disease == "Diabetes":

        st.header("Diabetes")

        st.subheader("What is Diabetes?")
        st.write("""
Diabetes is a disease in which the body cannot properly control blood sugar levels.
Normally, insulin helps glucose move into body cells for energy.
In diabetes, the body either does not make enough insulin or cannot use it properly.
""")

        st.subheader("Common Symptoms")
        st.write("""
- Frequent urination  
- Excessive thirst  
- Increased hunger  
- Weakness and fatigue  
- Weight loss  
- Blurred vision  
""")

        st.subheader("Precautions")
        st.write("""
- Eat healthy and balanced food  
- Avoid excessive sugar and junk food  
- Exercise daily  
- Maintain healthy body weight  
- Drink plenty of water  
- Avoid smoking and alcohol  
- Get proper sleep  
- Monitor blood sugar regularly  
""")

# ---------------- STOMACH CANCER ---------------- #

    elif disease == "Stomach Cancer":

        st.header("Stomach Cancer")

        st.subheader("What is Stomach Cancer?")
        st.write("""
Stomach cancer is a disease in which harmful cells grow uncontrollably in the stomach lining.
It is also called gastric cancer.
""")

        st.subheader("Why It Happens")
        st.write("""
- Smoking  
- Excess alcohol consumption  
- Oily and processed food  
- Helicobacter pylori infection  
- Family history  
- Obesity and unhealthy lifestyle  
""")

        st.subheader("Common Symptoms")
        st.write("""
- Stomach pain  
- Acidity and indigestion  
- Weight loss  
- Loss of appetite  
- Nausea and vomiting  
""")

        st.subheader("Precautions")
        st.write("""
- Eat fruits and vegetables daily  
- Avoid smoking and alcohol  
- Reduce salty and processed food  
- Exercise regularly  
- Maintain healthy lifestyle  
- Regular medical checkups  
""")

# ---------------- MALARIA ---------------- #

    elif disease == "Malaria":

        st.header("Malaria")

        st.subheader("What is Malaria?")
        st.write("""
Malaria is a serious disease caused by parasites and spread through infected mosquito bites.
""")

        st.subheader("Why It Happens")
        st.write("""
- Mosquito bites  
- Dirty surroundings  
- Stagnant water  
- Lack of cleanliness  
""")

        st.subheader("Common Symptoms")
        st.write("""
- High fever  
- Chills and shivering  
- Sweating  
- Headache  
- Weakness  
""")

        st.subheader("Precautions")
        st.write("""
- Use mosquito nets  
- Apply mosquito repellents  
- Keep surroundings clean  
- Avoid stagnant water  
- Wear full sleeve clothes  
""")

# ---------------- TYPHOID ---------------- #

    elif disease == "Typhoid":

        st.header("Typhoid")

        st.subheader("What is Typhoid?")
        st.write("""
Typhoid is a bacterial infection caused by Salmonella Typhi bacteria.
It spreads through contaminated food and water.
""")

        st.subheader("Why It Happens")
        st.write("""
- Drinking contaminated water  
- Eating unhygienic food  
- Poor sanitation  
- Lack of hand washing  
""")

        st.subheader("Common Symptoms")
        st.write("""
- High fever  
- Weakness  
- Headache  
- Stomach pain  
- Vomiting  
""")

        st.subheader("Precautions")
        st.write("""
- Drink boiled water  
- Wash hands before eating  
- Eat hygienic food  
- Maintain cleanliness  
- Get vaccinated  
""")

        st.success("Stay healthy and safe!")