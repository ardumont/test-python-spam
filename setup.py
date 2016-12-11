from distutils.core import setup, Extension

spammodule = Extension('spam', sources = ['spam-module.c'])

setup(name='spam',
      version='1.0',
      description='Spam package to demonstrate c extending python lib',
      ext_modules=[spammodule])
