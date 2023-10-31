# Python Fastapi Development Environment with DevContainer, Docker, and Poetry

This is a basic Fastapi project setup for a Python development environment using DevContainer, Docker, and Poetry. It includes custom workspace settings for Visual Studio Code (VSCode) with a Black formatter configuration and a maximum line length of 100 characters.


## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>

2. Run .devcontainer in vscode

3. Install Poetry env and use

   ```bash
   poetry install

4. Run Server

   ```bash
   cd app
   uvicorn main:app --reload