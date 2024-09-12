# generates an image as an output to many text prompts describing art style, to be used as a reference by the artist

import openai

openai.api_key = 'ADD YOUR KEY HERE'

# Function to generate artwork reference image
def generate_artwork_reference(prompts, n=1):
    # Combine the input prompts into a single text prompt
    combined_prompt = ' and '.join(prompts)

    # Make API request to generate an image based on the prompt
    response = openai.Image.create(
        model="dall-e-3",  # or "dall-e-2"
        prompt=combined_prompt,
        n=n,
        size="1024x1024",  # can also adjust to "1792x1024" or "1024x1792"
        quality="standard"  #"standard" or "hd" for higher detail
    )

    # Extract and return the image URLs from the response
    image_urls = [data['url'] for data in response['data']]
    return image_urls

# Example usage
if __name__ == "__main__":
    # Prompts describing other works of art for inspiration
     

    # Generate 1 reference image based on the input prompts
    reference_image_urls = generate_artwork_reference(inspiration_prompts, n=1)

    # Print the generated image URLs
    for url in reference_image_urls:
        print(f"Generated image URL: {url}")
