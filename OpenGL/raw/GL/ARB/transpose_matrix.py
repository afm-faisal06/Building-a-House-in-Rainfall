'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_transpose_matrix'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_transpose_matrix',error_checker=_errors._error_checker)
GL_TRANSPOSE_COLOR_MATRIX_ARB=_C('GL_TRANSPOSE_COLOR_MATRIX_ARB',0x84E6)
GL_TRANSPOSE_MODELVIEW_MATRIX_ARB=_C('GL_TRANSPOSE_MODELVIEW_MATRIX_ARB',0x84E3)
GL_TRANSPOSE_PROJECTION_MATRIX_ARB=_C('GL_TRANSPOSE_PROJECTION_MATRIX_ARB',0x84E4)
GL_TRANSPOSE_TEXTURE_MATRIX_ARB=_C('GL_TRANSPOSE_TEXTURE_MATRIX_ARB',0x84E5)
@_f
@_p.types(None,arrays.GLdoubleArray)
def glLoadTransposeMatrixdARB(m):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glLoadTransposeMatrixfARB(m):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glMultTransposeMatrixdARB(m):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glMultTransposeMatrixfARB(m):pass