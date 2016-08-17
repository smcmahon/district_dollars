#!/usr/bin/env python
# encoding: utf-8
"""
simplify_table.py

Created by Steve McMahon on 2010-01-06.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from types import StringTypes

from lxml import etree

badAttrs = ['style', 'class', 'border', 'cellpadding', 'cellspacing']

def main():
    
    tree = etree.parse(file(sys.argv[1]))

    root = tree.getroot()
    nodes = root.iter();
    
    row = 0
    cell = 0
    for node in nodes:
        for attr in badAttrs:
            try:
                del node.attrib[attr]
            except KeyError:
                pass
        if type(node.tag) in StringTypes:
            tag = node.tag.replace('{http://www.w3.org/1999/xhtml}','') 
            if tag == 'tr':
                row += 1
                node.attrib['class'] = 'trow%s' % row
                cell = 0
            if tag == 'td':
                cell += 1
                node.attrib['class'] = 'tcol%s' % cell
	
	
    print etree.tostring(tree).replace('&#160;', '&nbsp;')


if __name__ == '__main__':
	main()

