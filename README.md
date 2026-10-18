# STUDENT REPORT ANALYZER --  A MINI PROJECT MADE USING NUMPY --
A Python project that uses Numpy to read a csv or text file to find out the students who have failed. It averages out the grades 
of each student and then uses a pre-defined criterion to decide whehter the student passes the exam or not.

## Features
- Load CSV data from a file named data.txt 
- Calculates averages of each student using .mean().
- Then uses the boolean conditioning to decide the outcome.
- Outputting the names of the students failed.

## Technologies Used
- Python 3
- NumPy

## Project Structure
student-grade-analyzer/
├── data.txt
└── student_report_analyzer.py

## Requirements 
- Python 3.10 or later
- NumPy
 
## Installation
1. clone the repository: git clone <url>
2. Navigate to the project directory: cd student_report_analyzer
3. install numpy: python -m pip install numpy

## Usage 
Run the program.
python main.py
Make sure data.txt is present in the project directory and follows the expected CSV format.

## Example input
![Program Input](sccreenshots/input.png)

## Example output
![Program Output](screenshots/output.png)
 
## Concepts Used:
- Used Numpy .mean()
- Also used Boolean Conditoning.
- Used .loadtxt() to load csv file.
- learned about the subtleties of using these functions.
 
