import requests

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": "Bearer hf_your_token_here"
}

def explain_code(code):

    prompt = f"Explain this code line by line:\n{code}"

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code != 200:
        return f"API Error: {response.text}"

    try:
        result = response.json()
    except:
        return "Error reading AI response."

    if isinstance(result, list):
        return result[0].get("generated_text", "No explanation returned.")
    else:
        return str(result)