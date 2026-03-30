# FuturePath AI

FuturePath AI is a single-file Python desktop application that helps students explore suitable career paths based on their academic background, skills, and interests.  
The app gives users their top career matches, explains why each path fits, and suggests practical next steps to start learning.

## Overview

Choosing a career path is difficult for many students, especially when they have interests in more than one area or do not know how their strengths connect to real opportunities.  
FuturePath AI was built to make that decision easier through a simple, interactive desktop experience.

Instead of showing only a single recommendation, the app provides:

- Top 3 matching career paths
- A clear explanation for each recommendation
- Personal strengths that support the match
- Improvement areas to focus on next
- A starter roadmap for each career path

## Why This Project Matters

This project solves a real problem: many students know what subjects they like, but they do not know which career path fits them best.  
FuturePath AI turns self-assessment into actionable guidance in a way that is easy to use, easy to present, and easy to improve later.

It is also a strong portfolio project because it combines:

- Problem-solving and recommendation logic
- Python desktop GUI development
- User-centered design
- Explainable outputs instead of black-box results
- A practical education-focused use case

## Features

- Single-file implementation in Python
- Desktop GUI built with `tkinter`
- No external Python libraries required
- Clean interactive interface with sliders and dropdowns
- Scrollable layout for smaller screens
- Explainable recommendation engine
- Personalized career guidance and learning roadmap
- Can be launched by double-clicking the Python file on Windows

## Supported Career Paths

- Software Engineering
- Data Science
- UI/UX Design
- Digital Marketing
- Biotechnology
- Business Analytics

## How It Works

The user enters:

- Academic background
- Self-rating for core skills
- Self-rating for interests

The system then:

1. Compares the user profile against predefined career profiles
2. Scores how closely the student matches each path
3. Ranks the best matches
4. Generates an explanation for the top recommendations
5. Suggests a learning roadmap for each career option

This makes the application more useful than a basic quiz because it focuses on both recommendation and explanation.

## Tech Stack

- Python
- `tkinter`
- `ttk`
- `ScrolledText`

## File Structure

This final version is intentionally simple:

```text
PROJECT 1/
|-- FuturePathAI.pyw
|-- FuturePathAI.exe
`-- README.md
```

Main app file:

- `FuturePathAI.pyw`

## How To Run

### Option 1: Double-click

On Windows, double-click:

- `FuturePathAI.pyw`

This opens the desktop application directly.

### Option 2: Run from terminal

```powershell
python FuturePathAI.pyw
```

If you are using a local virtual environment:

```powershell
.\.venv\Scripts\python.exe FuturePathAI.pyw
```

## Requirements

- Python 3.x
- `tkinter` available in the Python installation

No external packages are required for the current final version.

## Example Output

The app can produce results like:

- Best matching career path
- Match score
- Reason for the recommendation
- Key strengths
- Areas to improve
- Starter roadmap

Example idea:

> You may be a strong fit for Data Science because your profile shows strong math, logic, and coding alignment, with a solid interest in technology.

## Project Strengths

- Easy to run and demonstrate
- Focused on a real student problem
- Designed with clarity and usability in mind
- Strong as a portfolio, scholarship, or CV project
- Built in a way that can be expanded into a smarter recommendation system later

