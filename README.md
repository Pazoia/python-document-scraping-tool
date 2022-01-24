[![Scraping Tool](https://github.com/Pazoia/python-document-scraping-tool/actions/workflows/scrapingtool.yml/badge.svg)](https://github.com/Pazoia/python-document-scraping-tool/actions/workflows/scrapingtool.yml)

# Document Scraping Tool

## Table of Contents

- [Client requirements](#client-requirements)
- [Technologies](#technologies)
- [How to run program](#how-to-run-program)
- [Project Status](#project-status)

## Client requirements

> We spend a lot of time getting useful stuff out of documents. Usually a word or two, perhaps a sentence or paragraph. For this task, we’d like you to show us how you would do something similar!

> We’ve attached a few documents, each of which has lots of words and sentences. For this task, produce a list of the most frequent interesting words, along with a summary table showing where those words appear (sentences and documents).

> This task can be tackled in any way you feel best solves the problem; feel free to show off your prowess! Our only “rule” is that you write your solution in Python, since that’s the main language we use at Eigen. Otherwise, please include instructions to help us get up and running with your code!

**Input**  
Given document **x** and document **y**

**Output**

| Word(Total Ocurrences) | Documents |                                  Sentences containing the word                                  |
| :--------------------: | :-------: | :---------------------------------------------------------------------------------------------: |
|     Philosophy(42)     |   x, y    | ["I don't have time for **philosophy**", "Still, her pay-as-you-go **philosophy** implies it."] |

> You can be creative with the output, so feel free to format in whatever way you feel best fits your solution!

## Technologies

- Python 3.8  
  [Installation instructions](https://www.python.org/)

- Pytest 6.2

## How to run program

> It's good practice to work on a virtual environment with it's own depencies and packages.

1 - To create a virtual environment on your machine follow the commands below:

```
$ python3 -m venv <env_name>
```

2 - Activate the newly created environment:

```
$ source <env_name>/bin/activate
```

You should see the env_name now on your terminal like in the shown example

```
(<env_name>) [computer:~/projects/pazul-game]$
```

### **Dependencies**

> To install all dependencies saved in the requirements.txt file in your virtual environment run the command below:

```
$ pip install -r requirements.txt
```

### **Pytest**

> Run the following command in your command line to run all the tests in the project:

```
$ pytest
```

## Project Status

> To Do's

- Create skeleton structure with module folders and files
- Add data files to project
- Get data from files

> Done

- Start project
- Install and activate virtual environment
- Add .gitignore file
- Initialize git repository
- Add GitHub Actions to repository
