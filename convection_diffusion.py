# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 06:23:55 2018

@author: Pierre-Alexandre Tremblay
"""
import imageio
import math 
import matplotlib as mpl
import numpy as np
from PIL import Image
from sphereProjection import sphereProjection

# User-defined Variables
from config import *

# Other variables
pi2 = math.pi * 2
map_movie_file = gifFilePath + mapMovieName;
planet_movie_file = gifFilePath + planetMovieName;
background_file = rootFilePath + background_label
background_ref = Image.open(background_label).convert("RGB");

dh = 1/size
nbStepsPerPic = (nbSteps - minStepForPicture) / nbPictures

u0 = np.random.rand(size, size)
v0 = np.random.rand(size, size)

u = u0
v = v0

# Functions
def init_v():
    v =  np.sin(m_x * np.c_[0:size] / size)
    v_x = c_x * v
    w =  np.sin(m_y * np.c_[0:size] / size)
    v_y = c_y * w.transpose()
    return (v_x, v_y)

def lapl(X):
    X_c = X[0:, 0:]
    X_u = np.concatenate((X[-1:, 0:], X[:-1, 0:]), axis=0)
    X_d = np.concatenate((X[1:, 0:], X[:1, 0:]), axis=0)
    X_l = np.concatenate((X[0:,-1:], X[0:,:-1]), axis=1)
    X_r = np.concatenate((X[0:,1:], X[0:,:1]), axis=1)

    return (-4*X_c + X_u + X_d + X_l + X_r) / dh**2

def convect(X):
    X_u = np.concatenate((X[-1:, 0:], X[:-1, 0:]), axis=0)
    X_d = np.concatenate((X[1:, 0:], X[:1, 0:]), axis=0)
    X_l = np.concatenate((X[0:,-1:], X[0:,:-1]), axis=1)
    X_r = np.concatenate((X[0:,1:], X[0:,:1]), axis=1)        
    return np.multiply(v_x, (X_l - X_r)) / (2*dh) + np.multiply(v_y, (X_u - X_d))/ (2*dh)    

# Main loop
    
(v_x, v_y) = init_v()
counter = 0
map_images = []
planet_images = []
cm_blues = mpl.cm.get_cmap(cmap_name)
for k in range(nbSteps):
          
    R_u = (a * u - u**3 - sigma * v - kappa)
    u = u + dt * (d_u * lapl(u) - convect(u) + R_u) 
    
    R_v = b * (v - u)
    v = v + dt * (d_v * lapl(v) - convect(v) + R_v) 

    if (k % nbStepsPerPic) == 0 and k >= minStepForPicture:
        counter += 1
        print(counter)

        map_img_color = mpl.cm.ScalarMappable(cmap = cm_blues).to_rgba(v, bytes = True)
        map_images.append(map_img_color) 
        
        xy = pi2 * xy_r
        xz = pi2 * xz_r * counter #/ nbPictures)
        yz = pi2 * yz_r
    
        map_image_input = Image.fromarray(map_img_color)
        background = background_ref
        planet_image_output = sphereProjection(xy, xz, yz, map_image_input)
            
        background = background.resize(planet_image_output.size) #, Image.ANTIALIAS)
        planet_image_output.alpha = True
    
        background.paste(planet_image_output, (0,0), planet_image_output)
    
        planet_img = np.asarray(background)
        planet_images.append(planet_img)

        
# Make GIFs
imageio.mimwrite(map_movie_file, map_images, duration = frameDuration, subrectangles = True)
imageio.mimwrite(planet_movie_file, planet_images, duration = frameDuration, subrectangles = True)
            