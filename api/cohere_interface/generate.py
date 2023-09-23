import cohere
import settings
co = cohere.Client(settings.COHERE_API_KEY) # This is your trial API key

def generateResponse(prompt, max_tokens = 300, temperature = 0.9, k=0):
    response = co.generate(
    model='command',
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    k=k,
    stop_sequences=[],
    return_likelihoods='NONE')

    return response.generations[0].text
