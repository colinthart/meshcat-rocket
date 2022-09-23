import numpy as np
import meshcat
from meshcat import geometry as g
from meshcat import transformations as tf

vis = meshcat.Visualizer()
vis.open()

vis["center_of_mass"].set_object(g.Sphere(0.01))
vis["center_of_mass"]["rocket"].set_object(g.Box([0.1, 0.2, 0.3]))

vis["center_of_mass"].set_transform(tf.translation_matrix([1, 1, 1]))
vis["center_of_mass"]["rocket"].set_transform(tf.rotation_matrix(np.pi/4, [0, 0, 1]))

input("press enter to quit")