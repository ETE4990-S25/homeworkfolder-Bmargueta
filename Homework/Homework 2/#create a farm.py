#create a farm
# cow, pig, horse, donkey ,hen ,dog
class animals:
    def _init_ (self,cow ,pig ,horse ,donkey ,hen , dog):
     self.cow = cow  # done 
     self.pig = pig  # done
     self.horse = horse #done
     self.donkey = donkey #done
     self.hen = hen #done
     self.dog = dog #done
     self.goat= goat 


class pets (animals):
    def _init_ (self, eat, friend):
     self.eat = False
     self.friend = friend
    

class farm (animals):
    def _init_ (self, eat , leather , worker, dirt , soap):
      self.eat = eat
      self.leather = leather
      self.worker = worker
      self.dirt= dirt
      self.soap= soap

    class worker:
         def _init_ (self, worker):
            self.worker= worker

class dog (pets):
     def _init_ (self, cute ,type):
        self. cute = True
        self. type = "type of dog is ?"

dog1= dog(cute= True, dog_type= "pug")
list_of_animals=[dog1()]


class cow (farm):
   def _init_ (self, eat , leather , worker, dirt , soap):
      super ().__init__(eat,leather , worker, dirt , soap) #googles this
      self.eat = True
      self.leather = True 
      self.worker = False
      self.dirt= True 
      self.soap=True
cow1= cow(eat=True, leather= True , worker= False , dirt=True, soap=False)

list_of_animals=[cow1()]

class horse (farm):
   def _init_ (self, eat , leather , worker, dirt , soap):
      super ().__init__(eat,leather , worker, dirt , soap)#googles this
      self.eat = False
      self.leather = False 
      self.worker = True
      self.dirt= False
      self.soap=False
horse1= horse(eat=False, leather= False,worker= True , dirt=False, soap=False)

list_of_animals=[horse1()]

class pig (farm):
   def _init_ (self, eat , leather , worker, dirt , soap):
      super ().__init__(eat,leather , worker, dirt , soap)#googles this
      self.eat = True
      self.leather = False 
      self.worker = False
      self.dirt= True
      self.soap=False
pig1= pig(eat=True, leather= False,worker= False , dirt=False, soap=False)

list_of_animals=[pig1()]



class donkey (farm):
   def _init_ (self, eat , leather , worker, dirt , soap):
      super ().__init__(eat,leather , worker, dirt , soap)#googles this
      self.eat = False
      self.leather = False 
      self.worker = True
      self.dirt= False
      self.soap=False
donkey1= donkey(eat=False, leather= False,worker= True, dirt=False, soap=False)

list_of_animals=[donkey1()]

class hen(farm):
   def _init_ (self, eat , leather , worker, dirt , soap):
      super ().__init__(eat,leather , worker, dirt , soap)#googles this
      self.eat = True
      self.leather = False 
      self.worker = False
      self.dirt= False
hen1= hen(eat=False, leather= False,worker= True, dirt=False, soap=False)

list_of_animals=[hen1()]

class goat(farm):
   def _init_ (self, eat , leather , worker, dirt , soap):
      super ().__init__(eat,leather , worker, dirt , soap)#googles this
      self.eat = False
      self.leather = False 
      self.worker = True
      self.dirt= False
      self.soap=True
goat1= goat(eat=False, leather= False,worker= True, dirt=False, soap=True)

list_of_animals=[goat1()]