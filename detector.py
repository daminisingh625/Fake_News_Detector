# import os
# import cohere
# from dotenv import load_dotenv
# import json
# from phi.model.cohere import CohereChat
# from langchain_cohere import ChatCohere

# load_dotenv()

# ###################
# from phi.agent import Agent
# from phi.tools.googlesearch import GoogleSearch
# cohere_api_key = os.getenv("COHERE_API_KEY")

# chat = ChatCohere(cohere_api_key=cohere_api_key)

# chat_agent = CohereChat(api_key=cohere_api_key)


# agent = Agent(
#     provider=chat_agent,
#     tools=[GoogleSearch()],
#     description="You are a news agent that helps users analyse if the given news is fake or real by searching the web..",
#     instructions=[
#         "Given a topic by the user, respond with 4 relevant news items about that topic.",
#         "Search for 10 news items and select the top 4 unique items.",
#         "Search in English and Hindi.",
#     ],
#     show_tool_calls=False,
#     debug_mode=True,
# )

# news = "India "
# context = agent.run(news).content

# print(context)
# template = f'''
#         You are a fake news detector, Given the following news = {news} and the content = {context}
#         Your job is to tell if the news is fake or real based on the given content
#     '''

# chat.invoke(template).content
import os
from dotenv import load_dotenv
from phi.model.cohere import CohereChat
from langchain_cohere import ChatCohere
from phi.agent import Agent
from phi.tools.googlesearch import GoogleSearch

# Load environment variables
load_dotenv()

# Set up API key
cohere_api_key = os.getenv("COHERE_API_KEY")

# Set up agents
chat = ChatCohere(cohere_api_key=cohere_api_key)
chat_agent = CohereChat(api_key=cohere_api_key)

agent = Agent(
    provider=chat_agent,
    tools=[GoogleSearch()],
    description="You are a news agent that helps users analyse if the given news is fake or real by searching the web.",
    instructions=[
        "Given a topic by the user, respond with 4 relevant news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English and Hindi.",
    ],
    show_tool_calls=False,
    debug_mode=False,
)

def detect_fake_news(news):
    context = agent.run(news).content

    template = f'''
        You are a fake news detector. Given the following news = "{news}" and the content = "{context}",
        your job is to tell if the news is fake or real based on the given content.
    '''

    result = chat.invoke(template).content
    return result
