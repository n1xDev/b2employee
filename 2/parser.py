#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen # FROM
import json # Python's Lib's
import pg
from mydata import * # My local Lib's
from VkGet import *
from VkSet import *

def Main():
	#print(getWallAmount("145476098"))
	#print(getFriendsAmount("3801006"))
	#saveAllNames("3801006", "0")

	#getSubscriptions("1")
	#print("-----------------------")
	#saveSubscriptions("1")

	#getAllFromGroup("32370614", "0") #LAST

	getSubscriptions("210064990")
	DoLast("210064990")

Main()