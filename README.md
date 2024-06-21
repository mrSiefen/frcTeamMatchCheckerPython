**What is FRC Matchfinder?**

An online tool, powered by The Blue Alliance API, that will find and display information about the connections between two FRC teams based on their numbers.

**Why does it need to be an online tool?**

It doesn't! This can be run in its simplest form to find match numbers as a python script. Its not pretty and this V1 script did not print out the alliance mates as well, just the match code, event code and match type.

However, this method is not pretty, it requires you to get your own TBA API key and also have python installed and pip install the required packages... Then you can only run it from a laptop or special app. So a website will be better. The backend will move to NodeJs with an EJS frontend just like GoFundRobots.org. The difference is this time we could lease a new domain or use a subdomain for FRCzero.org or GoFundRobots.org.

To try the idea out without moving to nodeJS yet I did a python flask server

With all of that you have a mini version of what this project will look like that you can run at home yourself before the real site goes live. 

**FRC Matchfinder is a terrible name, are we stuck with it?**

No! I didn't already rush out and lease a domain without asking first! Please give me some ideas!

**Possible Features**

1. Look up match 'crossover' between any two teams
2. View detailed stats about the % of alliance color, allied/against and win/loss ratio
3. Degrees of separation if you have not played with the target team previously. @brandonmcd mentioned this idea awhile ago and I think we could tie that idea in somewhere. its brilliant.
4. Top Connections list. This would be a top 10 list for both teams submitted that shows what teams they most commonly connect with.
5. [Give me more ideas please!]

The goal is to show connections between teams and not focus on the performance metrics so please think of features along those lines. How does FRC connect us because of the game?

Thanks in advance and I will update this thread as we go along and try to include snippets of code or screenshots. This is very early into the project (i.e. day 2)
