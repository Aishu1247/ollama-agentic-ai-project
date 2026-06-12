# Ollama Agentic AI Project

## Overview

This repository documents my journey of building AI agents locally using Ollama and Python.

The project begins with a simple interaction with a local Large Language Model (LLM) and progressively evolves into an agentic AI system featuring memory, prompt engineering, reasoning, tool calling, and multi-tool execution.

The goal of this project was to understand how modern AI agents work internally before moving to higher-level frameworks such as LangChain.

---

## Technologies Used

* Python
* Ollama
* Qwen 2.5 3B
* TinyLlama
* Prompt Engineering
* ReAct (Reasoning + Acting)
* Tool Calling
* JSON Parsing
* Agent Architecture

---

## Project Evolution

### 1. hello.py

Basic interaction with local Ollama models.

### 2. chatbot.py

Simple conversational chatbot implementation.

### 3. memory_chatbot.py

Introduces conversation memory using chat history.

### 4. system_agent.py

Demonstrates system prompts for controlling assistant behavior and personality.

### 5. react_agent.py

Implements the ReAct (Reasoning + Acting) framework using:

* THOUGHT
* PLAN
* ACTION
* FINAL ANSWER

### 6. tool_agent.py

Introduces tool-calling capabilities, including:

* Current Time Retrieval
* Mathematical Calculations
* Word Counting
* Quiz Generation

### 7. smartai.py

Final SmartBuddy AI implementation featuring:

* Conversation Memory
* Tool Registry
* Dynamic Tool Selection
* JSON-Based Tool Calls
* JSON Recovery & Error Handling
* Multi-Tool Architecture
* Structured Responses

---

## Key Concepts Explored

* Local LLM Deployment
* Prompt Engineering
* Conversation Memory
* ReAct Reasoning
* Tool Calling
* Agent Workflows
* Dynamic Tool Execution
* Multi-Step Reasoning
* AI Assistant Design

---

## Example Agent Workflow

User Query

↓

Model Reasoning

↓

Tool Selection

↓

Tool Execution

↓

Tool Result

↓

Final Natural Language Response

---

## Learning Outcomes

Through this project I gained hands-on experience with:

* Building AI applications locally using Ollama
* Designing and managing conversation memory
* Implementing ReAct reasoning patterns
* Creating and registering custom tools
* Parsing and validating structured JSON outputs
* Building tool-calling agents from scratch
* Understanding the foundations of agentic AI systems

---

## Future Improvements

* Weather Tool Integration
* Web Search Tool
* Voice Assistant Integration
* LangChain-Based Agent Framework
* Multi-Agent Collaboration
* RAG (Retrieval-Augmented Generation)

---

## Models Used

* Qwen 2.5 3B
* TinyLlama

---

## Author

Aishwarya Manoj Nair

