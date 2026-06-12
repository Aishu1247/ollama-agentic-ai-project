import ollama
 
# Send a single message to TinyLlama
response = ollama.chat(
    model='tinyllama',
    messages=[
        {
            'role': 'user',
            'content': 'What is Artificial Intelligence? Explain in 3 sentences.'
        }
    ]
)
 
# Extract and print the AI reply
print("AI Response:")
print("-" * 40)
print(response['message']['content'])
print("-" * 40)
print("Done!")
