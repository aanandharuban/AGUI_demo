# AG-UI Python Demo

A minimal demonstration of building an AI Agent UI using the AG-UI SDK with a Python backend and a TypeScript frontend.

This project showcases how AG-UI enables real-time communication between a user interface and an AI agent through standardized agent events, including streaming responses and agent state updates.

---

## Overview

The purpose of this demo is to demonstrate:

- AG-UI SDK integration
- Python-based agent backend
- TypeScript frontend client
- Real-time response streaming
- Standardized agent communication protocol
- Event-driven architecture

Unlike traditional chat applications that rely on custom WebSocket event formats, AG-UI provides a standard protocol for communication between agents and user interfaces.

---

## Architecture

```text
┌────────────────────┐
│    Frontend UI     │
│     index.ts       │
└─────────┬──────────┘
          │
          │ AG-UI Events
          │
┌─────────▼──────────┐
│   Python Server    │
│     server.py      │
└─────────┬──────────┘
          │
          ▼
      AI Agent
```

---

## Project Structure

```text
project/
│
├── server.py
├── index.ts
├── requirements.txt
├── package.json
└── README.md
```

---

## Features

### Implemented

- User message handling
- Agent response generation
- AG-UI event streaming
- Real-time updates
- TypeScript frontend integration
- Python backend integration

### Demonstrated Concepts

- Agent communication
- Event-driven architecture
- Streaming responses
- Frontend-backend separation
- AG-UI protocol usage

---

## Technologies Used

### Backend

- Python
- FastAPI
- AG-UI SDK

### Frontend

- TypeScript
- AG-UI Client SDK

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd <project-folder>
```

---

## Backend Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python server.py
```

or

```bash
uvicorn server:app --reload
```

Server will run on:

```text
http://localhost:8000
```

---

## Frontend Setup

Install dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm start
```

or

```bash
npm run dev
```

---

## Communication Flow

```text
User Input
     │
     ▼
Frontend (index.ts)
     │
     ▼
AG-UI Request
     │
     ▼
Python Server
     │
     ▼
Agent Processing
     │
     ▼
AG-UI Events
     │
     ▼
Frontend Update
```

---

## Example Workflow

```text
User:
Hello

Frontend:
Sends request to server

Server:
Processes message

Agent:
Generates response

Frontend:
Displays streamed response
```

---

## AG-UI Event Lifecycle

```text
Message Received
        │
        ▼
Agent Started
        │
        ▼
Content Streaming
        │
        ▼
Message Completed
```

This allows the UI to display responses incrementally rather than waiting for the entire response to be generated.

---

## Why AG-UI?

AG-UI provides a standardized approach for building agent-based applications.

Benefits include:

- Standard event format
- Real-time streaming support
- Reduced frontend complexity
- Framework interoperability
- Improved developer experience

---

## AG-UI vs Traditional Communication

| Feature | AG-UI | Custom WebSocket |
|----------|--------|-----------------|
| Streaming Support | ✓ | ✓ |
| Standard Protocol | ✓ | ✗ |
| Agent Events | ✓ | Custom |
| Tool Events | ✓ | Custom |
| State Updates | ✓ | Custom |
| Interoperability | ✓ | ✗ |

---

## Learning Objectives

This demo helps understand:

- AG-UI architecture
- Agent-to-UI communication
- Streaming event handling
- Python backend integration
- TypeScript frontend integration
- Event-driven application design

---

## Future Enhancements

- Tool calling support
- Multi-agent workflows
- Conversation memory
- Authentication
- Database integration
- MCP integration
- Advanced UI components

---

## References

- AG-UI Documentation
- FastAPI Documentation
- TypeScript Documentation

---

## License

This project is intended for educational and demonstration purposes.
