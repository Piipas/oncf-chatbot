# ONCF Assistant Chatbot

## How to use

1. clone the repository
```bash
$ git clone https://github.com/piipas/oncf-chatbot.git
```
2. create the venv directory
```bash
$ python3.8 -m venv venv
```

3. activate the virtual environment
```bash
$ venv/bin/activate
$ source venv/bin/activate
```

4. Install all dependencies/packages
```bash
$ pip install -r requirements.txt
```

5. Train the chatbot with the provided json data fron data.json
```bash
$ python train.py
```

6. Finally! Open the python file
```bash
$ python index.py
```

## How to build

1. Build the index file uding pyinstaller
```bash
$ project/directory/path/venv/bin/pyinstaller output.spec
```

2. Open the executable file from the dist file
```bash
$ ./dist/ONCF-chatbot
```

> The main packages of this project only supports the 3.8 version of python

> Note: This steps are only compatible with Linux

**Thank you for the internship opportunity :sunglasses:**