#!/usr/bin/env python
#-*- coding: utf-8 -*-

import inkex

class MyExtensionName(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-x', '--something', action='store', type='string', dest='optionName',
                                     default='defaultvalue', help='Helper text for this option')

    def effect(self):
        option = self.options.optionName
        self._main_function(option)

    def _main_function(self, option):
        print 'Hello world'

if __name__ == '__main__':
    MyExtension = MyExtensionName()
    MyExtension.affect()
