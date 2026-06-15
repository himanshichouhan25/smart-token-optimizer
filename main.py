from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Prompt
prompt = "Write a detailed essay on AI and society."

# Count tokens
token_info = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents=prompt
)

print("Total Tokens:", token_info.total_tokens)

# Check token limit
if token_info.total_tokens > 1000:
    print("Warning: The prompt is quite long and may exceed token limits for some models.")
else:
    print("The prompt is within the token limits for most models.")

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print("\nResponse:\n")
print(response.text)