##data_classes.py 

##homework 2 


import json
class person(object):
 def __init__( self, name, age, email):
    self.name = name 
    self.age = 22
    self.email = email

#added self I was getting a lot of errors and googled why so added self to define
# added dict (base code was right idea)
def to_dict(self):
   return {'name':self.name, 'age': self.age,'email': self.email}




class student (person):
  def __init__(self,name, age, email, student_id):
        self.student_id = student_id= 123456
        super().__init_(name,age ,email)

  def to_dict_ ( self, name, age, email, student_id):
      
  
 #student = student ('Brianna',22,'bmargueta@cpp.edu',123456 )
  #ilename ='data_claases.py'
 #with open ('data_classes.py' , 'w') as f:
 #   jspon.dump(student.to_dict() , f, indent= 4 ) 

 #with open('data_classes.py'),as f:
    #data_classes =json.load(f)
    #print (json.dumps(data_classes, indent-2))

   data = super().to_dict()
   data ['student_id']= self.student_id
   return data
  
#undo that latter

 #import jsonstudent=student(name,age,email,studentid)

   #ilename = 'data_classes.py'
  #with open(filename,'w')as f:
 
  #json.dump ('w')as f:


## this part (below) is what online was saying to add 
def save_to_json(self, filename):
   with open (filename,'a') as f:

      json.dump(self.to_dict(),f,indent=4 )
 
@staticmethod
def display_json_content(filename):
        try:
            with open(filename, 'a') as f:
                data = json.load(f)
                print(json.dumps(data, indent=4))
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

##print ( person, student)


##obj = student ()
##json_string = json.dumps (obj._dict_)
##print (json_string)
# note I followed and online method for this part.