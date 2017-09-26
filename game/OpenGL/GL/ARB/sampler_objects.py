'''OpenGL extension ARB.sampler_objects

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.sampler_objects to provide a more 
Python-friendly API

Overview (from the spec)
	
	In unextended OpenGL textures are considered to be sets of image
	data (mip-chains, arrays, cube-map face sets, etc.) and sampling
	state (sampling mode, mip-mapping state, coordinate wrapping and
	clamping rules, etc.) combined into a single object. It is typical
	for an application to use many textures with a limited set of
	sampling states that are the same between them. In order to use
	textures in this way, an application must generate and configure
	many texture names, adding overhead both to applications and to
	implementations. Furthermore, should an application wish to sample
	from a texture in more than one way (with and without mip-mapping,
	for example) it must either modify the state of the texture or
	create two textures, each with a copy of the same image data. This
	can introduce runtime and memory costs to the application.
	
	This extension separates sampler state from texture image data. A
	new object type is introduced, the sampler (representing generic
	sampling parameters). The new sampler objects are represented by a
	new named type encapsulating the sampling parameters of a
	traditional texture object. Sampler objects may be bound to texture
	units to supplant the bound texture's sampling state. A single
	sampler may be bound to more than one texture unit simultaneously,
	allowing different textures to be accessed with a single set of
	shared sampling parameters. Also, by binding different sampler
	objects to texture units to which the same texture has been bound,
	the same texture image data may be sampled with different sampling
	parameters.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/sampler_objects.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.sampler_objects import *
from OpenGL.raw.GL.ARB.sampler_objects import _EXTENSION_NAME

def glInitSamplerObjectsARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGenSamplers=wrapper.wrapper(glGenSamplers).setOutput(
    'samplers',size=lambda x:(x,),pnameArg='count',orPassIn=True
)
# INPUT glDeleteSamplers.samplers size not checked against count
glDeleteSamplers=wrapper.wrapper(glDeleteSamplers).setInputArraySize(
    'samplers', None
)
# INPUT glSamplerParameteriv.param size not checked against 'pname'
glSamplerParameteriv=wrapper.wrapper(glSamplerParameteriv).setInputArraySize(
    'param', None
)
# INPUT glSamplerParameterfv.param size not checked against 'pname'
glSamplerParameterfv=wrapper.wrapper(glSamplerParameterfv).setInputArraySize(
    'param', None
)
# INPUT glSamplerParameterIiv.param size not checked against 'pname'
glSamplerParameterIiv=wrapper.wrapper(glSamplerParameterIiv).setInputArraySize(
    'param', None
)
# INPUT glSamplerParameterIuiv.param size not checked against 'pname'
glSamplerParameterIuiv=wrapper.wrapper(glSamplerParameterIuiv).setInputArraySize(
    'param', None
)
glGetSamplerParameteriv=wrapper.wrapper(glGetSamplerParameteriv).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetSamplerParameterIiv=wrapper.wrapper(glGetSamplerParameterIiv).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetSamplerParameterfv=wrapper.wrapper(glGetSamplerParameterfv).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetSamplerParameterIuiv=wrapper.wrapper(glGetSamplerParameterIuiv).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
### END AUTOGENERATED SECTION