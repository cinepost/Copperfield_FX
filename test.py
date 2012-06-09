import engines	
import sources
import comps
import effects
import os

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

## First create engine
engine = engines.CLC_Engine("GPU")



## Create source layer
layer1 = sources.CLC_Source_Image(engine)
layer1.setParms({"width":1920, "height":1276, "imagefile":"media/photo.jpg"})


blur2 = effects.CLC_Effect_FastBlur(engine)
blur2.setInput(0, layer1)
blur2.setParms({"blursize":0.002, "blursizey": 0.004, "useindepy" : True})

raster = effects.CLC_Effect_PressRaster(engine)
raster.setInput(0, blur2)
raster.setParms({"density":320, "quality":3})
raster.cook()
raster.show()

## Now create compositing node CL_Add and
#comp = comps.CLC_Comp_Add(engine)
#comp.setInput(0, layer1)
#comp.setInput(1, layer2)
#comp.cook()
#comp.show()
