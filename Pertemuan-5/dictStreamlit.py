import streamlit as st

st.title("Aplikasi dictionary")
st.subheader("Hitung kata dalam paragraf")

textInput = st.text_area("Masukkan paragraf", height = 200)
 
if st.button("Hitung analisis"):
    words = textInput.lower().split()
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    st.subheader("Hasil Analisis")
    st.write(count)
    st.bar_chart(count)