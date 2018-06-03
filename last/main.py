import json, pg

from urllib.request import urlopen
from mydata import *

obj1 = {}
obj2 = {}

def doGet(u1id, u2id, u3id):
	c = pg.connect(dbname='we', host='localhost', user='postgres', passwd='givemehack')
	res1 = c.query("SELECT * FROM me" + u1id + ";").getresult()
	res2 = c.query("SELECT * FROM me" + u2id + ";").getresult()
	res3 = c.query("SELECT * FROM me" + u3id + ";").getresult()
	for item in dict:
		if item.title not in list:
			
	for i in range(0, len(res1)):
		for j in range(0, len(res2)):
			for n in range(0, len(res3)):
				if (res1[i][0] == res2[j][0]) and (res1[i][0] != res3[n][0]):
					print("Вариант совпадения -- 1-й: " + res1[i][0])
				elif (res1[i][0] == res3[n][0]) and (res2[j][0] != res3[n][0]):
					print("Вариант совпадения -- 2-й: " + res1[i][0])
				elif (res1[i][0] == res2[j][0]) and (res2[j][0] == res3[n][0]):
					print("Тройное совпадение -- " + res1[i][0])
				else:
					pass
					#print(str(i) + " / " + str(j) + " / " + str(n))

def doSort():
	doGet("210064990", "145476098", "107394388")

def doNew(u1id):
	c = pg.connect(dbname='we', host='localhost', user='postgres', passwd='givemehack')
	res1 = c.query("SELECT * FROM me" + u1id + ";").getresult()


def Main():
	#doSort()
	print("\n")

Main()