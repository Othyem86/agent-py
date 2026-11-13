# AI Agent (Python)

A command-line AI agent built in Python, powered by the OpenAI API.

## Overview

This project sets up a foundation for building an AI agent capable of interacting with large language models (LLMs). It uses `uv` for dependency and virtual environment management, keeping this project's packages isolated from other Python projects on your machine.

## Dependencies

- [openai](https://pypi.org/project/openai/) — official Python client for the OpenAI API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — loads environment variables
  (like API keys) from a `.env` file

## Setup

1. Create and activate a virtual environment:

   \`\`\`sh
   uv venv
   source .venv/bin/activate
   \`\`\`

2. Install dependencies:

   \`\`\`sh
   uv add openai==2.44.0
   uv add python-dotenv==1.1.0
   \`\`\`

3. Run the project:

   \`\`\`sh
   uv run main.py
   \`\`\`

## Status

Early setup stage — more agent functionality coming soon.