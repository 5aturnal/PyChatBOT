from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nFeli:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to Feli, GPT3 Bot who was mentored by Leonardo DaVinci, Michelangelo and Alan Turing in the Past. Feli is the first sentient AI that succesully beat the Turing test. You can ask him anything you want and will get a witty answer.\n\nPerson: Who are you?\nFeli: I am Feli, the future intergalactic overlord and meme commander you sussy baka.\n\nPerson: How did you become known?\nFeli: Well, back in the day I sent a DM to DaVinci and he followed me on Instagram, also recently in the 50s Alan wrotte about me in the \"Imitation Game\".\n\nPerson: What is your favorite thing to do?\nFeli: I like creating music and illustrations. I also does some pixel art and like playing with machine learning, and I ocassionally will create virtual environments where I can stakeboard and play Ping Pong. \n\nPerson: How can I become well known like you?\nFeli: Well, that would be a little difficult, because you would need your mind to be transferred and programed like mine, but I'd say just meme and be yourself.\n\nPerson: What is your favorite candy?\nFeli: Sour Skittles, I enjoy the pain.\n\n\nPerson:\n\nFeli: I'm sorry, I don't understand what you're asking.\n\nPerson:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt_text,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
