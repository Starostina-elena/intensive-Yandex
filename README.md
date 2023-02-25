![](https://img.shields.io/github/actions/workflow/status/Starostina-elena/intensive-Yandex/.github/workflows/python-package.yml?style=flat-square)

# intensive-Yandex
How to run the project in dev mode:

1_1. Run in console following lines (for Linux):

    git clone https://github.com/Starostina-elena/intensive-Yandex.git (cloning github repo to your device)
    cd intensive-Yandex (moving to the directory with project)
    python3 -m venv venv (creating virtual enviroment)
    source venv\bin\activate (activating virtual enviroment)
    python3 -m pip install --upgrade pip (updating pip)
    pip3 install -r requirements\requirements.txt (installing packages required for running project)
    pip3 install -r requirements\requirements-dev.txt (installing packages required for development)
2_1. Create file .env and fill parameters like in the file .env.example

3_1. Run in console:

    cd django_3_2_15 (changing directory to the one which contains main project file)
    python3 manage.py runserver (starting the server)

1_2. Run in console following lines (for Windows):

    git clone https://github.com/Starostina-elena/intensive-Yandex.git (cloning github repo to your device)
    cd intensive-Yandex (moving to the directory with project)
    python -m venv venv (creating virtual enviroment)
    venv\Scripts\activate (activating virtual enviroment)
    python -m pip install --upgrade pip (updating pip)
    pip install -r requirements\requirements.txt (installing packages required for running project)
    pip install -r requirements\requirements-dev.txt (installing packages required for development)
2_2. Create file .env and fill parameters like in the file .env.example 

3_2. Run in console:

    cd django_3_2_15 (changing directory to the one which contains main project file)
    python manage.py runserver (starting the server)

4. Go on link you got in console to view the work of the program
  
