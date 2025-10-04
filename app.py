import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image

st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")
st.header("🔭 J. Webb Space Telescope vs Hubble Telescope")

st.write(
    """
    Discover the universe side-by-side with the James Webb and Hubble Space Telescopes.<br>
    Effortlessly compare stunning images and experience the evolution of cosmic observation.<br>
    <br>
    This visualization is inspired by [WebbCompare](https://www.webbcompare.com/index.html), reimagined for Streamlit.
    """
)

st.markdown("### NGC 346")
img1 = Image.open("hubble_ngc346.png")
img2 = Image.open("webb_ngc346.png")
image_comparison(
    img1=img1,
    img2=img2,
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Sombrero Galaxy")
img3 = Image.open("sombrero_hubble.png")
img4 = Image.open("sombrero_webb.png")
image_comparison(
    img1=img3,
    img2=img4,
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Galaxies IC 2163 and NGC 2207")
img5 = Image.open("Galaxies IC 2163 and NGC 2207_hubble.png")
img6 = Image.open("Galaxies IC 2163 and NGC 2207_webb.png")
image_comparison(
    img1=img5,
    img2=img6,
    label1="Hubble",
    label2="Webb",
)
