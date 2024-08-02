from chatterbot import ChatBot

chatbot = ChatBot(
    'ONCFDSIChatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///oncf_dsi_database.sqlite3',
    read_only=True
)
