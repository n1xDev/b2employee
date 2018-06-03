#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, vk_api, json
from urllib.request import urlopen
import data

def main():
	""" Starting main Daemon """
	print("Daemon started.")
	mylogin = "+"
	mypassword = ""
	vk_session = vk_api.VkApi(mylogin, mypassword)

	try:
		vk_session.authorization()
	except vk_api.AuthorizationError as error_msg:
		print(error_msg)
		return

	vk = vk_session.get_api()

	response = vk.wall.get(count=1)  # Используем метод wall.get

	if response['items']:
		wall_amount = response['items'][0]
		print(wall_amount)


main()
