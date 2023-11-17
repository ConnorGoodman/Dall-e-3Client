import os
import openai
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
    )
    print(response)
    return response

def save_image(image_url, folder, image_name):
    response = requests.get(image_url)
    with open(os.path.join(folder, image_name), "wb") as file:
        file.write(response.content)

def main():
    # Prompt the user for an image generation prompt
    prompt = input("Enter the image generation prompt: ")

    # Prompt user for how many images to generate
    num_images = int(input("Enter the number of images to generate: "))
    num_images = min(num_images, 10)
    for x in range(num_images):
        # Generate image using DALL·E 3
        response = generate_image(prompt)
        image_url = response.data[0].url
        created = response.created
        print(image_url)
        # Prompt the user for an image name

        # Save the image to the 'images' folder
        folder = "images"
        os.makedirs(folder, exist_ok=True)
        image_name = str(created) + '.' + 'png'
        save_image(image_url, folder, image_name)

        print(f"Image '{image_name}' saved successfully in the 'images' folder.")

if __name__ == "__main__":
    main()
