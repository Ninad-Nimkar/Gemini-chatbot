from google import genai

client = genai.Client(api_key="")
prompt = input("prompt: ")

response = client.models.generate_content(
    model = "gemini-3-flash-preview", contents = prompt 
)
print(response.text)