## N.B:
1. Always check mutability by reference or identity not by values.

**Numbers:**
1. Integers
2. Boolean
3. a.Real b.floating(decimal)
4. Complex

**Comprehensions**
Comprehensions are a concise way to create lists, sets, dictionaries, or generators in python using a single line of code.
e.g. filter items, transform items, create a new collection, flateen nested structures
#### Purpose:
1. cleaner code
2. faster execution

#### Types:
a. List
b. Set
c. Dictionary
d. Generator

1. List comprehension:[expression for item in iterable if condition]

2. Set comprehension:{expression for item in iterable if condition}

3. Dictionary comprehension:{expression for item in iterable if condition}

4. Generator comprehension:(expression for item in iterable if condition) -> like a stream

### Generators:
1. Useful in certain cases.
2. Replacement of functions.
3. Memory optimized.
4. Do one task at a time.(lazy evaluation)

**Keywords:** yield, next


### Decorators:
Used for decoration.
Wraps our functions with decorations. 

**Paradigm** -> Way of writing code.

### N.B.: 
1. Everything in python is an object.
2. Every object has its own entity which is known as namespace. 

#### Accessing Base Class:
1. Code duplication.
2. Explicit Call.
3. super().


##### Static methods don't need object creation.


**Class Methods:**                          **Static Methods:**
1. Receives cls(the class itself)           1. Receives no automatic first argument.
2. Operate on the class, not instance       2. Utility function related to class
3. Access to cls                            3. No access to cls
4. No access to self                        4. No access to self            


#### Concurrency:
Doing multiple tasks at the same time.(One guy switching between tasks)
e.g. One person chatting and making tea at the same time.
1. threading.Thread
2. asyncio

#### Parallelism:
Doing simultaneous tasks by more than one.(Multiple guys are engaged)
e.g. Two persons making tea at the same time.
1. multiprocessing.Process
2. concurrent.futures.ProcessPoolExecutor



**GIL- Global Intepreter Lock**


#### Thread Usecases:
1. i/o bound
2. web requests
3. disk read/write

#### Async Python:
**async def:** declare a coroutine(special function that can be paused)

**await:** Pauses execution until the result is ready.

**asyncio:** Built in python library

**Event Loop:** The egine that runs and schedule co-routines in python.

##### await: 
We have to wait but in a non-blocking way.

**Blocking:** -> time.sleep(2)
**Non-Blocking:** -> await asyncio.sleep(2)


### Pydantic:
It is a python library that gives us - 1. Data Validation, 2. Setting management

**Data Validation:**
1. Data parsing and validation.
2. API development.
3. Config management.
4. Data serialization/deserialization.


#### Advanced Nested Models:
1. Optional Nested Models
2. Mixed Data types
3. Deeply Nested Structure


### Best Practices 

##### Model organization:
1. **Define leaf models first** - Models with no dependencies
2. **Build upward** - Gradually compose more complex models
3. **Use clear naming** - Make relationships obvious
4. **Group related models** - Keep models in logical modules

##### Performance Considerations:
1. **Deep nesting impacts performance** - Keep reasonable depth
2. **Large lists of nested models** - Consider pagination(very rare)
3. **Circular references** - Use carefully, can cause memory issues
4. **Lazy loading** - Consider for expensive nested computations

##### Data Modeling Tips:
1. **Model real-world relationships** - Mirror your domain structure
2. **Use Optional appropriately** - Not all relationships are required
3. **Consider Union Types** - For polymorphic relationships
4. **Validate business rules** - Use model validators for cross-model logic 


#### Serialization:
Process of converting complex pydantic models into easier data types e.g: Python dict, JSON Strings, XML


## LLM:
-> Stands for Large Language Model.
-> Require GPU

**Definition**- LLMs are sophisticated artificial intelligence systems that are trained to understand, process and generate human language. 

*GPT -> Generative(Nature) Pre-Trained(Basis) Transformers(Reality)*

    e.g: Gemini, Claude, GPT, Mistral



Input Tokens -------> Transformers(GPT) -------> Predict the next token

**Tokens:**
-> The characters that humans used are mapped to some numbers, is known as tokens.

**Tokenization:**
-> Converting the user input into a set of numbers is known as tokenization.

-> There is also the concept of *De-Tokenization*.

**Vector Embeddings(Input Embeddings):**
-> Vector embeddings are numerical representations of data points, including text, images, and other data types, that capture their meaning and relationships.

**Positional Encoding:**
-> Adds the data about the positions of the vector embeddings.

**Self-Attention:**
-> The self-attention mechanism in Transformers allows the model to weigh the importance of different words in an input sequence when processing a single word, enabling it to capture dependencies and understand context.

**Multi-Head-Attention:**
Multi-head attention is a mechanism in Transformer models that performs the self-attention process multiple times in parallel, each with a different learned linear transformation.


#### Zero-shot Prompting:
-> The model is given a direct question or task without prior examples.

#### Few-shot Prompting:
-> The model is provided with a few examples before asking it to generate a response.


**Accuracy of few-shot prompting = 50x Accuracy of zero-shot prompting.**

#### Chain-of-Thought Prompting(CoT):
-> You add phrases like "let's think step by step" or "explain your reasoning" to your prompt. The AI will then generate a step-by-step explanation of how it arrived at the answer, rather than just the final result.

*Example: Instead of just asking "What is the answer to (10+5/2)?", you would ask "What is (10+5/2)? Let's think step by step" to get an answer that shows the order of operations.*

#### Persona-based Prompting:
-> You instruct the AI to "act as" a specific character, professional, or personality. This gives the AI a role to play, which influences how it responds.

*Example: You might start a prompt with "You are a professional historian specializing in ancient Rome. Describe the daily life of a Roman citizen".*


# Prompt Styles:

## 1.Alpaca Prompt:

### Instructions: <SYSTEM_PROMPT>\n

### Input: <USER_QUERY>

### Response:\n


## 2. ChatML Prompt: (e.g: ChatGPT, Gemini)

{
    "role": "system" | "user" | "assistant",
    "content": "string"
}


## 3. INST Prompting: (e.g: LLaMA-2)

[INST] What is the time now? [/INST]


**Ollama:**
To run AI models locally on your machines.

**N.B.:**
1. OpenWeb API
2. Ollama
3. Hugging Face -> Github of LLM models.


## Agents:
1. LLM: These are DUMB pieces of code sitting in a server taking text as input and giving text as output, i.e. it is like a human brain without a body.

2. Agents: LLM with tools is basically known as agents.


## RAG(Retrieval Augmented Generation):

**Problem 1:**
- LLM does not have context about YOUR DATA.It is basically trained on the data available over the internet.

**Problem 2:**
- You can not give large amount of context at once to the LLM, because there is a rate limiting. If you are trying to feed the LLM about 1000 files at once then it'll be very costly.

**Solution:**
- RAG

#### RAG:
RAG, or Retrieval-Augmented Generation, is an AI framework that combines the strengths of large language models(LLMs) with external knowledge sources.

**Problems of Naive Retrieval-Based Approach:**
1. Cost 
2. Context Window(e.g.:1M Token Window in GPT)

##### RAG Phases:
1. Indexing Phase -> Provide the data
2. Retrieval Phase -> CHatting with Data

#### Indexing Phase:
- Chunking(Can be in paragraph level, page level or even some characters)
- Give every chunk to an embedding model and create vector embeddings
- Store the vector embeddings in vector databases(vector DB)
- Also store the chunks and meta data(e.g. page number, source document) into the vector DB

#### Retrieval Phase:
- User gives a query
- Convert the user_query into vector embedding(by Embedding model)
- Query(Vector similarity search) into vector DB
- User got only and only relevant chunks from the DB
- Pass the relevant data as a system prompt to a chat model(e.g. GPT-5), also pass the user_query to the caht model.
- The model responds to the user.

**Vector DB examples**
1. pinecone DB
2. Chroma DB
3. pgVector
4. Qdrant DB

#### LangChain:
- It is a library that provide us a wide range of tools which we can use in our AI engineering.

#### RQ:
- RQ (Redis Queue) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry. It can be integrated in your web stack easily.

#### Multi-modal AI:
- Multimodal AI refers to artificial intelligence systems that can process and integrate information from multiple data types, or "modalities," such as text, images, audio, and video.

## LangGraph:
- A framework that helps us to build agentic workflows.

1. Build the Nodes(i.e.Functions)
2. Connect the nodes by Edges.
3. Create a state(a type of data).
4. Give the state as an input while running the graph.
5. Get the final state back as output.


## Memory of AI agents:

**Types of Memory:**
- Short-Term Memory (STM)
  -> While you are in the session.
  -> While the task is getting performed. 

- Long-Term Memory (LTM) 
  -> Stays forever.
  -> Your name.
  -> Your age.
  -> Your preferences.

e.g. Factual Memory(Facts about the user), Episodic Memory(Memory about the past interactions), Semantic Memory(General knowledge about real world)

#### Short-term Memory(STM)/ Working Memory:
Short-term memory (STM) enables an AI agent to remember recent inputs for immediate decision-making. This type of memory is useful in conversational AI, where maintaining context across multiple exchanges is required.

- For example, a chatbot that remembers previous messages within a session can provide coherent responses instead of treating each user input in isolation, improving user experience.
- For example, OpenAI’s ChatGPT retains chat history within a single session, helping to ensure smoother and more context-aware conversations.

#### Long-term Memory(LTM)/ Growing Memory:
Long-term memory (LTM) allows AI agents to store and recall information across different sessions, making them more personalized and intelligent over time.

- For example, an AI-powered customer support agent can remember previous interactions with a user and tailor responses accordingly, improving the overall customer experience.

1. Factual Memory:
- Facts about the user like name, age
- This is something always there in context

2. Episodic Memory:
- Episodic memory allows AI agents to recall specific past experiences, similar to how humans remember individual events.
- This type of memory is useful for case-based reasoning, where an AI learns from past events to make better decisions in the future.
- on Demand long-term memory

3. Semantic Memory:
- Semantic memory is responsible for storing structured factual knowledge that an AI agent can retrieve and use for reasoning. 
- Unlike episodic memory, which deals with specific events, semantic memory contains generalized information such as facts, definitions and rules.
![alt text](<image.png>)


## Graph in AI agent and Data Systems:
- Nodes(Data)
- Edges(Connection) 

**Graph is represented by the relationships between different nodes which are connected to each other by some edges.**

#### Graph can be of two types:
1. Directed Graph
2. Un-directed Graph

#### N.B.
- Graph gives us info about relationships which vector embeddings can't give.

## Voice Agents:
- User speaks to an LLM and the model gives the response by talking or in voice.

**Architectures:**
1. Speech to Speech(s2s).
2. Chained Architecture.

##### Speech to Speech(s2s):
-> Native audio handling by the model using the Realtime API.
-> Low latency.
-> Limited scope to only one agent.
-> Very expensive.
-> Unstructured Conversation.


##### Chained Architecture:
-> Speech to text(STT).
-> Pass the text to the LLM.(e.g. Gemini, Claude, OpenAI)
-> Text to Audio(TTS).


## MCP(Model Context Protocol):
- Introduced by Anthropic.

- MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.

- Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.

![alt text](mcp-simple-diagram.avif)

#### Why does MCP matter?
Depending on where you sit in the ecosystem, MCP can have a range of benefits.

- Developers: MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
- AI applications or agents: MCP provides access to an ecosystem of data sources, tools and apps which will enhance capabilities and improve the end-user experience.
- End-users: MCP results in more capable AI applications or agents which can access your data and take actions on your behalf when necessary.

#### Tools:
-> Tools let agents take actions: things like fetching data, running code, calling external APIs, and even using a computer. 

There are three classes of tools in the Agent SDK:
- Hosted tools: these run on LLM servers alongside the AI models. OpenAI offers retrieval, web search and computer use as hosted tools.
- Function calling: these allow you to use any Python function as a tool.
- Agents as tools: this allows you to use an agent as a tool, allowing Agents to call other agents without handing off to them.

1. Hosted Tools:
OpenAI offers a few built-in tools when using the OpenAIResponsesModel:

- The WebSearchTool lets an agent search the web.
- The FileSearchTool allows retrieving information from your OpenAI Vector Stores.
- The ComputerTool allows automating computer use tasks.
- The CodeInterpreterTool lets the LLM execute code in a sandboxed environment.
- The HostedMCPTool exposes a remote MCP server's tools to the model.
- The ImageGenerationTool generates images from a prompt.
- The LocalShellTool runs shell commands on your machine.

2. Function Tools:
You can use any Python function as a tool. The Agents SDK will setup the tool automatically:

- The name of the tool will be the name of the Python function (or you can provide a name)
- Tool description will be taken from the docstring of the function (or you can provide a description)
- The schema for the function inputs is automatically created from the function's arguments.
- Descriptions for each input are taken from the docstring of the function, unless disabled

3. Agent as a Tool:
In some workflows, you may want a central agent to orchestrate a network of specialized agents, instead of handing off control. You can do this by modeling agents as tools.

# 🔥 High-Impact Generative AI Project Ideas

### 1. **AI-Powered Content Creation Tool**
- **What:** Web app (React/NodeJS or JAVA backend) where users input topics, and your model generates articles, summaries, or social posts.
- **Skills:** NLP (Natural Language Processing), API integrations, UX design.
- **Bonus:** Connect to OpenAI/GPT or fine-tune a Hugging Face transformer.

---

### 2. **Image-to-Text Captioning System**
- **What:** Upload image, auto-generate a creative caption or description using a vision-language model.        
- **Skills:** Computer Vision + NLP, Flask/FastAPI backend, ReactJS UI.

---

### 3. **AI Chatbot with Personality**
- **What:** A chatbot (for web/app) with a unique & consistent personality. Use GPT-3.5/4 or open-source LLMs with parameter tweaks.
- **Skills:** Prompt engineering, API handling, frontend chat UI.

---

### 4. **Custom Style Transfer App**
- **What:** Upload two images; your app applies the "style" of one image to the content of the other.
- **Skills:** PyTorch or TensorFlow, model deployment, JavaScript frontend to preview results.

---

### 5. **AI-Based Music/Audio Generator**
- **What:** Input text prompts or parameters (e.g., mood, genre); output is generated music or soundscapes.     
- **Skills:** Use models like Magenta, Riffusion, or open-source audio LLMs. Integrate with ReactJS for UI.     

---

### 6. **Document Summarizer & Highlighter**
- **What:** Drag-and-drop PDFs or docs; AI generates summaries, highlights key points, extracts questions/answers.
- **Skills:** NLP (transformers/LLMs), RESTful APIs, frontend bookmarking or highlighting.

---

### 7. **Product Recommendation Engine (with Chat)**    
- **What:** E-commerce mini-site with conversational product recommender (uses user input, preferences, and LLM-based recommendations).
- **Skills:** LLMs (for chat), ML-based recommenders, integrating with ReactJS UI.
