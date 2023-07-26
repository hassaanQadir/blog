# Avalo In Review
### Looking back on my 2023 summer at [Avalo Inc](https://www.avalo.ai/)

## Who am I?

My name is Hassaan Qadir, and I’m a Yale CS major with a heavy focus on biology. 

Last summer, I did wet-lab biology research as part of the Yale International Genetically Engineered Machines (iGEM) team. iGEM was super fun, and confirmed my interest in synbio and biotech. I also saw firsthand the bottlenecks slowing biology down, from DNA synthesis to pipetting error, and I turned my focus to the labs and companies that are working to 10x speed up biology research.

That winter, I emailed about 100 companies, and after a few companies offered me an internship for the next summer, I eventually went for Avalo Inc because I thought the work at an ML+genetics startup would be the most interesting. Good move on my part!

## My first day here

I showed up Monday morning to a futuristic biotech campus which hosted a number of biotech startups, feeling like I was stepping into the Avengers compound. Right off the bat, I was given a tour by Mariano Alvarez, the Chief Scientific Officer and the other co-founder along with Brendan Collins. He was super-friendly, and everyone welcomed me into the company from Day 1.

## Lab vs Startup

I was wondering how a startup would differ from an academic lab, but it was actually pretty similar. Everyone at Avalo is enthusiastic about working hard and getting stuff done. I’d overhear conversations about complex computational problems that’d boil down to two choices—an easy option that works for now but will blow up in somebody else’s face down the line, or a difficult option that’d require ten hours of deep thought but make things easy for everyone else—and they’d always choose the better option regardless of difficulty. Lunch conversations would go from local BBQ spots to local parasitic plants in an instant, and the office would often be buzzing with tangential conversation about bioinformatics file formats and US agricultural law.

## Leadership of Avalo

Of course, the technology itself was very interesting, and the team members enthusiasm and talent was essential for this environment to spring up, but I was often struck by the leadership of Brendan and especially Mariano, who I personally worked with more. They were both able to balance the line between providing necessary guidance and decision-making while delegating enough to allow us to be empowered over and excited about our domains. And I was really amazed by how Mariano could go from talking about the profit margins of Kraft Heinz to the ploidy of _japonica_ rice to the algorithm behind variant-calling like nothing. Seeing Brendan and Mariano breathe life into Avalo made me more certain than ever that I want to one day be a founder in my own right.

## What I actually did

My work ended up breaking into about three projects, one for each month.

The first project had to do with adding steps to the primary data pipeline of Avalo Inc. Avalo’s primary focus is taking in genetic data, running them through the functions of open source and proprietary bioinformatics libraries, and using the information to make plant breeding decisions. I personally dealt with two open source libraries, Sarek, which aligns variant calls with a reference genome, and VCFtools, which manipulates Variant Call Format files. 

Briefly, variant calls store mutation information about a particular genetic sequence accession. Old-school methods would store the entire experimentally-derived genetic sequence, i.e. aaccggtctcaa, and then we could compare that to the reference genome, i.e. aagcggtctcaa. Here we can easily see there’s a mutation in the third nucleotide, G to C. But if all we care about is mutations, then most of those letters are not relevant to us, and this issue exponentially increases when we’re dealing with millions of bases, only a few thousand of which might be meaningfully mutated. Variant calls tell us what sites are mutated and let us assume the rest matches the reference genome. It’s much more complicated than I just let on, and these libraries deal with really complex math, so I spent a while learning about these libraries and testing various functions until I finally got them to do what I wanted.

The second month was focused on understanding and working with the Nextflow software which coordinates the entire Avalo data pipeline. Nextflow is a Java-based scripting language built to automate the process of running huge data sets through multiple bioinformatics tools. Avalo works with thousands of plant genomes, which is the same throughput as hundreds of millions of bacteria genomes, so they need a robust scheduling and channeling system. Nextflow, running on AWS servers and in Docker containers, provides that, and I learned a lot about it all through the process of adding my two new bioinformatics steps into the Nextflow pipeline. The AWS and Docker familiarity will definitely transfer over to wherever I go, and a lot of the logic behind Nextflow is common to any high-throughput handler.

My final project was working with a rice genome-wide association study (GWAS) conducted by Groen et al. 2020. GWAS matches the genome of a plant to its phenotype, so we can say that XYZ genotype correlates with a more drought-resistant plant, which is what I was researching. I used the data to develop a model which allows us to sequence rice seeds and predict approximately how many grains of rice the resulting plant would yield in various conditions. Useful stuff!

## Differences between school and internship

I often compare school to my experience here, at my first real internship. I have a great time at college and learn a lot, but if I had to compare just classes to just Avalo, Avalo is certainly more educational.

Classes do a good job of teaching me about the abstract concepts and math behind CS, which is certainly nice to know, but at Avalo I’m dealing with the real bottlenecks in production software. I never thought about the idealized time complexity of any program I wrote, because here, constant-time operations don’t exist and the difference between O(3N) and O(9N) can be 18 hours. The work felt less like math, which I honestly do enjoy, and more like being a detective or a carpenter.

But where Avalo takes the medal is that every problem here is real and I am incentivized to use every tool at my disposal, whereas classwork is necessarily contrived and I’m artificially handicapped. It’s way more fun to do cutting-edge work nobody in the world has done before and nobody but me understands, rather than write an algorithm ChatGPT could provide for me instantly.

That being said, I’ve come to appreciate the structured nature of problem sets. Sometimes I would struggle just knowing where to start, but my direct supervisor, Emily Bellis, was a professor at Arkansas State University, so she was great at teaching and guiding me through my various projects.

## My plans for the future

I plan to return to Yale this fall, entering into my junior year. But it’ll be my last term for a while.

I’m taking next spring off to focus on my website molbio.ai, a project which uses LLMs to plan and conduct biology research. I think the time is now to revolutionize automation in biology research, and I plan to get at least ten users from the Yale bio labs this fall before I go full-time on molbio.ai

If things go well, molbio.ai will keep me busy for a long while, but if not, I plan to finish up my degree and probably do entry-level SWE at a FAANG… or maybe Avalo!
