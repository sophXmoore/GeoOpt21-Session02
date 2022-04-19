from flask import Flask
import ghhops_server as hs

#we also import random library to generate some randomness 
import random as r

#notice, we import another file as a library
import geometry as geo

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/network",
    name = "Create Network",
    inputs=[

    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)

def createGraph():

    G = geo.createGridGraph()

    nodes = geo.getNodes(G)
    edges = geo.getEdges(G) 

    return nodes, edges


if __name__== "__main__":
    app.run(debug=True)