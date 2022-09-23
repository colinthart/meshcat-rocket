import numpy as np
import meshcat

vis = meshcat.Visualizer()
vis.open()

vis.set_object(meshcat.geometry.Box([0.1, 0.2, 0.3]))
vis.set_transform(meshcat.transformations.rotation_matrix(np.pi/4, [0,0,1]))
vis.set_transform(meshcat.transformations.translation_matrix([1,1,1]))

input("press enter to quit")