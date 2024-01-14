import random

lista = ['🎰', '💰', '💎']
score = 0
spin = 10
a = random.choice(lista)
b = random.choice(lista)
c = random.choice(lista)


def disegno():

	print("""								   

			 
		   /~~~~~~~~~~~~~~~~~~~~\  O
		  /-•_•-•_•-•_•-•_•-•_•-\  |
		  |---------------------|  /
		  |•""", a, """•|•""", b, """•|•""", c, """•|-/
		  /---------------------\\""")

	print("""		  |					 |""")
	print("""		  |_____________________|""")
	print(f"		  💰SCORE💰: {score}")
	print(f"		  🎰SPIN🎰: {spin}\n\n\n\n")


print(" \n\n\n\n\n  ⭐️⭐️⭐️⭐️⭐️W⃨e⃨l⃨c⃨o⃨m⃨e⃨ T⃨o⃨ C⃨a⃨s⃨i⃨n⃨o⃨⭐️⭐️⭐️⭐️⭐️\n")

while True:
	input("			 🎰 RETURN FOR SPIN 🎰\n")

	if a == '🎰' and b == '💎' and c == '💰':
		spin -= 1
		score += 300
	
	elif a == '🎰' and b == '💰' and c == '💎':
		spin -= 1
		score += 300
		
	elif a == '💎' and b == '🎰' and c == '💰':
		spin -= 1
		score += 300
		
	elif a == '💎' and b == '💰' and c == '🎰':
		spin -= 1
		score += 300
		
	elif a == '💰' and b == '🎰' and c == '💎':
		spin -= 1
		score += 300
		
	elif a == '💰' and b == '💎' and c == '🎰':
		spin -= 1
		score += 300
		
	elif a == '💎' and b == '💎' and c == '🎰':
		spin -= 1
		score += 300
		
	elif a == '💎' and b == '💎' and c == '💰':
		spin -= 1
		score += 500
		
	elif a == '💰' and b == '💎' and c == '💎':
		spin -= 1
		score += 500
		
	elif a == '🎰' and b == '💎' and c == '💎':
		spin -= 1
		score += 400
		
	elif a == '🎰' and b == '🎰' and c == '💎':
		spin -= 1
		score += 200
		
	elif a == '🎰' and b == '🎰' and c == '💰':
		spin -= 1
		score += 100
		
	elif a == '💎' and b == '🎰' and c == '🎰':
		spin -= 1
		score += 200
		
	elif a == '💰' and b == '🎰' and c == '🎰':
		spin -= 1
		score += 100
		
	elif a == '💰' and b == '💰' and c == '🎰':
		spin -= 1
		score += 200
	
	elif a == '💰' and b == '💰' and c == '💎':
		spin -= 1
		score += 400
		
	elif a == '💎' and b == '💰' and c == '💰':
		spin -= 1
		score += 400
		
	elif a == '🎰' and b == '💰' and c == '💰':
		spin -= 1
		score += 200
		
	elif a == '💰' and b == '💰' and c == '💰':
		spin += 1
		score += 600
	elif a == '💎' and b == '💎' and c == '💎':
		spin += 1
		score += 1200
	elif a == '🎰' and b == '🎰' and c == '🎰':
		spin += 6
	
	elif a == '💎' and b == '💰' and c == '💎':
		spin -= 1
		score += 500
		
	elif a == '💎' and b == '🎰' and c == '💎':
		spin -= 1
		score += 400
	
	elif a == '💰' and b == '💎' and c == '💰':
		spin -= 1
		score += 400
		
	elif a == '💰' and b == '🎰' and c == '💰':
		spin -= 1
		score += 200
		
	elif a == '🎰' and b == '💎' and c == '🎰':
		spin -= 1
		score += 200
		
	elif a == '🎰' and b == '💰' and c == '🎰':
		spin -= 1
		score += 100

	if spin == 0:
		print("			 ❌ GAME OVER ❌")
		print(f"		    💰SCORE💰: {score}")
		break
	disegno()

	a = random.choice(lista)
	b = random.choice(lista)
	c = random.choice(lista)

	

	
