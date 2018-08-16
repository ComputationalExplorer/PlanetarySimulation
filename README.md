# PlanetarySimulation

# Objective
Produce an animation of a planet that is rotating around an axis and that has a dynamic atmosphere, as seen from space.

# Methodology

The main idea is to generate the dynamics of the atmosphere using a convection-diffusion model.
This is similar to a reaction-diffusion model, which in itself is known to generate interesting patterns.
But it also includes a convection term, in order to force some movement into the patterns.

This model is applied to generate patterns on a 2-d rectangular grid.
The convection terms are defined so as to be proportional to the sine of the latitude or of the longitude,
this adding some waviness to the result.
There are in fact 2 variables, by we focus on only one of them in the visualizations.
This grid is then projected on a sphere, that is rotated for every image frame, which creates the illusion of movement.
The resulting images (both for the flat "map" and the spherical "planet") are saved as animated GIF files.

# Results

Here is an example, using the parameters from file XYZ.

Without any convection term, the map is :

Now, adding a convection term (with params ABCD), we get instead :

![alt text](https://github.com/ComputationalExplorer/PlanetarySimulation/gifs/map_demo.gif "Blue planet projection")

The final result, projected on a rotating sphere :

![alt text](https://github.com/ComputationalExplorer/PlanetarySimulation/gifs/planet_demo.gif "Blue planet demo")

# References
