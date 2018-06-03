import os, sys, json, pg
from urllib.request import urlopen

def Save2File(user_id, next_num):
	f = open("local" + str(next_num) + ".db", "w")
	address = "https://api.vk.com/method/users.getSubscriptions?user_id=" + str(user_id)
	data = urlopen(address)
	decoded_response = data.read().decode()
	final_data = json.loads(decoded_response)
	i = 0
	while i < int(final_data['response']['groups']['count']):
		f.write(str(final_data['response']['groups']['items'][i]) + "\n")
		i += 1

def Scanner(user_1id, user_2id, second):
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	res1 = connection.query("select * from u" + str(user_1id)).getresult()
	res2 = connection.query("select * from u" + str(user_2id)).getresult()
	coincidence = 0
	coincidence_str = []
	excepts = 0
	i = 0
	for i in range(0, len(res1)):
		try:
			for j in range(0, len(res2)):
				if res1[i][0] == res2[j][0]:
					coincidence += 1
					coincidence_str.append(str(res1[i][1]))
		except:
			excepts += 1
	print("coincidence: " + str(coincidence))
	print("coincidence name: " + str(coincidence_str))
	print("excepts: " + str(excepts))
	#print("\nRes1: " + str(res1))
	#print("\nRes2: " + str(res2))
	if second == "0":
		Scanner(user_2id, user_1id, "1")

def Main():
	#Save2File("1", "1")
	#Save2File("20020126", "2")
	#Save2File("53083705", "3")
	#Save2File("273251945", "4")
	#Save2File("93388", "5")

	"""i = 0
	while i < len(two_links[0]):
		i += 1"""

	Scanner("1", "1092", "0")
	PrintAll()
	print("Done.")

Main()