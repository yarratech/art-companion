import base64
import requests

# OpenAI API Key (replace with your own key)
api_key = 'sk-cKUrGR5jHlZBAe18bTzOLdxQbCFGinlsAOVMEfxZbaT3BlbkFJV00_PeiTnFbynjwtiO2Jw-ccJkGOpacTLiGeugwFsA'

# Function to encode the image as base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your local image - change this as you please
image_file_path = r"C:\Users\yarra\Downloads\Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

# Encode the image
base64_image = encode_image(image_file_path)

# Set headers for the OpenAI API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Create the payload with the base64 image
payload = {
    "model": "gpt-4o-mini",  # or another model with vision capabilities
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What’s in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

# Make the POST request to OpenAI API
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Print the response from the API
print(response.json())

