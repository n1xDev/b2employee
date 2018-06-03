from urllib.request import urlopen # FROM

import json # Python's Lib's
import psycopg2
import pg
from mydata import * # My local Lib's

#connection = psycopg2.connect(postgre_auth)
#cursor = connection.cursor()
#cursor.execute("INSERT INTO followers VALUES(555, 666)")

def getWallAmount(owner_id):
	address = "https://api.vk.com/method/wall.get?owner_id=" + owner_id + "&count=1&filter=owner&access_token=" + admin_token
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	wall_amount = final_data['response'][0]
	print(wall_amount)

def getFriendsAmount(group_id):
	address = "https://api.vk.com/method/groups.getMembers?group_id=" + group_id + "&fields=sex&access_token=" + admin_token
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	friends_amount = final_data['response']['count']
	print(friends_amount)

def saveAllNames(group_id, offset):
	offset = int(offset)
	address = "https://api.vk.com/method/groups.getMembers?group_id=" + group_id + "&fields=sex&access_token=" + admin_token + "&count=1000"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	i = offset
	"""while i < (offset + 998):
		tmp_a = final_data['response']['users'][i]['uid']
		tmp_b = getFollowers(final_data['response']['users'][i]['uid'])
		connection.query("INSERT INTO followers VALUES(" + str(tmp_a) + ", " + str(tmp_b) + ")")
		print("now user: " + str(i))
		i += 1"""
	for i in range(offset, offset + 998):
		tmp_a = final_data['response']['users'][i]['uid']
		tmp_b = getFollowers(final_data['response']['users'][i]['uid'])
		connection.query("INSERT INTO followers VALUES(" + str(tmp_a) + ", " + str(tmp_b) + ")")
		#print("now user: " + str(i))
	connection.close()
	saveAllNames(group_id, offset + 998)

def getFollowers(user_id):
	# truncate table followers
	#address = "https://api.vk.com/method/users.getFollowers?user_id=" + str(user_id) + "&count=0&access_token=" + admin_token
	address = "https://api.vk.com/method/users.getFollowers?user_id=" + str(user_id) + "&count=0"
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	return final_data['response']['count']

def testPSQL():
	print("\n\nStarting PSQL...\n")
	connection = psycopg2.connect(postgre_auth)
	cursor = connection.cursor()
	cursor.execute("SELECT follower FROM followers")
	records = cursor.fetchall()
	print(records)

def main():
	getWallAmount("145476098")
	getFriendsAmount("3801006")
	saveAllNames("3801006", "0")
	testPSQL()

main()