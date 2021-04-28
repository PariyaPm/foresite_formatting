#!/usr/bin/env python

"""python_sample: this is a .py code sample
"""

__author__ = "Name Lastname"
__credits__ = ["Name Lastname", "Other_name Other_lastname"]
__version__ = "01.0"
__maintainer__ = "Name Lastname"
__email__ = "your.email@email.com"
__status__ = "Production"

import numpy as np


class TheClass:
    """TheClass does such and so 

    Attributes
    ----------
    attribute : type
        description
    other_attr : type, optional
        description (default: None)
    """

    def __init__(self,
                 attribute,
                 other_attr=None):
        
        self.attr = attribute
        self.other_attr = other_attr

    def the_function(self, another_attr):
        """
        Parameters
        ----------
        another_attr : type
            description

        Returns
        -------
        something : type
            description 
        """
        
        # TODO (name) use this codetag

        # FIXME
        
        something = another_attr
        
        return something
        
        
if __name__ == 'python_sample':
    path = '.'
    attr = 'data.txt'

    data = ClassName(attr)
