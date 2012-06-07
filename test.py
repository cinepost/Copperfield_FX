import engines	
import sources
import comps
import os

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

## First create engine
engine = engines.CLC_Engine()

## Create two test layers
layer2 = sources.CLC_Source_Image(engine, width=512, height=512, imagefile="media/cross.png")
layer2.cook()
#layer2.show()

layer1 = sources.CLC_Source_Image(engine, width=3072, height=1536, imagefile="media/grace-new.exr")
layer1.cook()
#layer1.show()

## Now create compositing node CL_Add and
comp = comps.CLC_Comp_Add(engine, background = layer1, foreground = layer2)
comp.cook()
#comp.show()
