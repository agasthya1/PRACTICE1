
def Time(sP):
	if "AM" !=  sP[6:8]:
		time = sP[0:2]+sP[3:5]
		time = int(time)
		if time < 1200:
			time += 1200
	else:
		time = sP[0:2]+sP[3:5]
		time = int(time)
		if time >= 1200:
			time-= 1200
	return time


T = int(input())

for i in range(T):
	sP = input()
	P = Time(sP)
	N = int(input())
	OL = ""
	for j in range(N):
		S = input()
		L = Time(S[0:8])
		R = Time(S[9:17])
		if P >= L and P <= R :
			OL+="1"
		else:
			OL+="0"
	print(OL)



		

	