from chatterbot.trainers import ListTrainer
from init import chatbot

try:
    with open("data.txt") as data:
        dataset = data.read().split('\n')

    trainer = ListTrainer(chatbot)
    trainer.train(dataset)
    
except FileNotFoundError:
    print('le fichier data.txt n\'existe pas! Essayer de creer un nouveau fichier qui contient la dataset!')