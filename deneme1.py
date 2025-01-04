import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import random

# Uygulama başlığı ve açıklama
st.title("Tütün Alanı Sınıflandırma Uygulaması")
st.markdown("""
Bu uygulama, verilen konum bilgilerine dayanarak alanların tütün ekimi için uygun olup olmadığını sınıflandırır. 
Ayrıca harita üzerinden interaktif olarak seçim yapabilir ve farklı ürün tiplerini inceleyebilirsiniz.
""")

# Ürün seçimi
st.sidebar.header("Ürün Seçimi")
product_options = ["Tütün", "Buğday", "Mısır", "Pamuk"]
selected_product = st.sidebar.selectbox("Ürün Türünü Seçin:", product_options)
st.sidebar.write(f"Seçilen ürün: {selected_product}")

# Harita oluşturma
st.header("Harita Üzerinden Konum Seçimi")
m = folium.Map(location=[38.0, 38.2], zoom_start=12)

# Örnek veriler
example_locations = [
    {"name": "Konum 1", "coordinates": [38.0260, 38.2176], "label": random.choice(["Tütün", "Diğer"])},
    {"name": "Konum 2", "coordinates": [38.0334, 38.2501], "label": random.choice(["Tütün", "Diğer"])},
    {"name": "Konum 3", "coordinates": [38.0312, 38.2465], "label": random.choice(["Tütün", "Diğer"])},
]

# Haritaya işaretler ekleme
for location in example_locations:
    label_color = "green" if location["label"] == "Tütün" else "red"
    folium.Marker(
        location=location["coordinates"],
        popup=f"{location['name']} - {location['label']}",
        icon=folium.Icon(color=label_color),
    ).add_to(m)

# Haritayı gösterme
st_data = st_folium(m, width=700, height=500)

# Konum bilgisi girdisi
st.subheader("Manuel Konum Girişi ve Sınıflandırma")
latitude = st.number_input("Enlem Girin:", value=38.0, step=0.01)
longitude = st.number_input("Boylam Girin:", value=38.2, step=0.01)

if st.button("Sınıflandır"):
    # Örnek bir sınıflandırma mantığı
    is_tobacco = random.choice([True, False])  # Gerçek sınıflandırma modeliniz burada kullanılabilir
    result = "Tütün Alanı" if is_tobacco else "Diğer"
    st.success(f"Bu konum: {result}")

# Özet rapor bölümü
st.subheader("Sonuç ve Özet")
st.markdown("""
- Seçilen ürün: **{product}**
- Tespit edilen alanlar haritada işaretlenmiştir.
- Verilen konum bilgisine göre sınıflandırma yapılmıştır.
""".format(product=selected_product))
