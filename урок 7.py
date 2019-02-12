import random




def getRandomList(count=5, population=False):
   p = count if not population or count > population else population
   return random.sample(range(1, p+1), count)


def bagOfCasks():
   for i in getRandomList(90):
      yield i


class Card:
   def __init__(self, title = 'Карточка'):
      self.title = title
      self.__crossed = set()
      self.__data = getRandomList(3 * 5, 90)
      self.__matrix = []
      for i in range(3):
         m = self.__data[i*5:(i+1)*5]
         m.sort()
         while len(m) < 9:
            j = random.randint(0, 9-1)
            m[j:j] = ['']
         self.__matrix.append(m)

   @property
   def matrix(self):
      return [['-' if x in self.__crossed else x for x in self.__matrix[i]] for i in range(3)]

   def __isub__(self, value):
      if value in self.__data:
         self.__crossed.add(value)
      return self

   def __len__(self):
      return len(self.__data) - len(self.__crossed)

   def __iter__(self):
      return iter(list(self.__data))


   def __str__(self):
      s =  [("{:-^" + str(9 * 3) + "}").format(" "+self.title+" ")]
      s += [("{:>3}" * 9).format(*self.matrix[i]) for i in range(3)]
      s += ["-" * 9 * 3]
      return "\n".join(s)



me = Card("Ваша карточка")
computer = Card("Карточка компьютера")

turn = 1
winner = False
for cask in bagOfCasks():
   print(f"\nХод №{turn}(осталось {90-turn}): Новый бочонок - {cask}")
   print(me)
   print(computer)

   computer -= cask  

   if True: 

      a = input("\n[y] - зачеркнуть / [enter] - продолжить: ")
      exist = cask in me  
      if (not exist and a == 'y') or (a != 'y' and exist):
         print('!!! тыошибся(лась)')
         winner = computer
         break

   me -= cask  

   if not len(me) and not len(computer):
      break
   if not len(me):
      winner = me 
      break
   if not len(computer):
      winner = computer 
      break

   turn += 1



print(f"\nИгра завершена", "в НИЧЬЮ" if winner is False else f"победила {winner.title}")
