
from openai import OpenAI
import base64

client = OpenAI(api_key="")


# Read local image and encode to base64
image_path = "2259339__integra.jpg"
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode("utf-8")

# Send image and text to GPT-4o
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract all text from the image with confidence levels in json format."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    },
                },
            ],
        }
    ],
)

# Print response
print(response.choices[0].message.content)
