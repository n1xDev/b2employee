#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen # FROM
import json, pg # Python's Lib's
from mydata import *

def getWallAmount(owner_id):
	address = "https://api.vk.com/method/wall.get?owner_id=" + owner_id + "&count=1&filter=owner&access_token=" + admin_token
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	wall_amount = final_data['response'][0]
	return wall_amount

def getFriendsAmount(group_id):
	address = "https://api.vk.com/method/groups.getMembers?group_id=" + group_id + "&fields=sex&access_token=" + admin_token
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	friends_amount = final_data['response']['count']
	return friends_amount

def getFollowersAmount(user_id):
	address = "https://api.vk.com/method/users.getFollowers?user_id=" + str(user_id) + "&count=0"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	followers_amount = final_data['response']['count']
	return followers_amount

def getSubscriptions(user_id):
	address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id) + "&extended=0"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	adata.subscriptions_amount = int(final_data['response']['groups']['count']) + 1
	#print(adata.subscriptions_amount)

	"""address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id) + "&extended=1&access_token=" + admin_token
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	data_length = final_data['response']
	i = 0
	for i in range(0, int(adata.subscriptions_amount)):
		print("now(get): " + str(i))"""
	#https://api.vk.com/method/users.getSubscriptions?user_id=1&extended=1&access_token=95f8c3991898c086358df460735307ef4e4e80cf516dff0e6e5dbff71308aee542469479f4e716bf71769

def getAllFromGroup(group_id, offset):
	address = "https://api.vk.com/method/groups.getMembers?group_id=" + str(group_id) + "&offset=" + str(offset) + "&count=500"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	i = int(offset)
	while i < 1000:#(int(offset) + 500):
		try:
			print("Doing while cycle with I variable... I = " + str(i))
			user_id = final_data['response']['users'][i]
			connection.query('CREATE TABLE u' + str(user_id) + ' (group_id	text,group_name	text);')
			# quantity
			"""address2 = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id) + "&extended=0"
			data2 = urlopen(address2)
			decoded_response2 = data2.read().decode()
			final_data2 = json.loads(decoded_response2)"""
			getSubscriptions(str(user_id))
			j = 0
			while j < adata.subscriptions_amount:
				print("Doing while cycle with J variable... J = " + str(j))
				address3 = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id) + "&extended=1&count=999"
				data3 = urlopen(address3)
				decoded_response3 = data3.read().decode()
				final_data3 = json.loads(decoded_response3)
				try:
					connection.query("INSERT INTO u" + str(user_id) + " VALUES(" + "'" + str(final_data3['response'][j]['gid']) + "'" + ", " + "'" + str(final_data3['response'][j]['name']) + "'" + ")")
					print("One of all groups ID: " + str(final_data3['response'][j]['gid']))
					print("One of all groups Name: " + str(final_data3['response'][j]['name']))
				except (KeyError, TypeError):
					print("Error with inserting... *79*")
				j = j + 1
		except:
			print("This table was found! *82*")
		i = i + 1
	"""if offset < 10000:
		getAllFromGroup(group_id, offset + 500)
	else:
		print("Fully done... :)")
		exit()"""