## Invoice Extractor
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load all environment variables from .env
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro vision model and get response
def get_gemini_response(input_text, image_data, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_text + prompt, image_data[0]], stream=False)
        
        # When stream is True, use the below code

        # complete_response = []
        # for part in response:
        #    complete_response.append(part)

        # Join the parts to form the final text
        # final_text = ''.join(complete_response)
        # print(final_text)
        # return final_text

        return response.text
    except Exception as e:
        st.error(f"Error in generating content: {e}")
        return None

# Function to setup the input image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                'mime_type': uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize the Streamlit app
st.set_page_config(page_title="Invoice Extractor")
st.header("Gemini Application")

input_prompt = """
You are an expert in understanding invoices. You will receive input images as invoices
and you will have to answer questions on the input image.
"""

uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    input_text = st.text_input("Input Prompt: ", key="input")


submit = st.button("Tell me about the invoice")

if submit:
    if uploaded_file is not None:
        try:
            image_data = input_image_setup(uploaded_file)

            response = get_gemini_response(input_prompt, image_data, input_text)

            if response:
                st.subheader("The Response is")
                st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image before submitting.")
