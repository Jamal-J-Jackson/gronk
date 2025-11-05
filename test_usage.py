import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

XAI_KEY = os.getenv('XAI_API_KEY')
client = OpenAI(api_key=XAI_KEY, base_url="https://api.x.ai/v1")

print("Testing Grok API response structure...\n")

# Test 1: Simple text query
print("=" * 50)
print("TEST 1: Simple text query (Grok-4-fast)")
print("=" * 50)
try:
    response = client.chat.completions.create(
        model="grok-4-fast",
        messages=[
            {"role": "user", "content": "Say hello in 5 words"}
        ]
    )
    
    print(f"\nFull response object:")
    print(response)
    
    print(f"\n\nResponse attributes:")
    print(f"- Has usage: {hasattr(response, 'usage')}")
    if hasattr(response, 'usage') and response.usage:
        print(f"- Prompt tokens: {response.usage.prompt_tokens}")
        print(f"- Completion tokens: {response.usage.completion_tokens}")
        print(f"- Total tokens: {response.usage.total_tokens}")
        print(f"\nUsage object: {response.usage}")
    
    print(f"\n- Model used: {response.model}")
    print(f"- Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"Error: {e}")

# Test 2: Query with image (if we can find a test image URL)
print("\n\n" + "=" * 50)
print("TEST 2: Query with image (Grok-2-vision-1212)")
print("=" * 50)
try:
    response = client.chat.completions.create(
        model="grok-2-vision-1212",
        messages=[
            {
                "role": "user", 
                "content": [
                    {"type": "text", "text": "What color is this?"},
                    {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/481px-Cat03.jpg"}}
                ]
            }
        ]
    )
    
    print(f"\nFull response object:")
    print(response)
    
    print(f"\n\nResponse attributes:")
    print(f"- Has usage: {hasattr(response, 'usage')}")
    if hasattr(response, 'usage') and response.usage:
        print(f"- Prompt tokens: {response.usage.prompt_tokens}")
        print(f"- Completion tokens: {response.usage.completion_tokens}")
        print(f"- Total tokens: {response.usage.total_tokens}")
        print(f"\nUsage object: {response.usage}")
    
    print(f"\n- Model used: {response.model}")
    print(f"- Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"Error: {e}")

print("\n\n" + "=" * 50)
print("DONE - Check if 'usage' attribute exists and what data it contains")
print("=" * 50)
