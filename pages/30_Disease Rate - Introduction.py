import streamlit as st

# Page configuration
st.set_page_config(page_title="Introduction - Immunization & Disease Analysis", layout="wide")
st.title("📢 Introduction: A study of the relationship between infectious diseases and vaccination rates")

st.markdown("""
### 🌍 Background Information
Immunization is crucial for reducing the risk of infectious diseases and enhancing general health. Vaccination programs receive substantial funding from governments around the world, although the results of these expenditures vary greatly from nation to nation.

This dashboard aims look into the relationship between **immunization expenditure** and **infectious disease cases** in ASEAN countries, providing insights into whether increased funding leads to better disease control.

### 🎯 Main Objectives of the Research
- Understand **Global and Regional Immunization trend**
- Identify **patterns in Vaccination Expenditure and Disease Prevalence**
- Analyze whether **Higher Expenditures correlates in reducing disease cases**
- Provide **Data-Driven Insight for Policymakers and Healthcare Strategist**

### 🏥 Why Does This Matter?
- **For Policymakers**: Helps to optimize healthcare budgets for maximum disease control.
- **For Researchers**: Provides a data-driven approach to study healthcare interventions.
- **For Investors & Medical Industries**: Identifies trends in healthcare spending and disease management.

---

### 🔍 Key Research Question Explored:
1️⃣ How has immunization expenditure has evolved over time?  
2️⃣ Do countries with higher expenditure see a greater reduction in infectious diseases?  
3️⃣ What lessons can be drawn from the ASEAN region's immunization efforts?  

Use the navigation menu to explore the **analysis and findings** of this study.
""")
st.markdown("---")
col1, col2 = st.columns([4, 1])
with col1:
    if st.button("< Previous Page"):
           st.switch_page("pages/25_Education - Conclusion.py")

    # This is the subtitle (not clickable)
    st.caption("Education - Conclusion")
with col2:
    # This makes "Next Article >" clickable
    if st.button("Next Page >"):
           st.switch_page("pages/31_Disease Rates - Analysis Page.py")

    # This is the subtitle (not clickable)
    st.caption("Disease Rates - Analysis Page")
