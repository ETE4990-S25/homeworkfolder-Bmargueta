#create a farm
# cow, pig, horse, donkey ,hen ,dog
class animals:
    def _init_ (self,cow ,pig ,horse ,donkey ,hen , dog):
     self.cow = cow 
     self.pig = pig 
     self.horse = horse
     self.donkey = donkey 
     self.hen = hen
     self.dog = dog


class pets (animals):
    def _init_ (self, eat, friend):
     self.eat = False
     self.friend = True
    

class farm (animals):
    def _init_ (self, eat , leather , worker, dirt , soap):
      self.eat = True
      self.leather = True 
      self.worker = False
      self.dirt= True 
      self.soap=True

    class work (farm):
         def _init_ (self, worker):
            self.worker= True

class dog (pets):
     def _init_ (self, cute ,type):
        self. cute = True
        self. type = "type of dog is ?"
    listofanimals=[dog()]