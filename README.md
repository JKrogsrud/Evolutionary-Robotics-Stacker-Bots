# Cooperative Stacking: Distributive versus Hive Mind
## CS206: Final Project

### Goal

Many organisms have learned to work together to better survive or achieve goals that an individual 
could not. I plan on trying to create a small group of robots that have a goal as a
group rather than being rewarded based off of their own sole success. I’m hoping to 
do this by having several small robots be able to stack on top of each other and create 
a tower, much like red ants do when crossing gaps. Furthermore, I want to test how successful 
these robots might evolve as individuals in a group or as something a little bit more alien:
as part of a hive mind in which their neural networks are all intertwined.

### Planning

Week 1:

I will create a new bot very much similar to a mix between the hillclimber and the quadruped. 
I hope to give it a shape that will be “stackable” but also limber enough to move climb. 
This bot will have no neural controller, so all code that simulates sensors, motors and 
neural network controller will be commented out. I’ll submit a video of a ragdoll version
of one robot and show that the joints work correctly.

Results:

Week 2:

I will create three copies of my stacker-bot with sensors and show that the robots 
stack and the sensors on robot showing that the robots can “feel” if other robots 
are stacked on them or if they are stacked on other robots. I will show a video of sensor
activations under a stacked condition. The robots will still not have any motors.

Week 3:

I will attach motors to my stacker-bots with oscillatory motion and submit a video of 
the them moving rhythmically in response.

Week 4:

I will now reattach the Neural Network to the stacker-bots, 
each with its own neural network, and allow them to move randomly.

Week 5:

I will create an evolutionary algorithm that rewards cooperation between the three robots. 
I will submit a video of the three robots managing to have at least one robot stacked
on top of another.

Week 6:

I will create a new neural network for the stacker-bots which acts as a hive mind between
the three robots and allow the neurons to be created randomly so we can see the robots moving, 
I will submit a video of this.

Week 7:

I will implement a similar evolutionary algorithm and fitness function to that of 
the induvial stacker bots and allow the bots controlled by a hive mind to evolve and be 
able to stack on top of each other.

Week 8:

This week is primarily planned for overflow as I think the previous weeks plans
are going to be challenging. If everything is going smoothly I will start testing 
how well each neural network (or set of networks) adapts to having more than three bots. 
Perhaps achieving a good metric on how well each does within a certain amount of generations.

Week 9:

I’ll submit videos showing the results of the A/B testing as to what worked 
best: the individuals working together or the hive mind.
