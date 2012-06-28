import sys

srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'bindings'

  obj.source = [ 'src/codec.cc', 'src/bindings.cc',
                 'alac/EndianPortable.cc', 'alac/ALACBitUtilities.cc', 'alac/ALACEncoder.cpp',
                 'alac/ag_enc.cc', 'alac/ag_dec.cc', 'alac/dp_enc.cc', 'alac/matrix_enc.cc',
                 'src/aes_utils.cc', 'src/base64.cc', 'src/CAHostTimeBase.cpp' ]

  if sys.platform == 'darwin':
    obj.cxxflags = ["-I", "/System/Library/Frameworks/Kernel.framework/Versions/A/Headers/sys"]
    obj.source.append('src/coreaudio.cc')

