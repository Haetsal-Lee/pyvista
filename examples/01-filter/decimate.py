"""
Decimation
~~~~~~~~~~

Decaimate a mesh

"""
# sphinx_gallery_thumbnail_number = 4
import pyvista as pv
from pyvista import examples

mesh = examples.download_face()

# Define a camera potion the shows this mesh properly
cpos = [(0.4,-0.07,-0.31), (0.05,-0.13,-0.06), (-.1,1,0.08)]
dargs = dict(cpos=cpos, show_edges=True, color=True)

# Preview the mesh
mesh.plot(**dargs)

###############################################################################
#  Now let's define a target reduction and compare the
# :func:`pyvista.PolyData.decimate` and :func:`pyvista.PolyData.decimate_pro` filters.
target_reduction = 0.7
print('Reducing {} percent out of the original mesh'.format(target_reduction * 100.))

###############################################################################
decimated = mesh.decimate(target_reduction)

decimated.plot(**dargs)


###############################################################################
pro_decimated = mesh.decimate_pro(target_reduction, preserve_topology=True)

pro_decimated.plot(**dargs)


###############################################################################
# Side by side comparison:

p = pv.Plotter(shape=(1, 3))
p.add_mesh(mesh, **dargs)
p.add_text('Input mesh', font_size=24)
p.camera_position = cpos
p.reset_camera()
p.subplot(0,1)
p.add_mesh(decimated, **dargs)
p.add_text('Decimated mesh', font_size=24)
p.camera_position = cpos
p.reset_camera()
p.subplot(0,2)
p.add_mesh(pro_decimated, **dargs)
p.add_text('Pro Decimated mesh', font_size=24)
p.camera_position = cpos
p.reset_camera()
p.link_views()
p.show()
