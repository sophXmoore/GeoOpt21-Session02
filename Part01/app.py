from flask import Flask
import ghhops_server as hs

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createBuilding",
    name = "Create Building",
    inputs=[
        hs.HopsCurve("Curve", "C", "closed planar curve to represent building outline", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Story height", "H", "Story Height", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("Number of stories", "S", "Number of stories", hs.HopsParamAccess.ITEM),

    ],
    outputs=[
       hs.HopsBrep("Story masses","SM","Story masses as volumetric breps", hs.HopsParamAccess.LIST),
    ]
)
def CreateBuilding(baseGeom,sH,nS):

    extrusions = []
    
    for i in range(nS):
        vector =  rg.Vector3d(0,0,sH*i)
        base = rg.Extrusion.Create(baseGeom, sH, True)
        baseCopy = base.Duplicate()
        baseCopy.Translate(vector)
        extrusions.append(baseCopy)

    return extrusions


if __name__== "__main__":
    app.run(debug=True)