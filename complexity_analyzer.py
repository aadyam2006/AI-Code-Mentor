import requests

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": "Bearer hf_your_token_here"
}

def analyze_complexity(code):

    prompt = f"Analyze the time complexity of this code:\n{code}"

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code != 200:
        return f"API Error: {response.text}"

    try:
        result = response.json()
    except:
        return "Error reading AI response."

    if isinstance(result, list):
        return result[0].get("generated_text", "No complexity returned.")
    else:
        return str(result)