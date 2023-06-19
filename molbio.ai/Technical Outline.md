# Technical Outline
We trained five gpt-3.5-turbo agents with interlocking prompts and recursively chained them together. We then expose the final layer to a vectorize database of the OpenTrons API, and we return all this output to the user.

## Core App
At its heart is a Python script that relies heavily on the Langchain, Pinecone, OpenAI, and OpenTrons libraries.

Langchain lets us create the unique agents and pass one agent's output as input to the next. Pinecone is how we create and access the vectorize database. OpenAI is obviously for the LLMs and OpenTrons gives us the API to control their robots.

The five agents are set up like a tree. Layer 1 takes the user input, i.e. "Make glow in the dark E. coli," and breaks that into about three phases, "Phase 1: Find relevant genes, Phase 2: Create Plasmid, Phase 3: Integrate Plasmid, Phase 4: Test for expression." Layer 2 takes each phase and breaks it into about three steps. Layer 3 takes each step and breaks it into about three substeps. Layer 4 takes each substep and breaks into about three simple commands. The final layer, which is called AskOpenTrons and uses a slightly different langchain architecture, will use eac simple command to search for corresponding code in the OpenTrons API.

The output is returned all at once, but it is created sequentially. First we make all the phases, then we go into the first phase and list all the steps, then go into that step and list all the substeps, then go into that substep and list all the commands, then go into the command and search the API. Then we do the remaining commands. Then we go to the next substep of the first step of the first phase and do the commands. Then we go to the last substep of the first step of the first phase and do all the commands. And so on. Very slow.

If we visualize this as a tree with the user input at the top and commands as the leaves, everything that happens in the subtree of a certain node does not rely on anything outside of that subtree, so we stand to make huge time gains by doing the subtrees in parallel.

## Web Framework
In order to get this project to users, I made a Flask/React website Dockerized into three containers, one for Flask, one for React, and one for the Nginx stuff.

By default, the user goes to Port 5000 and encounters the React frontend. They submit a query and get a loading message. That query is sent to the Flask app, which sends that into the main() function from the backend script. That script does its thing and the returns a JSON object string. The Flask app takes that and returns it to the React frontend, which displays it to the user.

Pretty simple, but there's a lot of ways it could be made better.

## Future improvements
Use Celery to call the agents in parallel. Should be relatively easy and extremely helpful.
Add a Web Search agent at the start to find relevant papers, vectorize them, and use them as context. Would be difficult but could be pretty helpful.
Make it less ugly. Maybe it should be a higher priority but it's not exciting to me. Feels like grunt work, or GPT work.
