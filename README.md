# UI-Calculator
---
A simple GUI Calculator made with python.

![image](https://user-images.githubusercontent.com/23217592/201998247-46864e88-f860-4db8-9ab9-08a03c59aea5.png)


Python UI Calculator – Docker Deployment & Migration
📘 Project Overview

This is a simple Python Tkinter-based Calculator application.
It is deployed and tested on both Windows and Linux (Ubuntu) using Docker for portability and consistency.

📁 Folder Structure
docker_lab6/
└── UI-Calculator/
    ├── calculator.py
    ├── Dockerfile
    ├── README.md

⚙️ Prerequisites

Install the following on both Windows and Linux:

Python 3.8+

Docker Desktop (Windows)

Docker Engine (Linux)

FileZilla (for file transfer / migration)

Tkinter (Linux may require installation)

🚀 Running the Application (Without Docker)
On Windows
cd C:\docker_lab6\UI-Calculator
python calculator.py

On Linux
cd ~/docker_lab6/UI-Calculator
python3 calculator.py


If you get a Tkinter error:

sudo apt install python3-tk -y


This will open the calculator GUI.

🐳 Running the Application (With Docker)
Dockerfile (Include this in project folder)
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y python3-tk
CMD ["python", "calculator.py"]

1️⃣ Build Docker Image
docker build -t ui-calculator .

2️⃣ Run Docker Container
docker run -it ui-calculator


Note: Tkinter GUI may not display inside the Docker container.
For this lab, the purpose is to show that the container builds and runs successfully.

3️⃣ Verify Container
docker ps -a

📤 Migration (Windows ➝ Linux using FileZilla)
1. Transfer Project Folder

Windows path:

C:\docker_lab6\UI-Calculator


Linux destination:

/home/student/docker_lab6/UI-Calculator

2. Verify Files on Linux
cd ~/docker_lab6/UI-Calculator
ls

3. Build & Run Again on Linux
docker build -t ui-calculator .
docker run -it ui-calculator



## Instructions

- Download the [calculator.py](https://github.com/ArjunRAj77/UI-Calculator/blob/main/calculator.py)
- Run the python file. `python calculator.py `

## Code Flow

We want to create a simple calculator with 16 buttons across 4 rows. 
<p>
Here we will be mainly utilising the `Tkinter` library by Python , which can be used to create GUI based interactions.  
  </p>
  
The GUI should of the following structure :

![image](https://user-images.githubusercontent.com/23217592/202002279-14e80053-3885-47e2-a9b4-fd5ccd3207a0.png)

- Define the buttons and its actions
- Design the UI with the Tkinter library
- Connect the UI with the button actions

## References
- [Learn more about Tkinter library](https://tkdocs.com/tutorial/) 
- [Javapoint Article on GUI Calculator](https://www.javatpoint.com/gui-calculator-using-python)
