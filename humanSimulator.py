import time,os,random as ran,math
import matplotlib.pyplot as plt
clear = lambda: os.system('cls')
os.system('title Human Simulator')
names = ['James','John','Robert','Michael','William','David','Richard','Joseph','Thomas','Charles','Christopher','Daniel','Matthew','Anthony','Lennord','Donald','Mark','Paul','Steven','Andrew','Kenneth','Joshua','George','Kevin','Brain','Kieth','Edward','Ronald','Timothy','Jason','Jeffery','Ryan','Jacob','Hermia','Hestai','Ricki','Prabhakara','Ástríður','Chiyoko','Abdulla','Dolly','Shyamal','Uros','Misa','Gerrit','Vivianus','Rikke','Miran','Lalo','Cody','Ànghela','Thierry','Tryggve','Camellia','Shyam','Jaylin','Mohammad','Iara','Shell','Alban','Cezary','Fionntan','Gobind','Aviva']
lastNames = ['Smith','Adams','Hodge','Gardner','Pendragon','Williams','Daily','Bush','Kenedy','Lee','Khan','Genghis','Terranova','Karim','Rasmussen','Worner','Cory','Coeman','Burnham','Biermann','Donohoe','Landau','Shapiro','Stoyanov','Kumar','Jager','Shwetz','Pavic','Henriques','Mag Uidhir','Strudwick','Pedrotti','Bogdanovic','Scrivens','Bonnet','Kucuk','Kedves','Neil','Hendry','Xun','Martín','Kolbe']
countries_list = ['Afghanistan','Akrotiri','Albania','Algeria','American Samoa','Andorra','Angola','Anguilla','Antarctica','Antigua','Barbuda','Argentina','Armenia','Aruba','Ashmore','Cartier','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Bassas','India','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia','Herzegovina','Botswana','Bouvet','Brazil','Virgin Islands','Brunei','Bulgaria','Burkina','Faso','Burma','Burundi','Cambodia','Cameroon','Canada','Cape','Verde','Cayman','Chad','Chile','China','Christmas Island','Clipperton Island','Cocos Islands','Colombia','Comoros','Congo,','Democratic Republic of the Congo','Cook Islands','Coral Sea Islands','Costa Rica','Cote','Ivoire','Croatia','Cuba','Cyprus','Czech Republic','Denmark','Dhekelia','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial','Guinea','Eritrea','Estonia','Ethiopia','Europa Island','Falkland Islands','Faroe Islands','Fiji','Finland','France','French','Guiana','French Polynesia','Gabon','Gambia,','Georgia','Germany','Ghana','Gibraltar','Glorioso Islands','Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guernsey','Guinea','Guinea-Bissau','Guyana','Haiti','Heard Island and McDonald Islands','Holy (Vatican City)','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Isle of Man','Israel','Italy','Jamaica','Jan','Mayen','Japan','Jersey','Jordan','Juan de Nova Island','Kazakhstan','Kenya','Kiribati','Korea','North Korea,','South Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia,','Federated States of Moldova','Monaco','Mongolia','Montserrat','Morocco','Mozambique','Namibia','Nauru','Navassa Island','Nepal','Netherlands','Netherlands','Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island','Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Panama','Papua','New','Guinea','Paracel Islands','Paraguay','Peru','Philippines','Pitcairn Islands','Poland','Portugal','Puerto Rico','Qatar','Reunion','Romania','Russia','Rwanda','Samoa','San','Marino','Sao','Tome','Principe','Saudi Arabia','Senegal','Serbia','Montenegro','Seychelles','Sierra','Leone','Singapore','Slovakia','Slovenia','Solomon','Islands','Somalia','South Africa','South Georgia','South Sandwich Islands','Spain','Spratly Islands','Sri','Lanka','Sudan','Suriname','Svalbard','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Timor-Leste','Togo','Tokelau','Tonga','Trinidad and Tobago','Tromelin Island','Tunisia','Turkey','Turkmenistan','Turks and Caicos Islands','Tuvalu','Uganda','Ukraine','United','Arab','Emirates','United','Kingdom','United','States','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','Virgin Islands','Wake Island','Wallis and Futuna','West Bank','Western Sahara','Yemen','Zambia','Zimbabwe']

## VARS

deathHistory = []
yearList = []
events = []
countries = []
planets = ['Earth','Mars']
year = 0
staticDeathRate = 20
deathPlus = 0
warChance = 0
globalDeathFactor = 0
totalDead = 0
totalBirths = 0
sicknessDeaths = 0

while True:
	starting_countries = int(input('How many countries would you like to start out with? '))
	if starting_countries > 195:
		print('cannot be over 195')
	elif starting_countries < 2:
		print('cannot be under 2')
	else:
		break
starting_pops = int(input('And what would you like their starting populations to be? '))


def nameGen():
	first_name = names[ran.randint(0,len(names)-1)]
	last_name = lastNames[ran.randint(0,len(lastNames)-1)]
	return first_name+" "+last_name

## HUMAN FORMAT [number, name, sex, age, sick, thing, happiness]
class Country():
	def __init__(self, n):
		self.population = []
		self.name = n
		self.population_count = 0
		self.tech_level = 0
		self.country_death_factor = 0
		self.tech_advancement_level = 0
		self.war_win_chance = 0
		## 0 = centrist, 1 = auth-r, 2 = lib-r, 3 = lib-l, 4 = auth-l, 5 = x-auth-r, 6 = x-lib-r, 7 = x-lib-l, 8 = x-auth-l
		self.government_type = None
	def addHuman(self,h):
		self.population.append(h)
		self.population_count+=1
	def genCountry(self):

		hmn = Human(self.population_count,nameGen(),'m',18,False,'s',75)
		self.addHuman(hmn)
		hmn = Human(self.population_count,nameGen(),'f',18,False,'s',75)
		self.addHuman(hmn)
		for notneeded in range(2,starting_pops):
			coin = ran.randint(0,1)
			if coin == 0: self.addHuman(Human(self.population_count,nameGen(),'f',18,False,'s',75))
			else: self.addHuman(Human(self.population_count,nameGen(),'m',18,False,'s',75))
	def delHuman(self,num):
		del self.population[num]
		self.population_count-=1
	def toString(self):
		ans = ""
		ans+=self.name +", "+str(self.population_count)
		for hmn in self.population:
			ans+=hmn.toString()+'\n'
		return ans
		
			
		
class Human():
	def __init__(self, num, nm, s, a, sck, thng, hpyns):
		self.number = int(num)
		self.name = nm
		self.sex = s
		self.age = a
		self.sick = sck
		self.thing = thng
		self.happyness = hpyns
	def numdown(self):
		self.number-=1
	def aging(self):
		self.age+=1
	def mutateHappy(self, mood):
		self.happyness+=mood
	def getNum(self):
		return int(self.number)
	def toString(self):
		return self.name +", "+ self.sex +", "+ str(self.age) +", "+ str(self.happyness)

universe = {"Earth":[]}



## SETUP

universe['Earth'] = countries
countries_used = []
for rc in range(0,starting_countries):
	while True:
		x = ran.randint(0,len(countries_list))
		if countries_list[x] in countries_used:
			pass
		else:
			new_country = Country(countries_list[x])
			new_country.genCountry()
			countries_used.append(countries_list[x])
			countries.append(new_country)
			break
	
	

## METHODS		

def universeInfo():
	ans = ''
	for item in countries:
		ans+=item.toString()+'\n'
	return ans
		
def age():
	for country in countries:
		for hmn in country.population:
			hmn.aging()
			hmn.mutateHappy(ran.randint(-15,15))

def humanCount():
	ans = 0
	for country in countries:
		ans+=country.population_count
	return ans
	
## BIG LOOP

while True:
	
	deathCount = 0
	year+=1
	age()
	
	## DEATH
	
	for country in countries:
		deathRate = int(staticDeathRate + (int(country.tech_level)*0.25) - globalDeathFactor - country.country_death_factor)
		for human in country.population:
			deathR = ran.randint(1,deathRate)
			if deathR == 1:
				death = True
			else: death = False
			if human.age >= 50 or human.age <= 30:
				if death:
					country.delHuman(human.getNum())
					deathCount+=1
					for human2 in country.population:
						if human2.getNum() > human.getNum():
							human2.numdown()
			if human.sick and not death:
				sickDeath = ran.randint(1,3 + int((int(country.tech_level)*0.1)))
				if sickDeath == 1:
					country.delHuman(human.getNum())
					deathCount+=1
					sicknessDeaths+=1
					for human2 in country.population:
						if human2.getNum() > human.getNum():
							human2.numdown()
							
	## TECH_LEVEL INCREASE / ADVANCEMENTS
	for country in countries:
		tech_check = ran.randint(0,50 - int(math.floor((country.population_count * 0.001))))
		if tech_check == 0:
			country.tech_level+=1
		if country.tech_level == 50:
			country.tech_level+=1
			country.war_win_chance+=10
		elif country.tech_level == 100:
			country.tech_level+=1
			country.war_win_chance+=20
		elif country.tech_level == 250:
			## GOVERMENT GENERATION
			country.government_type = ran.randint(0,8)
			country.tech_level+=1
		elif country.tech_level == 400:
			country.tech_level+=1
			country.war_win_chance += 50
		elif country.tech_level == 600:
			country.country_death_factor-=10
			country.tech_level+=1
		elif country.tech_level == 700:
			country.tech_level+=1
			country.country_death_factor-=10
			country.war_win_chance+=40
		elif country.tech_level == 1000:
			## SPACE STUFF (if i ever get to it)
			print('',end='')
	
	## GLOBAL EVENTS
	for country in countries:
		if country.tech_level >= 2500:
			dchance = ran.randint(1,50-int(math.floor((country.tech_level/1000))))
			if dchance == 1:
				dchance = ran.randint(1,4)
				if dchance == 1:
					## AI take over
					print('',end='')
				elif dchance == 2:
					## Minor Atomic War
					print('',end='')
				elif dchance == 3:
					## Global Atomic War
					print('',end='')
				elif dchance == 4:
					## Resource Shortages
					print('',end='')

	
	
	
	## BIRTH + SOME OTHER CHECKS
						
	for country in countries:
		happy = 0
		numM = 0
		numF = 0
		haveM = False
		haveF = False
		for human in country.population:
			happy+=human.happyness
			getSick=ran.randint(1,100)
			if getSick == 1:
				human.sick = True
			if human.sex == 'm' and human.age >= 18 and human.age <= 45 and human.thing == 's' and human.happyness >= 50:
				hmnM=human
				haveM=True
			elif human.sex == 'f' and human.age >= 18 and human.age <= 45 and human.thing == 's' and human.happyness >= 50:
				hmnF=human
				haveF=True
			if haveF and haveM:
				birth = True
				if birth:
					if  hmnM.happyness < 100:
						hmnM.happyness+=10
					if hmnF.happyness < 100:
						hmnF.happyness+=10
					nameR = ran.randint(1,11)
					if nameR <= 5:
						fatherName = hmnM.name
						fatherName2 = fatherName.split()
						fatherLastName = fatherName2[1]
						newName = names[ran.randint(0,len(names)-1)] + " " + fatherLastName
					elif nameR >= 5 and nameR != 11:
						motherName = hmnF.name
						motherName2 = motherName.split()
						motherLastName = motherName2[1]
						newName = names[ran.randint(0,len(names)-1)] + " " + motherLastName
					elif nameR == 11:
						newName = names[ran.randint(0,len(names)-1)] + " " + lastNames[ran.randint(0,len(lastNames)-1)]
					ageR = ran.randint(1,2)
					if ageR == 1:
						sex = 'm'
					elif ageR == 2:
						sex = 'f'
					thingR = ran.randint(1,100)
					if thingR <= 2: thing = 'g'
					else: thing = 's'
					if hmnF.sick: sick = True
					else: sick = False
					country.addHuman(Human(country.population_count,newName,sex,0,sick,thing,80))
					haveM=False
					haveF=False
					totalBirths+=1
					
		## REVOLUTION
					
		if not country.population_count <= 0:
			if happy/country.population_count < 30:
				revR = ran.randint(1,1000)
				if revR == 1:
					eventR = ran.randint(1,3)
					if eventR == 1:
						revSucc = ran.randint(1,2)
						if revSucc == 1:
							events.append("In the year " + str(year) + " the people of " + country.name + " revolted against the government, causing a massive civil war... and the people lost.")
						if revSucc == 2:
							events.append("In the year " + str(year) + " the people of " + country.name + " overthrew there oppressive government.")
					elif eventR == 2:
						events.append("In the year " + str(year) + " the people of " + country.name + " had a riot over high taxes, leading to many civilian and army deaths.")
					elif eventR == 3:
						events.append("In the year " + str(year) + " a terrorist group struck " + country.name + " realising toxic neuro-gas into the capital city, killing many innocent civilians.")
					for human in country.population:
						deathR = ran.randint(1,2)
						if deathR == 1:
							death = True
						else: death = False
						if death:
							country.delHuman(human.number)
							deathCount+=1
							for human2 in country.population:
								if human2.number > human.number:
									human2.number-=1
									
	## WAR					
	
	warRan = ran.randint(1,100)
	if warRan <= warChance:
		warChance=0
		while True:
			country11 = ran.randint(0,3)
			country1 = countries[country11]
			if not country1.population_count <= 0:
				break
		while True:
			country22 = ran.randint(0,3)
			country2 = countries[country22]
			if not country2.population_count <= 0 and country2 != country1:
				break
		c1roll = ran.randint(1,50)+country1.war_win_chance
		c2roll = ran.randint(1,50)+country1.war_win_chance
		if c1roll > c2roll:
			events.append("In the year " + str(year) + " a war between " + country1.name +" and " + country2.name +" occured, the winner of the conflict ended up being " + country1.name +" but there were still casualties on both sides.")
			for human in country1.population:
				deathR = ran.randint(1,4 + country.country_death_factor)
				if deathR == 1:
					death = True
				else: death = False
				if death:
					country1.delHuman(human.number)
					deathCount+=1
					for human2 in country1.population:
						if human2.number > human.number:
							human2.number-=1
			for human in country2.population:
				deathR = ran.randint(1,2 + country.country_death_factor)
				if deathR == 1:
					death = True
				else: death = False
				if death:
					country2.delHuman(human.number)
					deathCount+=1
					for human2 in country2.population:
						if human2.number > human.number:
							human2.number-=1
		elif c2roll > c1roll:
			events.append("In the year " + str(year) + " a war between " + country1.name +" and " + country2.name +" occured, the winner of the conflict ended up being " + country2.name +" but there were still casualties on both sides.")
			for human in country1.population:
				deathR = ran.randint(1,2 + country.country_death_factor)
				if deathR == 1:
					death = True
				else: death = False
				if death:
					country1.delHuman(human.number)
					deathCount+=1
					for human2 in country1.population:
						if human2.number > human.number:
							human2.number-=1
			for human in country2.population:
				deathR = ran.randint(1,4 + country.country_death_factor)
				if deathR == 1:
					death = True
				else: death = False
				if death:
					country2.delHuman(human.number)
					deathCount+=1
					for human2 in country2.population:
						if human2.number > human.number:
							human2.number-=1
		elif c1roll == c2roll:
			events.append('In the year '+str(year)+' a war between '+ country1.name + " and " + country2.name + " occured, the conflict had no final result. Only ending with caualties on both sides.")
			for human in country1.population:
				deathR = ran.randint(1,2 + country.country_death_factor)
				if deathR == 1:
					death = True
				else: death = False
				if death:
					country1.delHuman(human.number)
					deathCount+=1
					for human2 in country1.population:
						if human2.number > human.number:
							human2.number-=1
		for human in country2.population:
				deathR = ran.randint(1,2 + country.country_death_factor)
				if deathR == 1:
					death = True
				else: death = False
				if death:
					country2.delHuman(human.number)
					deathCount+=1
					for human2 in country2.population:
						if human2.number > human.number:
							human2.number-=1
	else:
		warChance+=.005	
	if humanCount() <= 0:
		break
		
		
	## GRAPHING
	yearList.append(year)
	deathHistory.append(deathCount)
	if year%50==0 and year!=0:
		plt.plot(yearList,deathHistory)
		plt.ylabel('Deaths')
		plt.xlabel('Year')
		plt.suptitle('Deaths over Time')
		plt.show()
	
	
	
	## DISPLAY INFO
	
	clear()
	totalDead+=deathCount
	print("<-* GENERAL INFO *->")
	print('Year '+str(year))
	print('Earth Population: '+str(humanCount()))
	print('Total Births: '+str(totalBirths))
	print()
	print("<-< DEATH INFO >->")
	print('Deaths this Year: '+str(deathCount))
	print('Total Dead: '+str(totalDead))
	print('Total Deaths from Sickness: '+str(sicknessDeaths))
	print()
	for country in countries:
		if country.population_count != 0:
			print(country.name + ': ' + str(country.population_count))
	print()
	for item in events:
		print(item)
	
	with open('universe.txt','w+') as filew:
		filew.write(universeInfo())

print("Your universe has died.")
print("It lasted " + str(year) + " years")
