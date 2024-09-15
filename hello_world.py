import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import fitz
from PIL import Image
import io
 
# st.write(
#     """
#     # Ini Aplikasi Pertamaku
#     Hello, para calon praktisi data masa depan!
#     """
# )
# #Judul
# st.title('Ini Judul Belajar Analisis Data')

# #Header
# st.header('Ini Header Pengembangan Dashboard')

# #subheader
# st.subheader('Ini Subheader Pengembangan Dashboard')

#Untuk menulis sesuatu ditambah dengan efek hiasan, kayak bold, italic, etc
st.markdown(
    """
    # My first app (Ini Markdown)
    My name is Darmawan Setyaputra purba!
    """
)

#Ini text biasa
st.text('Halo, sekarang kita belajar widget.')

#Menampilkan kolom input
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

#Menampilkan kolom input untuk multi line
text = st.text_area('Feedback')
st.write('Feedback: ', text)

#Menampilkan kolom input angka
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

#Menampilkan kolom tanggal
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

#Menambah fitur upload file csv
uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)


# #Menambah fitur upload file pdf
# uploaded_file2 = st.file_uploader("Choose a PDF file", type="pdf")

# if uploaded_file2:
#     #Menampilkan sebagai text
#     # Open the uploaded PDF file
#     pdf_document = fitz.open(stream=uploaded_file2.read(), filetype="pdf")

#     # # Iterate through pages and extract text
#     # for page_num in range(pdf_document.page_count):
#     #     page = pdf_document.load_page(page_num)
#     #     text = page.get_text("text")
#     #     st.write(f"### Page {page_num + 1}")
#     #     st.text(text)

#     # Iterate through pages and convert to images
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document.load_page(page_num)
#         pix = page.get_pixmap()  # Render page to an image

#         # Convert to a PIL image
#         img = Image.open(io.BytesIO(pix.tobytes("png")))

#         # Display the image
#         st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)

# #Mengambil input berupa gambar
# picture = st.camera_input('Take a picture')
# if picture:
#     st.image(picture)

#Button Widgets
#Clickable Button
if st.button('Say hello'):
    st.write('Hello there')

#Checkbox
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

#Radio Button
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

#Selection Box
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

#Multi Selection Box
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

#Slider
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)

# #Nampilin histogram
# x = np.random.normal(15, 5, 250)
# fig, ax = plt.subplots()
# ax.hist(x=x, bins=15)
# st.pyplot(fig)

# #Rumus matematika
# st.latex(r"""
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
# """)

# st.subheader('Data Frame')

# #Nampilin Data Frame
# df = pd.DataFrame({
#     'c1': [1, 2, 3, 4],
#     'c2': [10, 20, 30, 40],
# })

# st.dataframe(data=df, width=500, height=150)

# st.write(pd.DataFrame({
#     'c1': [1, 2, 3, 4],
#     'c2': [10, 20, 30, 40],
# }))


# st.subheader('Tabel')
# #Nampilin tabel
# df2 = pd.DataFrame({
#     'c1': [1, 2, 3, 4],
#     'c2': [10, 20, 30, 40],
# })
# st.table(data=df2)

# #Mau masukin bahasa lain ke streamlit
# code = """def hello():
#     print("Hello, Streamlit!")"""
# st.code(code, language='python')

# #Metrik
# st.subheader('Metric')
# st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# #Menampilkan data json
# st.subheader('JSON')
# st.json({
#     'c1': [1, 2, 3, 4],
#     'c2': [10, 20, 30, 40],
# })

st.caption('Ini Caption Copyright (c) 2023')




