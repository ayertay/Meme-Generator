# Meme Generator

A multimedia application to dynamically generate memes.

## Overview

Project allows user to generate memes using a web and/or console application. 

## Instructions

Following the instruction to deploy the application on local computer.

### Requirements

Install dependencies with:

```
pip install -r requirements.txt
```

### For Linux/Mac

Install xpdf by running:

```
sudo apt-get install -y xpdf
```

### For Windows

Install xpdf from [Xpdf Reader](https://www.xpdfreader.com/pdftotext-man.html)

### Application

Start the application by running:

```
python app.py
```

Access the application at http://localhost:5000/

## Sub-modules

----

### QuoteEngine

Module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author.

### QuoteEngine Dependencies

[pandas](https://pypi.org/project/pandas/)

[python-docx](https://pypi.org/project/python-docx/)

[pdftotext](https://www.xpdfreader.com/pdftotext-man.html)

----

### MemeEngine

Module is responsible for manipulating and drawing text onto images.

### MemeEngine Dependencies

[pillow](https://pypi.org/project/Pillow/)