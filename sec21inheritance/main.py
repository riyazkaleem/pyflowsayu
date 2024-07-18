#declaring parent class
class Animal:
    
    #declaring the parent class constructor
    def __init__(self):
        self.num_eyes = 2
    
    #declaring the breathe method
    def breathe(self):
        print('inhale, exhale')

#declaring child class
class Fish(Animal):
    
    #declaring the child class constructor
    def __init__(self):
        #calling the parent class constructor into the child class
        super().__init__()

    #adding some functionalities for the parent class method in child class
    def breathe(self):
        #the below super command will bring in all the breathe functionalities from the parent class
        #on which we will write additional functionalities
        super().breathe()
        print('inside child class breathe, under water breathing possible now')

    #declaring the swim method
    def swim(self):
        print('moving inside the water')

#creating the child class object
nemo = Fish()

#calling the child class method through child class method
nemo.swim()

#calling the child class method through parent class method
nemo.breathe()

#accessing the parent class attribute through the child class object
print(f'number of eyes nemo has: {nemo.num_eyes}')