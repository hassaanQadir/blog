# Process
I actively worked on molbio.ai for about a week to get the public beta out, then I stepped back a week to focus on other stuff, and now I'm traveling around with my family, but I do need to get back on the horse.

## Research by Osmosis
For a couple weeks before, I was doing research by osmosis, watching random youtube videos and reading random articles about LLMs. I found James Briggs, who makes amazing LLM and Langchain tutorials and overviews. He seems to be affiliated with Pinecone, and I do love when companies advertise by providing extremely-helpful content. I was kind of procrastinating on getting started until the Google Summer 2024 internship application opened up and I realized I needed to get my resume from zero to hero ASAP.

## Building out the core app
First step was to build on the core Python script on Google Colab, based largely off tutorial documents provided by James Briggs. I also used a lot of ChatGPT to learn and troubleshoot. ChatGPT remained an invaluable aide throughout this whole process.

## Developing the web framework
Once I got the script running on Colab, which took about three nights of work, I set up a Digital Ocean Droplet, basically a virtual machine, and SSH'd into it to develop the Flask/React app and to add finishing touches to the core script. This was a lot of work, probaby four nights of work, more than I'd expected. Docker, frontend, and server stuff is harder than it looks, but now I have a pretty good understanding of it all.

# Domain DNS
Once I got it running on local host, I used the molbio.ai domain I'd bought and edited the DNS records to point it to my Droplet. There was some confusion here, and this step really mixed a lot with the prior step, but it all worked out.

# Future Work
I think after I parallelize the main script, I may put a pin in it and focus on leetcode and my internship. That being side, molbio.ai is definitely the most fulfilling work I'm doing, and it could become something big. In that case, I'd want to keep grinding and iterating as fast as possible. I'll have to think about it.
