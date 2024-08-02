from chatterbot.trainers import ListTrainer
from init import chatbot

dataset = [
    ['Bonjour', 'Bonjour! Comment puis-je vous aider?'],
    ["Je suis un nouvel stagiaire.",
        "Bienvenue! De quoi avez-vous besoin pour commencer?"],
    ["Pouvez-vous m'expliquer les tâches de la journée?",
        "Bien sûr. Vous devez d'abord vérifier vos e-mails pour les nouvelles instructions."],
    ["À qui puis-je demander de l'aide?",
        "Vous pouvez demander de l'aide à votre superviseur ou à n'importe quel collègue."],
    ["Quels outils vais-je utiliser?",
        "Vous utiliserez principalement Google Workspace, Slack et GitHub."],
    ["Merci", "De rien! Si vous avez d'autres questions, n'hésitez pas à demander."],
    ["Quelles sont les horaires de travail?",
        "Les horaires de travail sont de 9h à 17h, du lundi au vendredi."],
    ["Où se trouve la cafétéria?",
        "La cafétéria se trouve au rez-de-chaussée, près de l'entrée principale."],
    ["Comment puis-je accéder au réseau Wi-Fi?",
        "Vous pouvez accéder au réseau Wi-Fi en utilisant le SSID 'ONCF' et le mot de passe fourni par le service informatique."]
]


try:
    trainer = ListTrainer(chatbot)
    for qa in dataset:
        print(qa)
        trainer.train(qa)

except FileNotFoundError:
    print('le fichier data.txt n\'existe pas! Essayer de creer un nouveau fichier qui contient la dataset!')
