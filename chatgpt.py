import openai
openai.api_key = ""

def generate_response(prompt, input_text):
    response = openai.Completion.create(
        engine="text-ada-001",
        prompt=prompt + input_text,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text

while True:
    user_input = input("You: ")
    if user_input == "bye":
        break
    prompt = "Chatbot: "
    response = generate_response(prompt, user_input)
    print(response)
