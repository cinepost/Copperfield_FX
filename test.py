import os
import compy

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

## First create engine
engine = compy.CreateEngine("GPU")

## Create composition
comp = engine.createNode("img")


## Create source layer
layer1 = comp.createNode("file")
layer1.setParms({"width":1920, "height":1200, "imagefile":"~/Pictures/ava_05.png"})

## Create blur node
blur2 = comp.createNode("fastblur")
blur2.setInput(0, layer1)
blur2.setParms({"blursize":0.001, "blursizey": 0.002, "useindepy" : True})

## Create raster node
raster = comp.createNode("raster")
#raster.setInput(0, blur2)
#raster.setParms({"density":320, "quality":4})
#raster.cook()
#raster.show()

## Now create compositing node CL_Add and
#comp = comps.CLC_Comp_Add(engine)
#comp.setInput(0, layer1)
#comp.setInput(1, layer2)
#comp.cook()
#comp.show()
