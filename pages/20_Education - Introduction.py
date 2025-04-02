import streamlit as st

st.title("Education: The Cornerstone of a Healthy individual")

st.write(
    """
    Welcome to an exploration of how education shapes the health and well-being of ASEAN nations. This project delves into the intricate connections between education,
    healthcare, and life expectancy, highlighting the transformative power of investing in human capital.

    We examine key indicators such as literacy rates, primary school enrolment, and immunization coverage, and analyze their impact on health outcomes.
    Through data-driven insights, we aim to demonstrate the importance of education in empowering individuals, strengthening healthcare systems, and building a healthier future for the ASEAN region.
    """
)

st.write(
    """
    Join us on a journey through the following sections:
    
    * **Life Expectancy:** Explore the relationship between education and life expectancy, and uncover factors that contribute to longer, healthier lives.
    * **Literacy Rates:** Discover how literacy empowers individuals and strengthens communities.
    * **Immunization:** Examine the link between education and immunization rates, and how they collectively contribute to healthier communities.
    * **Primary School Enrolment:** Understand the crucial role of primary education in laying the foundation for health literacy and better healthcare access.
    * **Conclusion:** Reflect on the key findings and the transformative power of education in shaping a healthier future for ASEAN.

    Let's embark on this exploration together and discover how education can pave the way for a healthier, more prosperous ASEAN.
    """
)


st.markdown("---")
col1, col2 = st.columns([4, 1])
with col1:
    if st.button("< Previous Page"):
           st.switch_page("pages/17_Life expectancy - Healthcare expenditure Conclusion.py")
    # This is the subtitle (not clickable)
    st.caption("Life expectancy - Healthcare expenditure Conclusion.")
with col2:
    # This makes "Next Article >" clickable
    if st.button("Next Page >"):
           st.switch_page("pages/21_Education - Life Expectancy.py")
    # This is the subtitle (not clickable)
    st.caption("Education - Life Expectancy")
