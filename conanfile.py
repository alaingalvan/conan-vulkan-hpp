#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile

class vulkansdkConan(ConanFile):

    name = 'vulkan-hpp'
    version = '1.0.17.0'
    license = 'Apache'
    url = 'git@github.com:alaingalvan/conan-vulkan-hpp.git'
    settings = ('os', 'compiler', 'build_type', 'arch')
    exports = '*'

    foldername = 'Vulkan-Hpp'
    builddir = ''

    def source(self):
        self.run('git clone https://github.com/KhronosGroup/Vulkan-Hpp')

    def build(self):
        self.builddir = os.path.join(self.conanfile_directory, self.foldername)

    def package(self):
        self.copy(pattern='*', dst='include/vulkan', src='%s/vulkan' % self.builddir, keep_path=False)
