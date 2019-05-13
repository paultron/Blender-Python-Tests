import bpy

def squareFractal(x,y,sz,level):
	if level == 0:
		copy = ob.copy()
		copy.data = ob.data.copy()
		copy.location.x = x+(sz/2.0)
		copy.location.y = y+(sz/2.0)
		bpy.context.scene.collection.objects.link(copy)

	else:
		squareFractal(x,y,sz/3.0,level-1) #top left
		x += sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #top mid
		x += sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #top r

		y += sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #right mid

		y += sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #right btm
		x -= sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #btm mid
		x -= sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #btm left

		y -= sz/3.0
		squareFractal(x,y,sz/3.0,level-1) #left mid
		y -= sz/3.0 #return

fLevel = 2
#1 = 1/3
#2 = 1/9
#3 = 1/27
fSize = 1/(3**fLevel)
#create object to duplicate
bpy.ops.mesh.primitive_plane_add(size=fSize) 
ob = bpy.context.object
squareFractal(0,0,1,fLevel)
bpy.ops.object.delete() #remove original
bpy.context.scene.update() # only once
