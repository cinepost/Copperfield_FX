from process import *

# First create engine
engine = CL_Engine()

# Create two layers
#layer1 = CL_RGBA_Layer(width=64, height=64, imagefile="media/dog.jpg")
layer1 = CL_RGBA_Layer(width=128, height=128, color=(0, 0, 1, 1))
layer2 = CL_RGBA_Layer(width=128, height=128, color=(1, 0, 0, 1))

# Now create compositing node CL_Add and
comp = CL_Add(engine, background = layer1, foreground = layer2)
comp.cook()
comp.showResult()
