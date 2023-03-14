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

## Week 1:

I will create a new bot very much similar to a mix between the hillclimber and the quadruped. 
I hope to give it a shape that will be “stackable” but also limber enough to move climb. 
This bot will have no neural controller, so all code that simulates sensors, motors and 
neural network controller will be commented out. I’ll submit a video of a ragdoll version
of one robot and show that the joints work correctly.

Results:  https://youtu.be/k4eVCKiLt3E

Notes: I've given a quadruped 4 'sensor-flaps' with the aims of sensing when another bot is above or below it.
Additionally, the robot has a sensor above and below its torso. The 'sensor-flaps' can move with a joint but this may
be limited in the future. The four legs each have a small join that allows for rotation in the xy plane, like a rotator cuff
, and then two joints that serve for motion in the z direction.

Additional goals for week 2:

 - Create a function that generates the body.urdf with an x, y, and z coordinate so that the three robots can be
reproduced dynamically
 - Given some time I'd like to create another body or two so that I might choose later which body functions the best for
this experiment

Bot generated by calling search.

## Week 2:

I will create three copies of my stacker-bot with sensors and show that the robots 
stack and the sensors on robot showing that the robots can “feel” if other robots 
are stacked on them or if they are stacked on other robots. I will show a video of sensor
activations under a stacked condition. The robots will still not have any motors.

What the video shows: 

The link to the video should show that I can create one bot whose sensors all work as
expected. But when I create multiple robots they all report the exact same values as one
of the bots. This is something I need to work on for week 3. As this goal was unmet I 
am also showing that I have created functionality that can dynamically create a number
of robots of specified distance away either stacked already or horizontally for when the
experiment begins. I'm thinking this might be helpful later when attempting to train the neural
networks as I could try to train them to feel what a successful state feels like (stacked) and then
slowly spawn them apart horizontally so they can learn to achieve that last state.

Notes:

 -  I seem to have lost the ability to run through  my terminal, something to work on but results 
can still be reached without parallelization for now
 - Tweaked location flap sensors to improve connection capabilities when stacked
 - Altered height of torso to allow sensors to touch a bit easier
 - DEBUGGING: the sensors are all reporting identical values among all bots
   - I believe this has to do with a global dictionary being created by pyrosim?
       - Atempted naming of body parts of each robot to include their robotID so that the parts had unique names
         but something wasn't working there

Video of results: https://youtu.be/tGGVvboHUg4

Additional tasks for Week 3:
 - Debug the sensors so each robot does not somehow share what the last robot generated is sensing
 - Find out why I can no longer run multiple windows

## Week 3:

I will attach motors to my stacker-bots with oscillatory motion and submit a video of 
the them moving rhythmically in response.

Notes:

 - Motors Attached easily enough
 - have yet to work on other outstanding issue
 - Slow week due to spring break

Video of Results: https://youtu.be/NZ42BIrVYmo

Additional Tasks for Week 4:
 - Debug the sensors so each robot does not somehow share what the last robot generated is sensing
 - Find out why I can no longer run multiple windows

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
