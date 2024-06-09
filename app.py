import streamlit as st
st.set_page_config(page_title="portfolio",page_icon="🌐",layout="wide")
from streamlit.components.v1 import html
from PIL import Image
import base64
def load_css(file_path):
    with open(file_path, "r") as f:
        return f"<style>{f.read()}</style>"

# Load and inject CSS
css = load_css("style.css")
st.markdown(css, unsafe_allow_html=True)
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(45deg, #ffecd1, #d1ecff, #fff9d1, #e0e0e0);
        background-size: 800% 800%;
        animation: gradientAnimation 30s ease infinite;
    }}

    @keyframes gradientAnimation {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)


salina_regular_font = base64.b64encode(open("s1.otf", "rb").read()).decode()
salina_italic_font = base64.b64encode(open("s2.otf", "rb").read()).decode()
salina_font_styles = f"""
    @font-face {{
        font-family: 'Salina';
        font-style: normal;
        font-weight: 400;
        src: url('data:font/truetype;charset=utf-8;base64,{salina_regular_font}') format('truetype');
    }}
    @font-face {{
        font-family: 'Salina';
        font-style: italic;
        font-weight: 400;
        src: url('data:font/truetype;charset=utf-8;base64,{salina_italic_font}') format('truetype');
    }}
    .salina-font {{
        font-family: 'Salina', sans-serif;
        text-align: center;
        font-size: 36px; /* Increase the font size as desired */
    }}
"""


col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp1.png'))
html_component_1 = """
<div class="social-buttons">
  <a href= 'https://github.com/yashsarnaik' target="_blank" class="social-button github">
    <svg class="cf-icon-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-2.5 0 19 19"><path d="M9.464 17.178a4.506 4.506 0 0 1-2.013.317 4.29 4.29 0 0 1-2.007-.317.746.746 0 0 1-.277-.587c0-.22-.008-.798-.012-1.567-2.564.557-3.105-1.236-3.105-1.236a2.44 2.44 0 0 0-1.024-1.348c-.836-.572.063-.56.063-.56a1.937 1.937 0 0 1 1.412.95 1.962 1.962 0 0 0 2.682.765 1.971 1.971 0 0 1 .586-1.233c-2.046-.232-4.198-1.023-4.198-4.554a3.566 3.566 0 0 1 .948-2.474 3.313 3.313 0 0 1 .091-2.438s.773-.248 2.534.945a8.727 8.727 0 0 1 4.615 0c1.76-1.193 2.532-.945 2.532-.945a3.31 3.31 0 0 1 .092 2.438 3.562 3.562 0 0 1 .947 2.474c0 3.54-2.155 4.32-4.208 4.548a2.195 2.195 0 0 1 .625 1.706c0 1.232-.011 2.227-.011 2.529a.694.694 0 0 1-.272.587z"></path></svg>
      </a>
      <a href= 'https://www.linkedin.com/in/yash-sarnaik-31153a284/' target="_blank" class="social-button linkedin">
        <svg viewBox="0 -2 44 44" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <g id="Icons" stroke="none" stroke-width="1">
            <g transform="translate(-702.000000, -265.000000)">
                <path d="M746,305 L736.2754,305 L736.2754,290.9384 C736.2754,287.257796 734.754233,284.74515 731.409219,284.74515 C728.850659,284.74515 727.427799,286.440738 726.765522,288.074854 C726.517168,288.661395 726.555974,289.478453 726.555974,290.295511 L726.555974,305 L716.921919,305 C716.921919,305 717.046096,280.091247 716.921919,277.827047 L726.555974,277.827047 L726.555974,282.091631 C727.125118,280.226996 730.203669,277.565794 735.116416,277.565794 C741.21143,277.565794 746,281.474355 746,289.890824 L746,305 L746,305 Z M707.17921,274.428187 L707.117121,274.428187 C704.0127,274.428187 702,272.350964 702,269.717936 C702,267.033681 704.072201,265 707.238711,265 C710.402634,265 712.348071,267.028559 712.41016,269.710252 C712.41016,272.34328 710.402634,274.428187 707.17921,274.428187 L707.17921,274.428187 L707.17921,274.428187 Z M703.109831,277.827047 L711.685795,277.827047 L711.685795,305 L703.109831,305 L703.109831,277.827047 L703.109831,277.827047 Z" id="LinkedIn">
    </path>
            </g>
        </g>
    </svg>
  </a>
<a href= 'https://x.com/Yash_Sarnaik23' target="_blank" class="social-button twitter">
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" xml:space="preserve">
        <path d="M459.37,151.716c0.325,4.548,0.325,9.097,0.325,13.645c0,138.72-105.583,298.558-298.558,298.558
            c-59.452,0-114.68-17.219-161.137-47.106c8.447,0.974,16.568,1.299,25.34,1.299c49.055,0,94.213-16.568,130.274-44.832
            c-46.132-0.975-84.792-31.188-98.112-72.772c6.498,0.974,12.995,1.624,19.818,1.624c9.421,0,18.843-1.3,27.614-3.573
            c-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969,7.797,30.214,12.67,47.431,13.319
            c-28.264-18.843-46.781-51.005-46.781-87.391c0-19.492,5.197-37.36,14.294-52.954c51.655,63.675,129.3,105.258,216.365,109.807
            c-1.624-7.797-2.599-15.918-2.599-24.04c0-57.828,46.782-104.934,104.934-104.934c30.213,0,57.502,12.67,76.67,33.137
            c23.715-4.548,46.456-13.32,66.599-25.34c-7.798,24.366-24.366,44.833-46.132,57.827c21.117-2.273,41.584-8.122,60.426-16.243
            C498.793,125.977,480.091,140.445,459.37,151.716z"></path>
    </svg>
</a>
  <a href= 'https://www.instagram.com/yashsarnaik23/' target="_blank"  class="social-button instagram">
    <svg width="800px" height="800px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <g id="Page-1" stroke="none" stroke-width="1">
        <g id="Dribbble-Light-Preview" transform="translate(-340.000000, -7439.000000)">
            <g id="icons" transform="translate(56.000000, 160.000000)">
                <path d="M289.869652,7279.12273 C288.241769,7279.19618 286.830805,7279.5942 285.691486,7280.72871 C284.548187,7281.86918 284.155147,7283.28558 284.081514,7284.89653 C284.035742,7285.90201 283.768077,7293.49818 284.544207,7295.49028 C285.067597,7296.83422 286.098457,7297.86749 287.454694,7298.39256 C288.087538,7298.63872 288.809936,7298.80547 289.869652,7298.85411 C298.730467,7299.25511 302.015089,7299.03674 303.400182,7295.49028 C303.645956,7294.859 303.815113,7294.1374 303.86188,7293.08031 C304.26686,7284.19677 303.796207,7282.27117 302.251908,7280.72871 C301.027016,7279.50685 299.5862,7278.67508 289.869652,7279.12273 M289.951245,7297.06748 C288.981083,7297.0238 288.454707,7296.86201 288.103459,7296.72603 C287.219865,7296.3826 286.556174,7295.72155 286.214876,7294.84312 C285.623823,7293.32944 285.819846,7286.14023 285.872583,7284.97693 C285.924325,7283.83745 286.155174,7282.79624 286.959165,7281.99226 C287.954203,7280.99968 289.239792,7280.51332 297.993144,7280.90837 C299.135448,7280.95998 300.179243,7281.19026 300.985224,7281.99226 C301.980262,7282.98483 302.473801,7284.28014 302.071806,7292.99991 C302.028024,7293.96767 301.865833,7294.49274 301.729513,7294.84312 C300.829003,7297.15085 298.757333,7297.47145 289.951245,7297.06748 M298.089663,7283.68956 C298.089663,7284.34665 298.623998,7284.88065 299.283709,7284.88065 C299.943419,7284.88065 300.47875,7284.34665 300.47875,7283.68956 C300.47875,7283.03248 299.943419,7282.49847 299.283709,7282.49847 C298.623998,7282.49847 298.089663,7283.03248 298.089663,7283.68956 M288.862673,7288.98792 C288.862673,7291.80286 291.150266,7294.08479 293.972194,7294.08479 C296.794123,7294.08479 299.081716,7291.80286 299.081716,7288.98792 C299.081716,7286.17298 296.794123,7283.89205 293.972194,7283.89205 C291.150266,7283.89205 288.862673,7286.17298 288.862673,7288.98792 M290.655732,7288.98792 C290.655732,7287.16159 292.140329,7285.67967 293.972194,7285.67967 C295.80406,7285.67967 297.288657,7287.16159 297.288657,7288.98792 C297.288657,7290.81525 295.80406,7292.29716 293.972194,7292.29716 C292.140329,7292.29716 290.655732,7290.81525 290.655732,7288.98792" id="instagram-[#167]">

</path>
            </g>
        </g>
    </g>
</svg>
  </a>
</div>

"""
st.markdown(f"<style>{salina_font_styles}</style>", unsafe_allow_html=True)
st.markdown("<div class='salina-font'><span style='color:black'>YASH UDAY SARNAIK</span></div>", unsafe_allow_html=True)

text = "<div style='text-align: center;'><span style='font-weight:bold; font-style:italic; color:black'>An engineer skilled in AI, Machine learning, deep learning and data analytics, blending technical prowess with a passion for adventure. A rider and wanderlust, embracing the open road and exploring new horizons.</span></div>"

st.markdown(text, unsafe_allow_html=True)


# CSS styles
css = """
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.social-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f2f2f2;
  box-shadow: 0px 0px 15px #00000027;
  padding: 15px 10px;
  border-radius: 5em;
}

.social-button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin: 0 10px;
  background-color: #fff;
  box-shadow: 0px 0px 4px #00000027;
  transition: 0.3s;
}

.social-button:hover {
  background-color: #f2f2f2;
  box-shadow: 0px 0px 6px 3px #00000027;
}

.social-buttons svg {
  transition: 0.3s;
  height: 20px;
}

.facebook {
  background-color: #3b5998;
}

.facebook svg {
  fill: #f2f2f2;
}

.facebook:hover svg {
  fill: #3b5998;
}

.github {
  background-color: #333;
}

.github svg {
  width: 25px;
  height: 25px;
  fill: #f2f2f2;
}

.github:hover svg {
  fill: #333;
}

.linkedin {
  background-color: #0077b5;
}

.linkedin svg {
  fill: #f2f2f2;
}

.linkedin:hover svg {
  fill: #0077b5;
}

.instagram {
  background-color: #c13584;
}

.instagram svg {
  fill: #f2f2f2;
}

.instagram:hover svg {
  fill: #c13584;
}

</style>
"""


html(css + html_component_1,height=90)



html_button = """
"""

bt = """
<style>
.center-button {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;  /* Adjust as needed */
}
.button {
    cursor: pointer;
    position: relative;
    padding: 10px 24px;
    font-size: 18px;
    color: #00000;  /* Peach color */
    border: 2px solid #FFA07A;  /* Peach border */
    border-radius: 34px;
    background-color: transparent;
    font-weight: 600;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.320, 1);
    overflow: hidden;
}

.button::before {
    content: '';
    position: absolute;
    inset: 0;
    margin: auto;
    width: 50px;
    height: 50px;
    border-radius: inherit;
    scale: 0;
    z-index: -1;
    background-color: #FFA07A;  /* Peach color */
    transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1);
}

.button:hover::before {
    scale: 3;
}

.button:hover {
    color: #212121;
    scale: 1.1;
    box-shadow: 0 0px 20px rgba(255, 160, 122, 0.4);  /* Peach shadow */
}

.button:active {
    scale: 1;
}
</style>
<div class="center-button">
    <a href="https://huggingface.co/yashsarnaik23" target="_blank" class="button">My Projects</a>
</div>
"""

html(bt+html_button,height=85)

op="""

		<div class="socket">
			<div class="gel center-gel">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c1 r1">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c2 r1">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c3 r1">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c4 r1">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c5 r1">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c6 r1">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			
			<div class="gel c7 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			
			<div class="gel c8 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c9 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c10 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c11 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c12 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c13 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c14 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c15 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c16 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c17 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c18 r2">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c19 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c20 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c21 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c22 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c23 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c24 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c25 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c26 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c28 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c29 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c30 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c31 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c32 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c33 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c34 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c35 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c36 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			<div class="gel c37 r3">
				<div class="hex-brick h1"></div>
				<div class="hex-brick h2"></div>
				<div class="hex-brick h3"></div>
			</div>
			
		</div>
	
"""

op1="""
<style>
.socket {
  width: 200px;
  height: 200px;
  position: absolute;
  left: 50%;
  margin-left: -100px;
  top: 50%;
  margin-top: -100px;
}

.hex-brick {
  background: #000000;
  width: 30px;
  height: 17px;
  position: absolute;
  top: 5px;
  animation-name: fade00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  -webkit-animation-name: fade00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
}

.h2 {
  transform: rotate(60deg);
  -webkit-transform: rotate(60deg);
}

.h3 {
  transform: rotate(-60deg);
  -webkit-transform: rotate(-60deg);
}

.gel {
  height: 30px;
  width: 30px;
  transition: all .3s;
  -webkit-transition: all .3s;
  position: absolute;
  top: 50%;
  left: 50%;
}

.center-gel {
  margin-left: -15px;
  margin-top: -15px;
  animation-name: pulse00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  -webkit-animation-name: pulse00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
}

.c1 {
  margin-left: -47px;
  margin-top: -15px;
}

.c2 {
  margin-left: -31px;
  margin-top: -43px;
}

.c3 {
  margin-left: 1px;
  margin-top: -43px;
}

.c4 {
  margin-left: 17px;
  margin-top: -15px;
}

.c5 {
  margin-left: -31px;
  margin-top: 13px;
}

.c6 {
  margin-left: 1px;
  margin-top: 13px;
}

.c7 {
  margin-left: -63px;
  margin-top: -43px;
}

.c8 {
  margin-left: 33px;
  margin-top: -43px;
}

.c9 {
  margin-left: -15px;
  margin-top: 41px;
}

.c10 {
  margin-left: -63px;
  margin-top: 13px;
}

.c11 {
  margin-left: 33px;
  margin-top: 13px;
}

.c12 {
  margin-left: -15px;
  margin-top: -71px;
}

.c13 {
  margin-left: -47px;
  margin-top: -71px;
}

.c14 {
  margin-left: 17px;
  margin-top: -71px;
}

.c15 {
  margin-left: -47px;
  margin-top: 41px;
}

.c16 {
  margin-left: 17px;
  margin-top: 41px;
}

.c17 {
  margin-left: -79px;
  margin-top: -15px;
}

.c18 {
  margin-left: 49px;
  margin-top: -15px;
}

.c19 {
  margin-left: -63px;
  margin-top: -99px;
}

.c20 {
  margin-left: 33px;
  margin-top: -99px;
}

.c21 {
  margin-left: 1px;
  margin-top: -99px;
}

.c22 {
  margin-left: -31px;
  margin-top: -99px;
}

.c23 {
  margin-left: -63px;
  margin-top: 69px;
}

.c24 {
  margin-left: 33px;
  margin-top: 69px;
}

.c25 {
  margin-left: 1px;
  margin-top: 69px;
}

.c26 {
  margin-left: -31px;
  margin-top: 69px;
}

.c27 {
  margin-left: -79px;
  margin-top: -15px;
}

.c28 {
  margin-left: -95px;
  margin-top: -43px;
}

.c29 {
  margin-left: -95px;
  margin-top: 13px;
}

.c30 {
  margin-left: 49px;
  margin-top: 41px;
}

.c31 {
  margin-left: -79px;
  margin-top: -71px;
}

.c32 {
  margin-left: -111px;
  margin-top: -15px;
}

.c33 {
  margin-left: 65px;
  margin-top: -43px;
}

.c34 {
  margin-left: 65px;
  margin-top: 13px;
}

.c35 {
  margin-left: -79px;
  margin-top: 41px;
}

.c36 {
  margin-left: 49px;
  margin-top: -71px;
}

.c37 {
  margin-left: 81px;
  margin-top: -15px;
}

.r1 {
  animation-name: pulse00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: .2s;
  -webkit-animation-name: pulse00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-delay: .2s;
}

.r2 {
  animation-name: pulse00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: .4s;
  -webkit-animation-name: pulse00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-delay: .4s;
}

.r3 {
  animation-name: pulse00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: .6s;
  -webkit-animation-name: pulse00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-delay: .6s;
}

.r1 > .hex-brick {
  animation-name: fade00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: .2s;
  -webkit-animation-name: fade00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-delay: .2s;
}

.r2 > .hex-brick {
  animation-name: fade00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: .4s;
  -webkit-animation-name: fade00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-delay: .4s;
}

.r3 > .hex-brick {
  animation-name: fade00;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-delay: .6s;
  -webkit-animation-name: fade00;
  -webkit-animation-duration: 2s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-delay: .6s;
}

@keyframes pulse00 {
  0% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }

  50% {
    -webkit-transform: scale(0.01);
    transform: scale(0.01);
  }

  100% {
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

@keyframes fade00 {
  0% {
    background: #252525;
  }

  50% {
    background: #000000;
  }

  100% {
    background: #353535;
  }
}


</style>
"""

html(op+op1,height=300)

# HTML component 1



html_component_2 = """
<div class="card">
  <span class="title">Skills</span>
  <div class="card__tags">
    <ul class="tag">
      <li class="tag__name">Langchain</li>
      <li class="tag__name">NLP</li> 
      <li class="tag__name">Streamlit</li>
      <li class="tag__name">Machine Learning</li>
      <li class="tag__name">Deep Learning</li>
      <li class="tag__name">Hugging face</li>
      <li class="tag__name">R</li>
      <li class="tag__name">Tableau</li>
      <li class="tag__name">PowerBI</li>
       
    </ul>
  </div>
</div>

"""

css2 = """
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.card-container {
  display: flex;
  height: 100vh; /* Adjust the height as needed */
}

.card {
  width: 280px;
  height: 400px;
  background: #f5f5f5;
  padding: 10px;
  display: flex;
  flex-wrap: wrap;
  color: #333333;
  border-radius: 15px;
  box-shadow: -20px 20px 0px -5px #cccccc;
  margin: 0 auto;
}

.title {
  font-weight: 900;
  font-size: 1.7em;
  text-align: center;
  width: 100%;
}

.tag__name {
  display: inline-block;
  color: #ffffff;
  font-size: 1.1em;
  background-color: #999999;
  padding: 6px 23px 9px;
  border-radius: 70em;
  margin: 8px 6px 8px 0;
  margin-left: 0px;
  position: relative;
  text-transform: lowercase;
  cursor: pointer;
  transition: all .3s ease-in-out;
}

.tag__name::before,.tag__name::after {
  content: "";
  display: inline-block;
  position: absolute;
  top: 40%;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #cccccc;
}

.tag__name::before {
  left: 7px;
}

.tag__name::after {
  right: 7px;
}

.tag__name:hover {
  transform: scale(1.1);
  background-color: #808080;
}
</style>
"""

html(css2 + html_component_2, height=600)

d=""" 
<div class="loader">
  <div class="loaderMiniContainer">
    <div class="barContainer">
      <span class="bar"></span>
      <span class="bar bar2"></span>
    </div>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 101 114"
      class="svgIcon"
    >
      <circle
        stroke-width="7"
        stroke="black"
        transform="rotate(36.0692 46.1726 46.1727)"
        r="29.5497"
        cy="46.1727"
        cx="46.1726"
      ></circle>
      <line
        stroke-width="7"
        stroke="black"
        y2="111.784"
        x2="97.7088"
        y1="67.7837"
        x1="61.7089"
      ></line>
    </svg>
  </div>
</div>

"""


d2="""
<style>

body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
  margin: 0;
}

.loader {
  display: flex;
  align-items: center;
  justify-content: center;
}
.loaderMiniContainer {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 130px;
  height: fit-content;
}
.barContainer {
  width: 100%;
  height: fit-content;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  gap: 10px;
  background-position: left;
}
.bar {
  width: 100%;
  height: 8px;
  background: linear-gradient(
    to right,
    rgb(161, 94, 255),
    rgb(217, 190, 255),
    rgb(161, 94, 255)
  );
  background-size: 200% 100%;
  border-radius: 10px;
  animation: bar ease-in-out 3s infinite alternate-reverse;
}
@keyframes bar {
  0% {
    background-position: left;
  }
  100% {
    background-position: right;
  }
}
.bar2 {
  width: 50%;
}
.svgIcon {
  position: absolute;
  left: -25px;
  margin-top: 18px;
  z-index: 2;
  width: 70%;
  animation: search ease-in-out 3s infinite alternate-reverse;
}
@keyframes search {
  0% {
    transform: translateX(0%) rotate(70deg);
  }

  100% {
    transform: translateX(100px) rotate(10deg);
  }
}
.svgIcon circle,
line {
  stroke: rgb(162, 55, 255);
}
.svgIcon circle {
  fill: rgba(98, 65, 142, 0.238);
}


</style>
"""

html(d+d2)

edu="""


"""

oop="""
<div class="flip-card">
    <div class="flip-card-inner">
        <div class="flip-card-front">
            <p class="title">Currently Seeking oppurtunities for</p>
            
        </div>
        <div class="flip-card-back">
            <p class="title"></p>
            <p>⦿AI/ML Engineer</p>
            <p>⦿Deep learning</p>
            <p>⦿Data science</p>
            <p>⦿LLM</p>
            
            
        </div>
    </div>
</div>
"""

oop2="""
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
  margin: 0;
}

.flip-card {
  background-color: transparent;
  width: 300px;
  height: 350px;
  perspective: 1000px;
  font-family: sans-serif;
}

.title {
  font-size: 1.5em;
  font-weight: 900;
  text-align: center;
  margin: 0;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  box-shadow: 0 8px 14px 0 rgba(0,0,0,0.2);
  position: absolute;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border: 1px solid coral;
  border-radius: 1rem;
}

.flip-card-front {
  background: linear-gradient(120deg, bisque 60%, rgb(255, 231, 222) 88%,
     rgb(255, 211, 195) 40%, rgba(255, 127, 80, 0.603) 48%);
  color: coral;
}

.flip-card-back {
  background: linear-gradient(120deg, rgb(255, 174, 145) 30%, coral 88%,
     bisque 40%, rgb(255, 185, 160) 78%);
  color: white;
  transform: rotateY(180deg);
}
</style>
"""
html(oop+oop2,height=400)



htm="""
<div class="animation">Thank you!</div>

"""

htm2="""
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
@keyframes typing {
  from {
    width: 0;
  }
}

@keyframes blink-caret {
  50% {
    border-color: transparent;
  }
}
/* When you change the amount of characters in the h1, you have to change 
the with: 14ch and  steps(14, end), if there is 14 characters, put 14, 
if there is 20 put 20 */
.animation {
  font: bold 200% Consolas, Monaco, monospace;
  border-right: .1em solid black;
  width: 13.20ch;
  margin: 2em 2em;
  white-space: nowrap;
  overflow: hidden;
  -webkit-animation: typing 5s steps(13, end),
	           blink-caret .5s step-end infinite alternate;
}




</style>
"""
html(htm+htm2)

mar="""
<div class="brick one"></div>
<div class="tooltip-mario-container">
  <div class="box"></div>
  <div class="mush"></div>
</div>
<div class="brick two"></div>

"""

mar2="""
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.brick {
  height: 2px;
  width: 2px;
  box-shadow: 2px 2px 0px #ff9999, 4px 2px 0px #ff9999, 6px 2px 0px #ff9999,
    8px 2px 0px #ff9999, 10px 2px 0px #ff9999, 12px 2px 0px #ff9999,
    14px 2px 0px #ff9999, 16px 2px 0px #ff9999, 18px 2px 0px #ff9999,
    20px 2px 0px #ff9999, 22px 2px 0px #ff9999, 24px 2px 0px #ff9999,
    26px 2px 0px #ff9999, 28px 2px 0px #ff9999, 30px 2px 0px #ff9999,
    32px 2px 0px #ff9999, 2px 4px 0px #cc3300, 4px 4px 0px #cc3300,
    6px 4px 0px #cc3300, 8px 4px 0px #cc3300, 10px 4px 0px #cc3300,
    12px 4px 0px #cc3300, 14px 4px 0px #cc3300, 16px 4px 0px #000,
    18px 4px 0px #cc3300, 20px 4px 0px #cc3300, 22px 4px 0px #cc3300,
    24px 4px 0px #cc3300, 26px 4px 0px #cc3300, 28px 4px 0px #cc3300,
    30px 4px 0px #cc3300, 32px 4px 0px #000, 2px 6px 0px #cc3300,
    4px 6px 0px #cc3300, 6px 6px 0px #cc3300, 8px 6px 0px #cc3300,
    10px 6px 0px #cc3300, 12px 6px 0px #cc3300, 14px 6px 0px #cc3300,
    16px 6px 0px #000, 18px 6px 0px #cc3300, 20px 6px 0px #cc3300,
    22px 6px 0px #cc3300, 24px 6px 0px #cc3300, 26px 6px 0px #cc3300,
    28px 6px 0px #cc3300, 30px 6px 0px #cc3300, 32px 6px 0px #000,
    2px 8px 0px #000, 4px 8px 0px #000, 6px 8px 0px #000, 8px 8px 0px #000,
    10px 8px 0px #000, 12px 8px 0px #000, 14px 8px 0px #000, 16px 8px 0px #000,
    18px 8px 0px #000, 20px 8px 0px #000, 22px 8px 0px #000, 24px 8px 0px #000,
    26px 8px 0px #000, 28px 8px 0px #000, 30px 8px 0px #000, 32px 8px 0px #000,
    2px 10px 0px #cc3300, 4px 10px 0px #cc3300, 6px 10px 0px #cc3300,
    8px 10px 0px #000, 10px 10px 0px #cc3300, 12px 10px 0px #cc3300,
    14px 10px 0px #cc3300, 16px 10px 0px #cc3300, 18px 10px 0px #cc3300,
    20px 10px 0px #cc3300, 22px 10px 0px #cc3300, 24px 10px 0px #000,
    26px 10px 0px #cc3300, 28px 10px 0px #cc3300, 30px 10px 0px #cc3300,
    32px 10px 0px #cc3300, 2px 12px 0px #cc3300, 4px 12px 0px #cc3300,
    6px 12px 0px #cc3300, 8px 12px 0px #000, 10px 12px 0px #cc3300,
    12px 12px 0px #cc3300, 14px 12px 0px #cc3300, 16px 12px 0px #cc3300,
    18px 12px 0px #cc3300, 20px 12px 0px #cc3300, 22px 12px 0px #cc3300,
    24px 12px 0px #000, 26px 12px 0px #cc3300, 28px 12px 0px #cc3300,
    30px 12px 0px #cc3300, 32px 12px 0px #cc3300, 2px 14px 0px #cc3300,
    4px 14px 0px #cc3300, 6px 14px 0px #cc3300, 8px 14px 0px #000,
    10px 14px 0px #cc3300, 12px 14px 0px #cc3300, 14px 14px 0px #cc3300,
    16px 14px 0px #cc3300, 18px 14px 0px #cc3300, 20px 14px 0px #cc3300,
    22px 14px 0px #cc3300, 24px 14px 0px #000, 26px 14px 0px #cc3300,
    28px 14px 0px #cc3300, 30px 14px 0px #cc3300, 32px 14px 0px #cc3300,
    2px 16px 0px #000, 4px 16px 0px #000, 6px 16px 0px #000, 8px 16px 0px #000,
    10px 16px 0px #000, 12px 16px 0px #000, 14px 16px 0px #000,
    16px 16px 0px #000, 18px 16px 0px #000, 20px 16px 0px #000,
    22px 16px 0px #000, 24px 16px 0px #000, 26px 16px 0px #000,
    28px 16px 0px #000, 30px 16px 0px #000, 32px 16px 0px #000,
    2px 18px 0px #cc3300, 4px 18px 0px #cc3300, 6px 18px 0px #cc3300,
    8px 18px 0px #cc3300, 10px 18px 0px #cc3300, 12px 18px 0px #cc3300,
    14px 18px 0px #cc3300, 16px 18px 0px #000, 18px 18px 0px #cc3300,
    20px 18px 0px #cc3300, 22px 18px 0px #cc3300, 24px 18px 0px #cc3300,
    26px 18px 0px #cc3300, 28px 18px 0px #cc3300, 30px 18px 0px #cc3300,
    32px 18px 0px #000, 2px 20px 0px #cc3300, 4px 20px 0px #cc3300,
    6px 20px 0px #cc3300, 8px 20px 0px #cc3300, 10px 20px 0px #cc3300,
    12px 20px 0px #cc3300, 14px 20px 0px #cc3300, 16px 20px 0px #000,
    18px 20px 0px #cc3300, 20px 20px 0px #cc3300, 22px 20px 0px #cc3300,
    24px 20px 0px #cc3300, 26px 20px 0px #cc3300, 28px 20px 0px #cc3300,
    30px 20px 0px #cc3300, 32px 20px 0px #000, 2px 22px 0px #cc3300,
    4px 22px 0px #cc3300, 6px 22px 0px #cc3300, 8px 22px 0px #cc3300,
    10px 22px 0px #cc3300, 12px 22px 0px #cc3300, 14px 22px 0px #cc3300,
    16px 22px 0px #000, 18px 22px 0px #cc3300, 20px 22px 0px #cc3300,
    22px 22px 0px #cc3300, 24px 22px 0px #cc3300, 26px 22px 0px #cc3300,
    28px 22px 0px #cc3300, 30px 22px 0px #cc3300, 32px 22px 0px #000,
    2px 24px 0px #000, 4px 24px 0px #000, 6px 24px 0px #000, 8px 24px 0px #000,
    10px 24px 0px #000, 12px 24px 0px #000, 14px 24px 0px #000,
    16px 24px 0px #000, 18px 24px 0px #000, 20px 24px 0px #000,
    22px 24px 0px #000, 24px 24px 0px #000, 26px 24px 0px #000,
    28px 24px 0px #000, 30px 24px 0px #000, 32px 24px 0px #000,
    2px 26px 0px #cc3300, 4px 26px 0px #cc3300, 6px 26px 0px #cc3300,
    8px 26px 0px #000, 10px 26px 0px #cc3300, 12px 26px 0px #cc3300,
    14px 26px 0px #cc3300, 16px 26px 0px #cc3300, 18px 26px 0px #cc3300,
    20px 26px 0px #cc3300, 22px 26px 0px #cc3300, 24px 26px 0px #000,
    26px 26px 0px #cc3300, 28px 26px 0px #cc3300, 30px 26px 0px #cc3300,
    32px 26px 0px #cc3300, 2px 28px 0px #cc3300, 4px 28px 0px #cc3300,
    6px 28px 0px #cc3300, 8px 28px 0px #000, 10px 28px 0px #cc3300,
    12px 28px 0px #cc3300, 14px 28px 0px #cc3300, 16px 28px 0px #cc3300,
    18px 28px 0px #cc3300, 20px 28px 0px #cc3300, 22px 28px 0px #cc3300,
    24px 28px 0px #000, 26px 28px 0px #cc3300, 28px 28px 0px #cc3300,
    30px 28px 0px #cc3300, 32px 28px 0px #cc3300, 2px 30px 0px #cc3300,
    4px 30px 0px #cc3300, 6px 30px 0px #cc3300, 8px 30px 0px #000,
    10px 30px 0px #cc3300, 12px 30px 0px #cc3300, 14px 30px 0px #cc3300,
    16px 30px 0px #cc3300, 18px 30px 0px #cc3300, 20px 30px 0px #cc3300,
    22px 30px 0px #cc3300, 24px 30px 0px #000, 26px 30px 0px #cc3300,
    28px 30px 0px #cc3300, 30px 30px 0px #cc3300, 32px 30px 0px #cc3300,
    2px 32px 0px #000, 4px 32px 0px #000, 6px 32px 0px #000, 8px 32px 0px #000,
    10px 32px 0px #000, 12px 32px 0px #000, 14px 32px 0px #000,
    16px 32px 0px #000, 18px 32px 0px #000, 20px 32px 0px #000,
    22px 32px 0px #000, 24px 32px 0px #000, 26px 32px 0px #000,
    28px 32px 0px #000, 30px 32px 0px #000, 32px 32px 0px #000;
}
.brick.one {
  transform: translateX(-60px);
}
.mush {
  height: 2px;
  width: 2px;
  box-shadow: 14px 2px 0px #fc9838, 16px 2px 0px #fc9838, 18px 2px 0px #fc9838,
    20px 2px 0px #fc9838, 12px 4px 0px #fc9838, 14px 4px 0px #fc9838,
    16px 4px 0px #fc9838, 18px 4px 0px #fc9838, 20px 4px 0px #d82800,
    22px 4px 0px #d82800, 10px 6px 0px #fc9838, 12px 6px 0px #fc9838,
    14px 6px 0px #fc9838, 16px 6px 0px #fc9838, 18px 6px 0px #d82800,
    20px 6px 0px #d82800, 22px 6px 0px #d82800, 24px 6px 0px #d82800,
    8px 8px 0px #fc9838, 10px 8px 0px #fc9838, 12px 8px 0px #fc9838,
    14px 8px 0px #fc9838, 16px 8px 0px #fc9838, 18px 8px 0px #d82800,
    20px 8px 0px #d82800, 22px 8px 0px #d82800, 24px 8px 0px #d82800,
    26px 8px 0px #d82800, 6px 10px 0px #fc9838, 8px 10px 0px #fc9838,
    10px 10px 0px #fc9838, 12px 10px 0px #fc9838, 14px 10px 0px #fc9838,
    16px 10px 0px #fc9838, 18px 10px 0px #fc9838, 20px 10px 0px #d82800,
    22px 10px 0px #d82800, 24px 10px 0px #d82800, 26px 10px 0px #fc9838,
    28px 10px 0px #fc9838, 4px 12px 0px #fc9838, 6px 12px 0px #fc9838,
    8px 12px 0px #d82800, 10px 12px 0px #d82800, 12px 12px 0px #d82800,
    14px 12px 0px #fc9838, 16px 12px 0px #fc9838, 18px 12px 0px #fc9838,
    20px 12px 0px #fc9838, 22px 12px 0px #fc9838, 24px 12px 0px #fc9838,
    26px 12px 0px #fc9838, 28px 12px 0px #fc9838, 30px 12px 0px #fc9838,
    4px 14px 0px #fc9838, 6px 14px 0px #d82800, 8px 14px 0px #d82800,
    10px 14px 0px #d82800, 12px 14px 0px #d82800, 14px 14px 0px #d82800,
    16px 14px 0px #fc9838, 18px 14px 0px #fc9838, 20px 14px 0px #fc9838,
    22px 14px 0px #fc9838, 24px 14px 0px #fc9838, 26px 14px 0px #fc9838,
    28px 14px 0px #fc9838, 30px 14px 0px #fc9838, 2px 16px 0px #fc9838,
    4px 16px 0px #fc9838, 6px 16px 0px #d82800, 8px 16px 0px #d82800,
    10px 16px 0px #d82800, 12px 16px 0px #d82800, 14px 16px 0px #d82800,
    16px 16px 0px #fc9838, 18px 16px 0px #fc9838, 20px 16px 0px #fc9838,
    22px 16px 0px #fc9838, 24px 16px 0px #fc9838, 26px 16px 0px #d82800,
    28px 16px 0px #d82800, 30px 16px 0px #fc9838, 32px 16px 0px #fc9838,
    2px 18px 0px #fc9838, 4px 18px 0px #fc9838, 6px 18px 0px #d82800,
    8px 18px 0px #d82800, 10px 18px 0px #d82800, 12px 18px 0px #d82800,
    14px 18px 0px #d82800, 16px 18px 0px #fc9838, 18px 18px 0px #fc9838,
    20px 18px 0px #fc9838, 22px 18px 0px #fc9838, 24px 18px 0px #fc9838,
    26px 18px 0px #d82800, 28px 18px 0px #d82800, 30px 18px 0px #d82800,
    32px 18px 0px #fc9838, 2px 20px 0px #fc9838, 4px 20px 0px #fc9838,
    6px 20px 0px #fc9838, 8px 20px 0px #d82800, 10px 20px 0px #d82800,
    12px 20px 0px #d82800, 14px 20px 0px #fc9838, 16px 20px 0px #fc9838,
    18px 20px 0px #fc9838, 20px 20px 0px #fc9838, 22px 20px 0px #fc9838,
    24px 20px 0px #fc9838, 26px 20px 0px #fc9838, 28px 20px 0px #d82800,
    30px 20px 0px #d82800, 32px 20px 0px #fc9838, 2px 22px 0px #fc9838,
    4px 22px 0px #fc9838, 6px 22px 0px #fc9838, 8px 22px 0px #fc9838,
    10px 22px 0px #fc9838, 12px 22px 0px #fc9838, 14px 22px 0px #fc9838,
    16px 22px 0px #fc9838, 18px 22px 0px #fc9838, 20px 22px 0px #fc9838,
    22px 22px 0px #fc9838, 24px 22px 0px #fc9838, 26px 22px 0px #fc9838,
    28px 22px 0px #fc9838, 30px 22px 0px #fc9838, 32px 22px 0px #fc9838,
    4px 24px 0px #fc9838, 6px 24px 0px #d82800, 8px 24px 0px #d82800,
    10px 24px 0px #d82800, 12px 24px 0px #fff, 14px 24px 0px #fff,
    16px 24px 0px #fff, 18px 24px 0px #fff, 20px 24px 0px #fff,
    22px 24px 0px #fff, 24px 24px 0px #d82800, 26px 24px 0px #d82800,
    28px 24px 0px #d82800, 30px 24px 0px #fc9838, 10px 26px 0px #fff,
    12px 26px 0px #fff, 14px 26px 0px #fff, 16px 26px 0px #fff,
    18px 26px 0px #fff, 20px 26px 0px #fff, 22px 26px 0px #fff,
    24px 26px 0px #fff, 10px 28px 0px #fff, 12px 28px 0px #fff,
    14px 28px 0px #fff, 16px 28px 0px #fff, 18px 28px 0px #fff,
    20px 28px 0px #fff, 22px 28px 0px #fc9838, 24px 28px 0px #fff,
    10px 30px 0px #fff, 12px 30px 0px #fff, 14px 30px 0px #fff,
    16px 30px 0px #fff, 18px 30px 0px #fff, 20px 30px 0px #fff,
    22px 30px 0px #fc9838, 24px 30px 0px #fff, 12px 32px 0px #fff,
    14px 32px 0px #fff, 16px 32px 0px #fff, 18px 32px 0px #fff,
    20px 32px 0px #fc9838, 22px 32px 0px #fff;
  transform: translate(-0px, -0px);
  z-index: -1;
  opacity: 0;
}
.box {
  position: absolute;
  background-color: rgba(46, 37, 37, 0);
  z-index: 3;
  width: 34px;
  height: 34px;
}
.box:hover + .mush {
  animation: mush 0.5s linear forwards;
  opacity: 1;
}
@keyframes mush {
  0% {
    transform: scale(0.8) translate(-0px, -0px);
  }
  50% {
    transform: scale(1.1) translate(-0px, -80px);
  }
  100% {
    transform: scale(1.1) translate(-0px, -35px);
  }
}
.tooltip-mario-container {
  height: 2px;
  width: 2px;
  box-shadow: 4px 2px 0px #ce3100, 6px 2px 0px #ce3100, 8px 2px 0px #ce3100,
    10px 2px 0px #ce3100, 12px 2px 0px #ce3100, 14px 2px 0px #ce3100,
    16px 2px 0px #ce3100, 18px 2px 0px #ce3100, 20px 2px 0px #ce3100,
    22px 2px 0px #ce3100, 24px 2px 0px #ce3100, 26px 2px 0px #ce3100,
    28px 2px 0px #ce3100, 30px 2px 0px #ce3100, 2px 4px 0px #ce3100,
    4px 4px 0px #ff9c31, 6px 4px 0px #ff9c31, 8px 4px 0px #ff9c31,
    10px 4px 0px #ff9c31, 12px 4px 0px #ff9c31, 14px 4px 0px #ff9c31,
    16px 4px 0px #ff9c31, 18px 4px 0px #ff9c31, 20px 4px 0px #ff9c31,
    22px 4px 0px #ff9c31, 24px 4px 0px #ff9c31, 26px 4px 0px #ff9c31,
    28px 4px 0px #ff9c31, 30px 4px 0px #ff9c31, 32px 4px 0px #000,
    2px 6px 0px #ce3100, 4px 6px 0px #ff9c31, 6px 6px 0px #000,
    8px 6px 0px #ff9c31, 10px 6px 0px #ff9c31, 12px 6px 0px #ff9c31,
    14px 6px 0px #ff9c31, 16px 6px 0px #ff9c31, 18px 6px 0px #ff9c31,
    20px 6px 0px #ff9c31, 22px 6px 0px #ff9c31, 24px 6px 0px #ff9c31,
    26px 6px 0px #ff9c31, 28px 6px 0px #000, 30px 6px 0px #ff9c31,
    32px 6px 0px #000, 2px 8px 0px #ce3100, 4px 8px 0px #ff9c31,
    6px 8px 0px #ff9c31, 8px 8px 0px #ff9c31, 10px 8px 0px #ff9c31,
    12px 8px 0px #ce3100, 14px 8px 0px #ce3100, 16px 8px 0px #ce3100,
    18px 8px 0px #ce3100, 20px 8px 0px #ce3100, 22px 8px 0px #ff9c31,
    24px 8px 0px #ff9c31, 26px 8px 0px #ff9c31, 28px 8px 0px #ff9c31,
    30px 8px 0px #ff9c31, 32px 8px 0px #000, 2px 10px 0px #ce3100,
    4px 10px 0px #ff9c31, 6px 10px 0px #ff9c31, 8px 10px 0px #ff9c31,
    10px 10px 0px #ce3100, 12px 10px 0px #ce3100, 14px 10px 0px #000,
    16px 10px 0px #000, 18px 10px 0px #000, 20px 10px 0px #ce3100,
    22px 10px 0px #ce3100, 24px 10px 0px #ff9c31, 26px 10px 0px #ff9c31,
    28px 10px 0px #ff9c31, 30px 10px 0px #ff9c31, 32px 10px 0px #000,
    2px 12px 0px #ce3100, 4px 12px 0px #ff9c31, 6px 12px 0px #ff9c31,
    8px 12px 0px #ff9c31, 10px 12px 0px #ce3100, 12px 12px 0px #ce3100,
    14px 12px 0px #000, 16px 12px 0px #ff9c31, 18px 12px 0px #ff9c31,
    20px 12px 0px #ce3100, 22px 12px 0px #ce3100, 24px 12px 0px #000,
    26px 12px 0px #ff9c31, 28px 12px 0px #ff9c31, 30px 12px 0px #ff9c31,
    32px 12px 0px #000, 2px 14px 0px #ce3100, 4px 14px 0px #ff9c31,
    6px 14px 0px #ff9c31, 8px 14px 0px #ff9c31, 10px 14px 0px #ce3100,
    12px 14px 0px #ce3100, 14px 14px 0px #000, 16px 14px 0px #ff9c31,
    18px 14px 0px #ff9c31, 20px 14px 0px #ce3100, 22px 14px 0px #ce3100,
    24px 14px 0px #000, 26px 14px 0px #ff9c31, 28px 14px 0px #ff9c31,
    30px 14px 0px #ff9c31, 32px 14px 0px #000, 2px 16px 0px #ce3100,
    4px 16px 0px #ff9c31, 6px 16px 0px #ff9c31, 8px 16px 0px #ff9c31,
    10px 16px 0px #ff9c31, 12px 16px 0px #000, 14px 16px 0px #000,
    16px 16px 0px #ff9c31, 18px 16px 0px #ce3100, 20px 16px 0px #ce3100,
    22px 16px 0px #ce3100, 24px 16px 0px #000, 26px 16px 0px #ff9c31,
    28px 16px 0px #ff9c31, 30px 16px 0px #ff9c31, 32px 16px 0px #000,
    2px 18px 0px #ce3100, 4px 18px 0px #ff9c31, 6px 18px 0px #ff9c31,
    8px 18px 0px #ff9c31, 10px 18px 0px #ff9c31, 12px 18px 0px #ff9c31,
    14px 18px 0px #ff9c31, 16px 18px 0px #ce3100, 18px 18px 0px #ce3100,
    20px 18px 0px #000, 22px 18px 0px #000, 24px 18px 0px #000,
    26px 18px 0px #ff9c31, 28px 18px 0px #ff9c31, 30px 18px 0px #ff9c31,
    32px 18px 0px #000, 2px 20px 0px #ce3100, 4px 20px 0px #ff9c31,
    6px 20px 0px #ff9c31, 8px 20px 0px #ff9c31, 10px 20px 0px #ff9c31,
    12px 20px 0px #ff9c31, 14px 20px 0px #ff9c31, 16px 20px 0px #ce3100,
    18px 20px 0px #ce3100, 20px 20px 0px #000, 22px 20px 0px #ff9c31,
    24px 20px 0px #ff9c31, 26px 20px 0px #ff9c31, 28px 20px 0px #ff9c31,
    30px 20px 0px #ff9c31, 32px 20px 0px #000, 2px 22px 0px #ce3100,
    4px 22px 0px #ff9c31, 6px 22px 0px #ff9c31, 8px 22px 0px #ff9c31,
    10px 22px 0px #ff9c31, 12px 22px 0px #ff9c31, 14px 22px 0px #ff9c31,
    16px 22px 0px #ff9c31, 18px 22px 0px #000, 20px 22px 0px #000,
    22px 22px 0px #ff9c31, 24px 22px 0px #ff9c31, 26px 22px 0px #ff9c31,
    28px 22px 0px #ff9c31, 30px 22px 0px #ff9c31, 32px 22px 0px #000,
    2px 24px 0px #ce3100, 4px 24px 0px #ff9c31, 6px 24px 0px #ff9c31,
    8px 24px 0px #ff9c31, 10px 24px 0px #ff9c31, 12px 24px 0px #ff9c31,
    14px 24px 0px #ff9c31, 16px 24px 0px #ce3100, 18px 24px 0px #ce3100,
    20px 24px 0px #ff9c31, 22px 24px 0px #ff9c31, 24px 24px 0px #ff9c31,
    26px 24px 0px #ff9c31, 28px 24px 0px #ff9c31, 30px 24px 0px #ff9c31,
    32px 24px 0px #000, 2px 26px 0px #ce3100, 4px 26px 0px #ff9c31,
    6px 26px 0px #ff9c31, 8px 26px 0px #ff9c31, 10px 26px 0px #ff9c31,
    12px 26px 0px #ff9c31, 14px 26px 0px #ff9c31, 16px 26px 0px #ce3100,
    18px 26px 0px #ce3100, 20px 26px 0px #000, 22px 26px 0px #ff9c31,
    24px 26px 0px #ff9c31, 26px 26px 0px #ff9c31, 28px 26px 0px #ff9c31,
    30px 26px 0px #ff9c31, 32px 26px 0px #000, 2px 28px 0px #ce3100,
    4px 28px 0px #ff9c31, 6px 28px 0px #000, 8px 28px 0px #ff9c31,
    10px 28px 0px #ff9c31, 12px 28px 0px #ff9c31, 14px 28px 0px #ff9c31,
    16px 28px 0px #ff9c31, 18px 28px 0px #000, 20px 28px 0px #000,
    22px 28px 0px #ff9c31, 24px 28px 0px #ff9c31, 26px 28px 0px #ff9c31,
    28px 28px 0px #000, 30px 28px 0px #ff9c31, 32px 28px 0px #000,
    2px 30px 0px #ce3100, 4px 30px 0px #ff9c31, 6px 30px 0px #ff9c31,
    8px 30px 0px #ff9c31, 10px 30px 0px #ff9c31, 12px 30px 0px #ff9c31,
    14px 30px 0px #ff9c31, 16px 30px 0px #ff9c31, 18px 30px 0px #ff9c31,
    20px 30px 0px #ff9c31, 22px 30px 0px #ff9c31, 24px 30px 0px #ff9c31,
    26px 30px 0px #ff9c31, 28px 30px 0px #ff9c31, 30px 30px 0px #ff9c31,
    32px 30px 0px #000, 2px 32px 0px #000, 4px 32px 0px #000, 6px 32px 0px #000,
    8px 32px 0px #000, 10px 32px 0px #000, 12px 32px 0px #000,
    14px 32px 0px #000, 16px 32px 0px #000, 18px 32px 0px #000,
    20px 32px 0px #000, 22px 32px 0px #000, 24px 32px 0px #000,
    26px 32px 0px #000, 28px 32px 0px #000, 30px 32px 0px #000,
    32px 32px 0px #000;
  position: absolute;
  transform: translate(-30px);
  z-index: 3;
}

</style>
"""

html(mar+mar2)
