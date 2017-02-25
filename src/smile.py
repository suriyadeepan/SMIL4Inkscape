#!/usr/bin/env python
#-*- coding: utf-8 -*-

import inkex

class Smile(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-s', '--some_name', action='store', type='string', dest='optionName', default='defaultvalue', help='Helper text for this option')

    def effect(self):
        option = self.options.optionName
        self._main_function(option)

    def _main_function(self, option):
        svg = self.document.getroot()
        layer = inkex.etree.SubElement(svg, 'g')

if __name__ == '__main__':
    MyExtension = Smile()
    MyExtension.affect()
