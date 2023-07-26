# July 2023 Outline

## Vision — What’s the point of molbio.ai?
### The brain behind syn-bio
In the long-term, ~10 years, I believe molbio.ai or something like it will be able to handle reasoning at every step of a biology project, from outlining a research project to conducting assays to analyzing data to storing results in a lab notebook, left and right, forwards and backwards. 

Tomorrow’s undergrads will do the work of today’s PhDs, tomorrow’s PhDs will publish like today’s PIs, tomorrow’s PI’s will be as prolific as today’s departments, and the scientific output of humanity will 10x. And even in 2033, we’ll be sitting at the foot of the tree of life, scratching our heads at its beautiful complexity. 

But the main thesis is that current technology, current LLMs and modeling and lab automation, is technically sufficient for >80% of all lab-work, and it’s only a question of putting 2 and 2 together to make 4. How do we get there?
### The tree
![image](https://github.com/hassaanQadir/blog/assets/86531769/f014df8e-804b-49d7-81b2-4a99144f29bf)

I visualize this field as a tree opening downwards. The root is the title of the research project. It’s children are phases, who have children and so on until it’s broken down into specific movements. Go to NCBI, look up _BRCA2_… fill the pipette, shake the well, etc.

This was the thesis behind molbio.ai v1.0.0. Take the root and recursively build out the whole tree using a few simple one-shot-trained LLMs.

I am confident we will be able to handle this whole tree with almost no human input by 2038, but as anyone who used molbio.ai v1.0.0 knows, we aren't fully there yet.
### Start with nodes and subtrees, ultimate goal is the root

So how do we make something useful? We’ll go bottom up. Start by filling up nodes and once all the children have been implemented, the parent node is pretty easy to stitch together. 

If you’re feeling clever, maybe go directly for a parent node and you’ll get all the children implemented in one fell swoop, but by keeping it small, by building out features to implement small subtrees, we can keep providing useful features, getting users, and course-correcting off feedback until we complete the whole tree i.e. wet-lab singularity.
## Near-term goals — How will I get there?
### Leave of absence
I plan to take the Spring 2024 term off of Yale. I’ll have three terms to go. Yale allows undergrads to take 4 terms off, no questions asked, and even if I take more than 4 terms off, I can always rejoin after writing a short essay and being approved by a mysterious council of elders.

Most likely, I will also take the following term, Fall 2024, off as well. It’s futile to plan beyond that point.
### Users users users
The most important thing, the sine qua non, is getting users. What is a user? Do they pay? How often do they use it? Good questions that deserve further consideration.

But for now, let’s just say it’s someone who, at least monthly, visits the site, runs at least one of the components, and copies the output for their own purposes. I want them to pay $10 a month but honestly we’ll start out for free, at least while the website is ugly.

 My imagined user persona is a PhD or an undergrad in an academic wet-lab, maybe an industry wet-lab too. These are all hypotheses that will be verified through the pursuit of users.
### Cofounder
Next most important thing is to get a cofounder. I have two particular friends at Yale who would be great, but they are on the fence right now because they are not insane. Hopefully they join, because it’ll be hard to stay motivated and focused without a cofounder. I’m sure getting users will really help with this.
### Money
There is so, so, so much work to be done, which is good because that means the opportunity is huge, but even if I typed 24/7, there’d be more to do. Would be pretty nice to get money to hire full-time engineers, especially people who know SWE best-practices and can do frontend, because that ain’t me. Again, getting users will make this easy.
## Metrics for success and failure — When have I succeeded? When should I return to school?
### 10 users by 2024 or I quit
This means if I don’t get 10 users by the end of my Fall 2023 term, that’s game over. I won’t drag this out into an ignominious death, either we’re grinding molbio.ai or we’ve moved on to the next project.
### 1000 users or $100,000 in funding by 2025 or I quit
I have no idea if this is a bold or cautious goal. Assuming molbio.ai survives into Spring 2024, I’ll have a much better idea of what metrics and goals to set.
## Next steps — What i’m working on right now
### Wrapping up the askOpenTrons MVP
These are the nodes on the right side of the tree, automating out specific liquid-handling protocols. I made an MVP which takes a human protocol and writes a Python OpenTrons protocol. 

It’s barely an MVP because it’s barely useful. 

I’ll put in a few more days of work smoothing out some kinks and spreading the word, but if I don’t get any demonstrated interest, I’m going to switch to something else because I think most of the low-hanging fruit here has already been plucked by OpenTrons themselves, good for them.
### Starting work on the askNCBI MVP

Basically make an LLM agent that can interact with the NCBI API super easily. Users should be able to say, “Give me the gene sequences and amino acid sequences of dihydrodaidzein for every bacteria species it is found in,” and they should just get what they want.

Given that NCBI has an API publicly available, this looks like low-hanging fruit. Idk how good the API is though. It could be super great or catastrophically bad.
