import streamlit as st

# Conclusion Page
st.title("📌 Conclusion")

st.markdown("""
### In a Nutshell  
Our research points out the effectiveness of **strategic immunization investment** as a means of containing infectious diseases.  

Decrease in disease cases **often correlates** with higher vaccination spending, but the true effect depends on **how efficiently resources are used** rather than just the amount of money spent.
""")

# Key Takeaways
st.subheader("🔑 Key Takeaways for this Research")

st.markdown("""
- **Effective Resource Allocation Matters:**  
  Even though numerous countries spend a lot of money on vaccination, some, like **Myanmar**, have seen notable drops in disease cases with **relatively modest expenditure**.  
  
  This indicates that targeted intervention strategies and **efficient allocation** can occasionally outperform sheer spending volume.

- **Learning from Myanmar:**  
  Myanmar's was able to show impressive outcomes can also be achieved with a well-thought-out immunization strategy that emphasizes **community engagement, streamlined supply chains, and robust vaccination outreach**.  

  Despite spending considerably fewer resources than some of its regional peers, Myanmar was able to **effectively drive down disease prevalence** , making their own country a **Role Model** for others in resource optimization.
""")

st.subheader("🚀 Call to Action for Singapore’s Healthcare Policymakers")

st.markdown("""
  For healthcare policymakers in **Singapore**, these insights are particularly persuasive. By examining and follow behinds Myanmar's footstep, Singapore can consider:

  ✅ **Adopting more efficient vaccination distribution method** such as having more targeted community interventions.  
  ✅ **Leveraging Data-Driven Decision-Making** to identify and address gaps in immunization outreach.  
  ✅ **Optimizing existing resources** to further reduce the burden of infectious diseases.  

Ultimately, immunization is just merely an expense—it is a **critical investment in public health and economic stability**.  
""")

st.markdown("""
By **learning from successful Role Models** such as Myanmar, and tailoring these strategies to local context, Singapore could **strengthen its healthcare framework** and **safeguard its population** against preventable diseases.
""")
st.markdown("---")
col1, col2 = st.columns([4, 1])
with col1:
    if st.button("< Previous Page"):
        st.switch_page("pages/31_Disease Rates - Analysis Page.py")

    # This is the subtitle (not clickable)
    st.caption("Disease Rates - Analysis Page.")
