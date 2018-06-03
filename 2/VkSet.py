#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen # FROM
import json, pg
import psycopg2
from mydata import *
from VkGet import *

def saveAllNames(group_id, offset):
	offset = int(offset)
	address = "https://api.vk.com/method/groups.getMembers?group_id=" + group_id + "&fields=sex&access_token=" + admin_token + "&count=1000"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	i = offset
	for i in range(offset, offset + 998):
		tmp_a = final_data['response']['users'][i]['uid']
		tmp_b = getFollowersAmount(final_data['response']['users'][i]['uid'])
		connection.query("INSERT INTO followers VALUES(" + str(tmp_a) + ", " + str(tmp_b) + ")")
		print("now user: " + str(i))
	connection.close()
	saveAllNames(group_id, offset + 998)

def saveSubscriptions(user_id):
	address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id) + "&extended=1&count=9999&access_token=" + admin_token
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	print("preparing...")
	try:
		connection.query('CREATE TABLE u' + str(user_id) + ' (group_id	text,group_name	text);')
		i = 0
		print(str(adata.subscriptions_amount))
		while i < int(adata.subscriptions_amount):
			print("now(save): " + str(i))
			try:
				connection.query("INSERT INTO u" + str(user_id) + " VALUES(" + "'" + str(final_data['response'][i]['gid']) + "'" + ", " + "'" + str(final_data['response'][i]['name']) + "'" + ")")
			except (KeyError, TypeError):
				pass
			i = i + 1
	except:
		print("This table was found!")

def DoLast(user_id):
	address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id) + "&extended=1&count=9999"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	connection = pg.connect(dbname='we', host='localhost', user='postgres', passwd='givemehack')
	try:
		connection.query('CREATE TABLE me' + str(user_id) + ' (group_id	text,group_name	text);')
		i = 0
		print(str(adata.subscriptions_amount))
		while i < int(adata.subscriptions_amount):
			print("now(save): " + str(i))
			try:
				connection.query("INSERT INTO me" + str(user_id) + " VALUES(" + "'" + str(final_data['response'][i]['gid']) + "'" + ", " + "'" + str(final_data['response'][i]['name']) + "'" + ")")
			except (KeyError, TypeError):
				pass
			i = i + 1
	except:
		print("This table was found!")