# Cooperative Stacking: Distributive versus Hive Mind
## CS206: Final Project

This project was an ongoing project for a class in Evolutionary Robotics. The original codebase was
provided by Professor Josh Bongard.

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

## Week 4:

I will now reattach the Neural Network to the stacker-bots, 
each with its own neural network, and allow them to move randomly.

Notes:

 - Figured out the problem with sensors. Prepare_To-Simulate in Pyrosim is set up to create a global 
dictionary but that dictionary is still only local to a single call to pyrosim so every time a new 
urdf file is read it restarts the dictionary. What I need to do is modify robot to really just be ALL the robots.

- Update: Actually have the sensors working, it required a rather extensive dive into the pyrosim overlay
of pybullet. I can now create any number of robots and have each set of sensors respective to those robots

- I updated the motors to be able to be given their own oscillating movement

https://youtu.be/lxBY70h6j5o

Additional Tasks for Week 5:
 - Now that I have my sensors working I'm hoping to get both a neural network attached
to each individual bot and be able to run an evolutionary algorithm to make them all move in one direction
to start. I'm hoping that after this I might start searching for a good fitness function to train them to stack

Week 5:

I will create an evolutionary algorithm that rewards cooperation between the three robots. 
I will submit a video of the three robots managing to have at least one robot stacked
on top of another.

 - PHC set up and working
 - Neural network set up and working though I need to add a hidden layer to each bot
 - Hidden Layer Added
 - Laptop keeps sleeping, slowing down my runs
 - Reduced number of sensors - some body parts did not really need to sense like upper legs
 - Colored various limbs and reduced and restricted motor joints
   - created a dictionary for the various motors i.e. bottom of legs can either be straight or bent at 90 degrees
 -

TODO: 
 - Speed up evolution by changing more neurons each step?
 - Create a function that can start from specific nndf files
 - Modify fitness function to reward activation of flap sensors
   - Can i make them only sense when touching other bots?
 - Recurrent connections and CPG?

Video: https://youtu.be/m9Y3eo4ZjaI

Week 6:

Initial Goals:

I will create a new neural network for the stacker-bots which acts as a hive mind between
the three robots and allow the neurons to be created randomly so we can see the robots moving, 
I will submit a video of this.

Updated goals:
 - Move to a different evolutionary algorithm
 - Create Hive-Mind option

Extra Goals:
 - Create an info logging function, recording robot's sensor values over time. 
This is similar file for recording what constants were used in the run
 - Update algorithm to only update one robot at a time
 - Remove the sensor flaps and sensors (maybe keep top and bottom sensors for now)
This should quicken the pace of evolution (and how taxing it is on my PC)

Notes:
 - Wrapped fileread with in Wait_For_Simulation_To_End with a try except loop as lengthy runs would sometimes
crash mid-run
 - Created a new evolutionary algorithm called SurviveAndMultiply
 - currently writing a data.txt file recording some of the evolutionary constants

Video Link: https://youtu.be/z4UC5x4KG_o

Extra For Week 7:
 - Get the new evolutionary algorithm debugged
 - Create some more logging functions to see sensor patterns in the bots
 - Run some experiements to see some progress on both NN's

Week 7:

Initial Goals: I will implement a similar evolutionary algorithm and fitness function to that of 
the individual stacker bots and allow the bots controlled by a hive mind to evolve and be 
able to stack on top of each other.

Updated Goals:

Complete:
 - Fix evol algorithm
 - new fitness function that rewards topSensor being active and penalizes upside down orientation
 - Create a logging system that measures sensor inputs, center of mass, motor output, which synapses are dead
 for a single run for all robots for use in some stats and visualization

Needs Work:
 - Bots now spawn in a circle but not rotating to all have some chance finding (0, 0)

Incomplete:
 - Create some functionality to gather data every c.snapshot generations so we can try to actively witness
   evolution

Thoughts:
 - CPG
   - Perhaps A/B/C testing where I have Distributive vrs Distributive (with CPG) vrs Hivemind?
 - Repress more neurons when starting up? i.e. use a different probability distribution when setting up the arrays?
 - Have bots that lay dormant after having their topSensor pushed?

Video: https://youtu.be/HM0ujDOm-7w

Week 8:

Original Goal: This week is primarily planned for overflow as I think the previous weeks plans
are going to be challenging. If everything is going smoothly I will start testing 
how well each neural network (or set of networks) adapts to having more than three bots. 
Perhaps achieving a good metric on how well each does within a certain amount of generations.

Updated Goals:
 - Logging function:
   - Keeping track of individual and group fitnesses every generation and saving it as a .npy
     - DONE

 - Have bots "laydown" after getting within a certain distance of (0, 0), they are currently moving there slowly as not
    to pass by middle - a little malicious compliance there - the best walkers were probably walking right by the middle
   - adding a boolean state to each bot as "dormant" which should handle this
     - I should change the fitness function to reward "num bots dormant" - add this to logging function
        - DONE
 
 - Dampen the initialization of synapses
   - DONE

 - Neural network: Reduce hidden neurons but add in recurrant connections. Maybe bots could communicate over
   a long period of time by "tapping out" a signal with their touch sensors
   - Added Recurrant connections to Hive_mind and NN
     - DONE
 
- Choosing Random Synapse to modify: I need to weight the choices (recurrant connections more likely to be hit)
    - DONE

- TODO: Find a way to log a bit more info?
  - Perhaps logging the factors that went into the runs as well as the fitnesses?

Video: https://youtu.be/Zr-vIs9UX48

Next week:
 - Run simulations every night!

Week 9:

I’ll submit videos showing the results of the A/B testing as to what worked 
best: the individuals working together or the hive mind.

Best of the Distributive Minds:
https://youtu.be/mWuRHsRRrPs

Best of the Hive Minds:
https://youtu.be/jsY3wCGkDNU
