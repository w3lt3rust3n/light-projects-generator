#! /usr/bin/env python3
# coding: utf-8

#--------------------------------------------------------------------------------------------------------------
# LPG - Light Project Manager, a simple python program for lazy web developers ;)
#
# preparator.py :
# 
# 
# CAUTION : expect unexpected behaviors on Windows machines. May work as expected under GNU/Linux systems.
# 
# Made with love by Maxence Buisson for the fun of it.
# Contact : weltrusten@philentropy.org
# 
# Enjoy !
#---------------------------------------------------------------------------------------------------------------

class Preparator:
    LPG_DIR = ".lpg/"
    CONFIG_DIR = ".lpg/config"
    
    def __init__(self, lang):
        self.lang = lang

    def __load_conf_file(self):
        pass
    
    def init_preparator(self, lang):
        print("Hello from init_preparator")