import engines	
import sources
import comps
import effects
import os

os.environ['PYOPENCL_COMPILER_OUTPUT'] = "1"

## First create engine
engine = engines.CLC_Engine("GPU")

## Create two test layers
#layer2 = sources.CLC_Source_Image(engine)
#layer2.setParms({"width":512, "height":512, "imagefile":"media/cross.png"})
#layer2.cook()
#layer2.show()

#blur = effects.CLC_Effect_Blur(engine);
#blur.setInput(0, layer2)
#blur.setParms({"blursize":0.05})
#blur.cook()
#blur.show()

layer1 = sources.CLC_Source_Image(engine)
layer1.setParms({"width":1920, "height":1276, "imagefile":"media/photo.jpg"})
layer1.cook()
#layer1.show()


blur2 = effects.CLC_Effect_FastBlur(engine)
blur2.setInput(0, layer1)
blur2.setParms({"blursize":0.002, "blursizey": 0.004, "useindepy" : True})
blur2.cook()
#blur2.show()

raster = effects.CLC_Effect_PressRaster(engine)
raster.setInput(0, blur2)
raster.setParms({"density":300, "dot_size":1.5})
raster.cook()
raster.show()

## Now create compositing node CL_Add and
#comp = comps.CLC_Comp_Add(engine)
#comp.setInput(0, layer1)
#comp.setInput(1, layer2)
#comp.cook()
#comp.show()
