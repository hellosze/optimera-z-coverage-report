import streamlit as st

st.set_page_config(
    page_title="Optimera Z Coverage Report Generator",
    page_icon="📂",
    layout="centered"
)

st.title("📂 Optimera Z Coverage Report Generator")

st.write(
    "Upload two files below. This app can be used to compare or process them."
)

# File uploaders
file1 = st.file_uploader("Upload First File", type=None)
file2 = st.file_uploader("Upload Second File", type=None)

st.divider()

# Display file info
if file1:
    st.subheader("First File")
    st.write("Filename:", file1.name)
    st.write("Size:", file1.size, "bytes")

if file2:
    st.subheader("Second File")
    st.write("Filename:", file2.name)
    st.write("Size:", file2.size, "bytes")

# Action button
if file1 and file2:
    if st.button("Process Files"):

        data1 = file1.read()
        data2 = file2.read()

        st.success("Files successfully loaded!")

        st.subheader("Preview")

        st.write("First file first 200 bytes:")
        st.code(data1[:200])

        st.write("Second file first 200 bytes:")
        st.code(data2[:200])

        st.info("Add your processing logic here.")