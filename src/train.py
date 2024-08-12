from chatterbot.trainers import ListTrainer
from init import chatbot
import json
import os

data_file = open(os.path.abspath('src/data.json'), 'r')
dataset = json.load(data_file)['dataset']

try:
    trainer = ListTrainer(chatbot)
    for qa in dataset:
        trainer.train(qa)
except FileNotFoundError:
    print('le fichier data.json n\'existe pas! Essayer de creer un nouveau fichier qui contient la dataset!')
