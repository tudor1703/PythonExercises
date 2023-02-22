import random
choice = input(str('tasteaza "da" daca vrei sa incupi jocul sau "nu" daca nu vrei: '))
if choice == "nu":
   print('hai pa')
elif choice == "da":
   num = input("ghiceste-mi numarul dintre 1 si 100: ")
   numar = random.randint(1, 100)
   for x in numar:
      if x < num:
         input("numarul meu este mai mic")
      elif x > num:
         input("mai meu este mai mare")
      else:
         print("da bravo")
else:
   print(" nu e voe ")
   print(" nu e voe ")
   print(" nu e voe ")
   print(" nu e voe ")