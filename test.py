import engines	
import sources
import comps
import os

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

## First create engine
engine = engines.CLC_Engine()

## Create two test layers
layer1 = sources.CLC_Source_Image(engine, width=64, height=64, imagefile="media/dog.jpg")
layer1.cook()
layer1.show()

#layer2 = sources.CLC_Source_Image(engine, width=128, height=128, imagefile="media/cross.png")
#layer2.cook()
#layer2.show()

## Now create compositing node CL_Add and
#comp = comps.CLC_Comp_Add(engine, background = layer1, foreground = layer2)
#comp.cook()
#comp.show()
