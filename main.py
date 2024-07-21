import openai

openai.api_key = open("API_KEY", "r").read()

response = openai.Image.create(
    prompt="Five yellow dogs playing ball in the rain",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)

