# Premise
The main project I'm working on is a multi-LLM agent that'll take in a user's bio research project, tell you exactly how to do it, step-by-step, pipette by pippette, and program a lab robot to do as much of it as currently possible.

## Bio lab work sucks
I had this idea because last summer I did wet-lab bio research, and while the project was super interesting, I didn't like spending all day pipetting cloudy water back & forth and crossing my fingers to get good squiggles the next week. Obviously that's an uncharitable description, and it was very satisfying when things worked out, but I just knew there had to be a better way.

## ChatGPT can do very well breaking down a bio project
I noticed that GPT-3.5-turbo and GPT-4 are pretty good at taking a bio project and breaking it down into steps that fit together with little hallucination. It does require chaining together a bunch of prompts and queries.

## Lab automation APIs
I also noticed that OpenTrons, a major lab robot company, has open-sourced their Python API to control their robots, and if I introduced it as context for ChatGPT, we could break down a bio project into specific OpenTrons API calls.

## Future
OpenTrons has talked about using LLMs with their APIs, and Boiko et al. 2023 used LLMs to conduct a lab research project. This definitely seems like an opportunity and I should chase it. And yet, the applications and the leetcode and eventually the classes too, they're knocking at my door.

