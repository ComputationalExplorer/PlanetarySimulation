# PlanetarySimulation

# Objective
Produce an animation of a planet that is rotating around an axis and that has a dynamic atmosphere, as seen from space.

# Methodology

The main idea is to represent the dynamics of the atmosphere using a convection-diffusion model.
This is similar to a reaction-diffusion model, which in itself is known to generate interesting patterns (such as zebra-type stripes, or dots).
But it also includes a convection term, which forces some directed movement into the patterns (to make it look like moving clouds).

This model is applied to generate patterns on a 2-d rectangular grid.
The convection terms are defined so as to be proportional to the sine of the latitude or of the longitude,
this adding some waviness to the result. The boundary conditions used are periodic in both X and Y axes, so the underlying topology is that of a torus. This is obviously physically incorrect, but does not matter so much for animation purposes.

There are 2 variables (u, v) representing the concentrations of 2 interacting substances, but we focus on only one of them in the visualizations (u).
This grid is then projected on a sphere, that is rotated for every image frame, which creates the illusion of movement.
The resulting images (both for the flat "map" and the spherical "planet") are saved as animated GIF files.

# Results

Here is an example, using the parameters from file 'config_blue_planet.py'.

The evolution of the 'u' variable on a 2-d grid (the 'map' of the planet) looks like this:
![alt text](https://github.com/ComputationalExplorer/PlanetarySimulation/blob/master/gifs/map_demo.gif "Blue planet projection")

The final result, projected on a rotating sphere :
![alt text](https://github.com/ComputationalExplorer/PlanetarySimulation/blob/master/gifs/planet_demo.gif "Blue planet demo")

Here are the corresponding animations obtained if we multiply the c_x component of the convection term by a factor of 4 (see the configuration file 'config_red_planet.py) :
![alt text](https://github.com/ComputationalExplorer/PlanetarySimulation/blob/master/gifs/map_demo_red.gif "Blue planet projection")
![alt text](https://github.com/ComputationalExplorer/PlanetarySimulation/blob/master/gifs/planet_demo_red.gif "Blue planet demo")


# References
