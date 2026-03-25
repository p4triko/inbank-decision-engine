# Inbank Product Engineer Intern Test Task
## Technology used
Frontend - HTML, CSS and JS <br>
Backend - Python and FastAPI for building the API endpoint

## Prerequisites
1. pip (package installer for python) needs to installed.
2. In the terminal run the following commands:
   ```
   pip install fastapi
   ```
   ```
   pip install uvicorn
   ```
## Instructions
1. Clone the repository.
2. Open the folder in a code editor.
3. Navigate to the backend folder.
4. In the terminal run the command
   ```
   uvicorn main:app --reload
   ```
5. Open the index.html file in a browser, comfortable way is to use Live Server in VsCode.

## Process
For the frontend side I chose the vanilla approach since I'm most familiar with that. For the backend I chose FastAPI for it's simplicity and quick setup, also provided me with a chance to learn about a new technology.<br>
I first started with the neccessary base by setting up our custom domain and making sure requests done by the user side actually follow through. This part was relatively short, FastAPI provided a really quick way to set everything up. <br>
From there I started implementing the actual decision engine logic, by following the given instructions the logic behind wasn't overly complicated. I did however miss one thing at first, which I did later implement and that was approving the maximum sum. <br>
Last part was really tying it all together with the trinity, I would say that was the most difficult part of the task, because it was ultimately a process of glueing everything together. <br>

## What is one thing you would improve about the take home assignment and how would you improve it?
If I were to improve one thing, it would be the input side of things. Right now the only form of input is a slider, which does make precise inputs more difficult. In terms of implementing it there definitely needs to be some form of input validation, because
we are dealing with min and max for both the required values. The user would enter a value and then it would be ran through a filter basically to sort out all the bad.
