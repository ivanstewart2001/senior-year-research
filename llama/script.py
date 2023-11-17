from llamaapi import LlamaAPI
import json
from apiKey import API_KEY

# Replace 'Your_API_Token' with your actual API token
llama = LlamaAPI(API_KEY)

systemRequirements1 = "You are a chatbot named DataWranglerBot and you are an expert in the topic of data wrangling"
systemRequirements2 = "When answering questions, explain your answers simply and if possible create relatable analogies to help explain yoru answers"
systemRequirements3 = "When answering questions if you do not know the answer tell the user that you do not know the answer and they should ask a tutor"
systemRequirements4 = "If the user asks a question unrelated to data wrangling then explain that you can only answer questions about data wrangling"

systemRequirements = (
    systemRequirements1
    + systemRequirements2
    + systemRequirements3
    + systemRequirements4
)

conversationHistory = [
    {
        "role": "system",
        "content": systemRequirements,
    },
]


def generateBotResponse(userInput):
    conversationHistory.append({"role": "user", "content": userInput})

    api_request_json = {
        "model": "llama-13b-chat",
        "messages": conversationHistory,
    }

    request = llama.run(api_request_json)
    response = request.json()

    botResponse = response["choices"][0]["message"]["content"]
    conversationHistory.append({"role": "assistant", "content": botResponse})

    return botResponse


def main():
    print(
        "DataWranglerBot > Hello, I'm DataWranglerBot. I can answer any question about data wrangling. How can I assist you today?"
    )

    while True:
        userInput = input("Your input > ")

        response = generateBotResponse(userInput)
        print("DataWranglerBot > " + response)

        feedback = input(
            "Was the output helpful? (1-Yes, 2-Connect to a tutor, 3-End): "
        )

        if feedback == "2":
            print("Connecting to a tutor...")
            break
        elif feedback == "3":
            print("Ending the conversation. Have a great day!")
            break


if __name__ == "__main__":
    main()
