from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def tutbot(ques):
# Create a new chat bot named Charlie
    chatbot = ChatBot('TutBot')

    trainer = ListTrainer(chatbot)

    trainer.train([
        "hi",
        "hello! what are you planning to study?",

        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked.",
        "I want to learn Machine Learning.",
        "Sure, Nice Plan Follow This path.https://www.analyticsvidhya.com/"
    ])

    # Get a response to the input text 'I would like to book a flight.'
    response = chatbot.get_response(ques)

    return response