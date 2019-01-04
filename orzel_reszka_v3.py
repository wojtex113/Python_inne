import random 

def gra():
	orzel=reszka=0
	for i in range(100):
		x=random.randint(0,1)
		if x==0: orzel += 1
		else: reszka += 1
	return (orzel, reszka)

def wygrales():
	print("Gratulacje, wygrales !!")
	a=again()
	global wygrane
	wygrane += 1
	return a

def przegrales():
	print("Niestety przegrales...")
	a=again()
	global przegrane
	przegrane += 1
	return a

def wynik(re,*wynik):
	o=wynik[0]
	r=wynik[1]
	print("\nIlosc orlow: ",o)
	print("Ilosc rezek: ",r)
	if re=="o" and o>r: w=wygrales()
	elif re=="r" and r>o: w=wygrales()
	elif re=="re" and r==o: w=wygrales()
	else: w=przegrales()
	return w 

def again():
	while 1:
		pytanie=input("\nCzy chcesz zagrac jeszcze raz? [t/n] ")
		if pytanie=="t": 
			return True
		elif pytanie=="n":
			return False
		else: 
			print("Blad...") 

###################################################################################################

users_file="./orzel_reszka_users2.txt"
plik=open(users_file,"r+")

print("###############\nWitaj w grze orzel czy reszka.\nAby zakonczyc gre wcisnij Ctrl+C\n###############")
try:
	plik.seek(0)
	users=[]
	istnieje=False
	ilosc_userow=(sum(1 for line in plik))
	user_id=0
	plik.seek(0)
	print("Do tej pory w gre grali: [id_user rozegranych_rund wygrane przegrane]")
	for line in plik:
		user=line.split()	
		print(user)
		users.append(user)

	name=""
	rozgrywek=wygrane=przegrane=0
	while name=="":
		name=input("Podaj swoj nick: ")

	for i in range(ilosc_userow):
		if(users[i][1]==name): 
			istnieje=True
			user_id=i

	if istnieje==True: print("User ",name ," istnieje. Jego ID to: ", user_id)
	else: print("User ", name ," nie istnieje.")

	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

	ag=True
	if(istnieje==True):
		rozgrywek_old=rozgrywek=int(users[user_id][2])
		wygrane_old=wygrane=int(users[user_id][3])
		przegrane_old=przegrane=int(users[user_id][4])
		print(" Do tej pory grales %d razy. \n Wygrales %d razy. \n Przegrales %d razy. \n Powodzenia !!!\n" %(rozgrywek,wygrane,przegrane)) 

	while ag==True:
		result=input("Czego bedzie wiecej? [o]rlow, [r]ezek, a moze bedzie [re]mis? ")
		if(result=="o" or result=="r" or result=="re"):
			rozgrywek += 1
			res=gra()
			ag=wynik(result,*res)
		else:print("Wybrales niewlasciwa opcje")

except EOFError:
	plik.close()
except KeyboardInterrupt:
	plik.close()
except ValueError:
	plik.close()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("\nDziekujemy za zagranie w nasza gre!!!!")
print(" Zagrales %d razy. \n Wygrales %d razy. \n Przegrales %d razy"%(rozgrywek,wygrane,przegrane))

if istnieje!=True:
	new_user=(("%d %s %d %d %d")%(ilosc_userow,name,rozgrywek,wygrane,przegrane))
	users.append(new_user)
	if name!="":
		plik.write("%s\n" % new_user)
elif istnieje==True:
	users[user_id][2]=rozgrywek
	users[user_id][3]=wygrane
	users[user_id][4]=przegrane
	plik.seek(0)

	for i in range(len(users)):
        	s= " ".join(map(str, users[i]))     
	        plik.write(s+"\n")

plik.close()


