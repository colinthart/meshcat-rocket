import numpy as np
import meshcat
from meshcat import geometry as g
from meshcat import transformations as tf
import time

vis = meshcat.Visualizer()
vis.open()

vis["station"].set_object(g.Box([0.1, 0.1, 0.01]))

vis["center_of_mass"].set_object(g.Sphere(0.01))
vis["center_of_mass"]["rocket"].set_object(g.StlMeshGeometry.from_file('rocket.stl'))

duration = 5
fps = 15
frames = int(duration*fps+1)
for t in np.linspace(0.0, 1.0, frames):
    theta = np.pi/4 * t
    position = [t, t, 5*t]
    vis["center_of_mass"].set_transform(tf.translation_matrix(position))
    vis["center_of_mass"]["rocket"].set_transform(tf.rotation_matrix(theta, [0, 1, 1]))
    time.sleep(1/fps)

input("press enter to quit")