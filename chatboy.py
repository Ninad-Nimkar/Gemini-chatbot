from google import genai

client = genai.Client(api_key="AIzaSyDvtUKR01gwB7SZkiG8p2aC29E6IEiCORg")
prompt = input("prompt: ")

response = client.models.generate_content(
    model = "gemini-3-flash-preview", contents = prompt 
)
print(response.text)