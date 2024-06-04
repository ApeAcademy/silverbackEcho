what i did in logical order
what did i want to do
contract, test the contract (holla.py)
Test for the contract logic
wrote the bot and showed that silverback work as a listening
test it locall with anvil
 the fun part was farcast for the blog post
 
# intro
 hi my name is chris and this project is to teach you an example of how silverback can be used in a fun way. 
 
 The goal of this project is to learn how to use silverback. I wanted to use the docs and my ability to learn to figure out a way to use it. At the time, Farcast just come to my radar and I want to have some fun using. I took inspo from one of my favorite telegram channel Bear Market Screaming Therapy group. It is a channel dedicated to just audio messages of people screaming.
 
 So in a workshop session with my team, I proposed an idea of using Silverback. I got a breif understanding of what it can do. From what I understood, it can watch and trigger actions based off of certain conditions on chain.
 
HMM very interesting, so my first thought is what is a simple project that showcases this feature and what are some ideas that ive always wanted to automate. 

My first thought was make a platform that just watches the chain and notifies me on basic conditions? I've always wanted to get notified when unique happends on chain. I should make a contract and see if I can track the changes. What should I do when I see a change? I should scream into the void and have it posted somewhere. Farcast seemed like a cool place to try. 

# Breakdown
how should I break down this project?

1. Create a simple contract that accepts and withdraws eth. 
2. Create the silverback watcher to watch the logs of events.
3. Scream into the void

So I did excatly that and chose to breakdown the project into seperate files for readability. 

The file we have are:
* Holla.py
* Hollaback.py
* Echo.vy

NOTE: Hollaback.py is the main script everything is ran through this. Lets start by breaking down the puzzle pieces.

## Echo.vy
Echo.vy is the vyper contract that we are using to watch. It is a very simple contract so it is easy to understand. Silverback is going to watch the log events on chain to trigger events. More speficially, it is going to look at the amount Receueied and if it more than .01 eth. We will scream into the void. 

## Hollback.py
Hollaback.py is the Silverback App itself. Using the Silverback Documentation, we know that we start all Silverback apps with:

```python

from silverback import SilverbackApp
app = SilverbackApp()
```

from here, we are going to create a method based off of the event we want to watch. `@app.on_(my_contract.Received)`this is how we define what we are going to watch.

Based off of the Event Received, we are going to cast a message "Ah" and the number of H's are based on a equaiton `(text="A" + "H" * floor(log2(log.amount)))`

and then cast and print it out  `print(response.cast.hash)`

Now that we understand the 2 supporting pieces. Lets talk about the holla.py

## Holla.py

Holla.py is the main script. We want to setup the envioment and network we are going to play in. 
* So we saved the contract addrress of Echo.vy 
* set the network connection to ethereum:sepolia
* define the sender_account to transfer eth to the contract

in the main()
we initiate a transfer to the contract

silverback should be watching the event logs and read for the conditions.

So how does Silverback interact with holla script? there are no direct calls to the Silverback App. That is the beauty of hosting it.

You want to have 2 terminals running:
1. Termianl 1: run this command to host your Silverback App
  * `silverback run bots.hollaback:app --network ethereum:sepolia`

the base of the command is `silverback run bots.hollaback:app`

we chose to speficiy the network in the run command becasue we want to be able to run it in multiple networks without changing the core code. 

2. Terminal 2: run this command to start your holla main script:
   * ape run holla