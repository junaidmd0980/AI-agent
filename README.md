# AI Coding Agent

A lightweight, experimental coding agent built in Python that uses an LLM to inspect, edit, and run code within a local project workspace.

## Disclaimer

> [!CAUTION]
> This project is a **toy agent** built for educational purposes. It executes code and performs file modifications with minimal sandboxing. Do **not** run this agent on critical files, production systems, or untrusted inputs. Always commit your work before letting the agent modify a repository.

## Overview

This agent acts as an autonomous coding assistant capable of interacting with the file system and running shell/Python commands to diagnose issues, refactor code, and implement features based on natural language instructions.

## Features

- **LLM-Powered Tool Calling**: Connects to an LLM provider (such as OpenRouter) to decide actions iteratively.
- **File System Operations**: Reads from and writes to files inside the workspace.
- **Execution**: Runs Python scripts and test commands to inspect runtime output and errors.
- **Agent Loop**: Continues execution until the requested task is fulfilled or stopped.

## Getting Started

### Prerequisites

- Python 3.10+
- An API key from [OpenRouter](https://openrouter.ai/) (or your preferred LLM provider)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/junaidmd0980/AI-agent
   cd AI-agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables:
   ```bash
   cp .env.example .env
   # or export OPENROUTER_API_KEY directly
   ```

5. Add your API key inside `.env`.

### Usage

Run the agent from your terminal:
```bash
python3 main.py "Fix the failing test in tests/test_calc.py"
```
