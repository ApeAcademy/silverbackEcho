# what i did in logical order
# what did i want to do
# contract, test the contract (holla.py)
# Test for the contract logic
# wrote the bot and showed that silverback work as a listening
# test it locall with anvil
# the fun part was farcast for the blog post
# 


"H" * int(math.log_2(log.amount))

# what i did in logical order
# what did i want to do
# contract, test the contract (holla.py)
# Test for the contract logic
# wrote the bot and showed that silverback work as a listening
# test it locall with anvil
# the fun part was farcast for the blog post
# 
 

 hi my name is chris and this project is to teach you an example of how silverback can be used in a fun way. 
 
 The goal of this project is to learn how to use silverback. I wanted to use the docs and my ability to learn to figure out a way to use it. At the time, Farcast just come to my radar and I want to have some fun using. I took inspo from one of my favorite telegram channel Bear Market Screaming Therapy group. It is a channel dedicated to just audio messages of people screaming.
 
 So in a workshop session with my team, I proposed an idea of using Silverback. I got a breif understanding of what it can do. From what I understood, it can watch and trigger actions based off of certain conditions on chain.
 
HMM very interesting, so my first thought is what is a simple project that showcases this feature and what are some ideas that ive always wanted to automate. 

My first thought was make a platform that just watches the chain and notifies me on basic conditions? I've always wanted to get notified when unique happends on chain. I should make a contract and see if I can track the changes. What should I do when I see a change? I should scream into the void and have it posted somewhere. Farcast seemed like a cool place to try. 

how should I break down this project?

1. Create a simple contract that accepts and withdraws eth. 
2. Create the silverback watcher to watch the logs of events.
3. Scream into the void

So I did excatly that and chose to breakdown the project into seperate files for readability. 

The file we have are:
* Holla.py
* Hollaback.py
* Echo.vy


Holla is the main script that interacts with the contract by initiating a transfer of eth to the contract.

 