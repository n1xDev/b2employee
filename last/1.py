#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, Response, request, redirect
from urllib.request import urlopen # FROM
import json, pg

app = Flask(__name__, static_folder='static', static_url_path='')



mydict = {}

# 0f719753716e4f851b4158feddcf3b9dcae296372c0c321d74335d40ebf16a0aa9b1f391ee1e4a6d26c0c

mylist = {}
tmps = 0
weight = 0

def doSearchGroups(uid): #From one user
	address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(uid) + "&extended=0"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	user_subs = int(final_data['response']['groups']['count'])
	print(user_subs)
	i = 0
	while i < user_subs:
		address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(uid) + "&extended=1"
		data = urlopen(address)
		decoded_response = data.read().decode()
		final_data = json.loads(decoded_response)
		print(str(final_data['response'][i]['gid']))

def doSearchUsers(gid, offset):
	address = "https://api.vk.com/method/groups.getMembers?group_id=" + str(gid) + "&offset=" + str(offset) + "&count=500"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	i = 0
	while i < int(final_data['response']['count']):
		try:
			now_user = str(final_data['response']['users'][i])
			print("Searching " + str(now_user) + " user's groups...")
			#doSearchGroups(now_user)
			#getData(now_user)
		except:
			pass
		i += 1

	

def AnalyzeGroups(listGroup):
	c = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	arr = {}
	user = 0
	for i in range(0, 100000):
		try:
			res = c.query("SELECT * FROM u" + str(i)).getresult()
			user = "u" + str(i)
			for item in res:
				print(user)
				for it in range(len(listGroup)):
					if listGroup[it] == item[0]:
						arr[user] =  arr.get(user, 0) + 1
		except:
			continue


	return arr



def corel(data, currentData): 
	c = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	arr = {}
	for k,v in data.items():
		res = c.query("SELECT * FROM " + str(k)).getresult()

		ton = float(v) / (float(len(currentData)) + float(len(res)) - float(v))
		arr[k] = str(ton)

	return arr


def DoGet(arrUser):
	interest={}
	arr = []
	c = pg.connect(dbname='we', host='localhost', user='postgres', passwd='givemehack')
	for i in range(len(arrUser)):
		res = c.query("SELECT * FROM me" + arrUser[i] + ";").getresult()
		for item in res:
			interest[item[0]] = interest.get(item[0], 0) + 1

	listInterest = sorted([(v,k)  for k,v in interest.items() ], reverse=True)
	listInterest = [k for v,k in listInterest if v > 2]
	return listInterest

def GetNameById(vkid):
	resname = vkid[1:]
	address = "https://api.vk.com/method/users.get?user_id=" + resname
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	myname = final_data['response']['first_name']
	print (myname)
	return myname

def Main():
	print("\n")
	mydict = DoGet(["210064990", "107394388", "123875893", "140140875"])
	tmp = mydict 
	arr = []
	myres = AnalyzeGroups(mydict)
	ton = corel(myres, mydict)
	print ("\n")
	tmp_i = 0
	for k,v in ton.items():
		tmp_i += 1
		print(str(k) + "\t" + str(v))
		data = {}
		data['sort_num'] = tmp_i
		data['user'] = k#GetNameById(k)
		data['cor'] = int(float(float(v) * 100))
		arr.append(data)
	@app.route('/')
	def index():
		return render_template('index.html', data=arr)
	app.run(host='0.0.0.0', debug=True)




Main()