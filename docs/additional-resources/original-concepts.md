---
sidebar_position: 1
description: The concepts that were originally pitched for the 2024 Aerospace Jam.
---

# Original Concept

If you're curious (which is probably why you're here), here's the exact text of the concepts that were originally pitched for the 2024 Aerospace Jam - most of them ended up making it in, except for a few notable exceptions.

## Challenges

- Two RFID tags - one mounted on a vertical surface (e.g. about halfway up the side of the netting) and one mounted on a horizontal surface (e.g. on the top of an elevated platform) - that have to be flown to and read with an drone-mounted RFID reader (Medium)

- Two boxes arranged in parallel to each other along a center drone landing point, in which the drone must land in the middle, take one reading of distance in one direction, turn, then take another reading in the other, then add those values in the code, directly sending it back to the base - this would have to be watched to ensure that the values aren't added manually by the team (Easy-medium)

- Land at a target and read the ambient temperature (Easy)

- Read a color with an AS7341 from an elevated platform and display an approximation of it on an RGB LED array attached to the drone. For bonus points, convert it to a hex color code and display it on the base station. (Very hard)

- Measure the drone's tilt with a gyroscope - on the competition day, the drone would be placed on a tilting platform that would autonomously move to different degree measures - these measures would be checked against the measurements retrieved by the team's drone (Medium)

- Land at a target location and measure the distance to a target object (Easy)

- The same movement challenges as previous years (Medium-hard)

## Programming Guidance and Documentation

- For each challenge, produce a stub of sample code - this would introduce the required concepts, but not overtly give the solution (except in the case of easy programming tasks, or unless specifically asked).
  
- Give an example of hosting a web server on the pi itself, and an example of creating a hotspot and assigning the pi a static IP.
  
- Introduce source control, git, and git best practices.
  
- Create a barebones template for a WebUI and compatible server that can be easily extended without being too complex.
  - Emphasize that you don't need to use a WebUI - you can use any UI and any server architecture you'd like, just make it run on the pi.
  
- Create a fully-featured WebUI to demonstrate, but not release the code for.

## Judging

- Judging based on mission report would remain mostly unchanged
  
- New judging categories would be introduced:
  - Style points
    - Look and feel of app
    - Code best practices
    - Code elegance
    - Artistic expression in drone construction
    - Engineering in drone construction
