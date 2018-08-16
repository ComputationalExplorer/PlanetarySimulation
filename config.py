# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 06:31:26 2018

@author: Pierre-Alexandre Tremblay
"""

a = 1.0
b = 1.0
d_u = 1e-4
d_v = 1e-4
c_x = 5e-2 
c_y = 5e-2
m_x = 20
m_y = 10

sigma = 0.5
kappa = 1e-1

dt = 0.005
size = 250 

nbSteps = 500
nbPictures = 50
frameDuration = 0.1
minStepForPicture = nbSteps / 2

gifFilePath = 'C:/Users/Admin/Documents/ComputationalExplorer/PlanetarySimulation/GIFs/'
rootFilePath = 'C:/Users/Admin/Documents/ComputationalExplorer/PlanetarySimulation/'
mapMovieName = 'map_demo.gif' 
planetMovieName = 'planet_demo.gif'
background_label = "stars.png"
cmap_name = 'Blues'

xy_r = 0
xz_r = -0.10
yz_r = 0.25 

