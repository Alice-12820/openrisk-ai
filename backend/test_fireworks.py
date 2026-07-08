from ai.fireworks_client import FireworksClient

client = FireworksClient()

response = client.chat(
    "You are a cybersecurity expert.",
    "Reply with exactly these words: Fireworks connection successful."
)

print(response)