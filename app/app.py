
import pandas as pd

from collections import deque

# Define function
def getData():
    print("Dayum, functions are awesome")

# Call the function
getData()   

# functions with parameters
def btctousd(btc):
     
    print("btc - " , btc ,  " is equal to " , btc*527 ,  " usd")

# Call 
btctousd(110.923)

# function with parameters
def getdata_listasparam(animal):
    print("animal 1:", animal[0], " animal 2:", animal[1])

#calling the function 
mammels = ["elephant", "tiger"]
#getdata_listasparam(mammels)

# passing data fram as parameter


mammels_df = pd.DataFrame(data =["elephant", "tiger"], columns=["animal"], index=["id", "animal"])
print(mammels_df)
print(mammels_df.size) 
print(mammels_df.index)


def generatedocstring():
    """ Do nothing but document the function 
        Really dont do anything
        
         added a variable 
         
         add 10 to it
        
    """
    a = 10
    
   
    
    a += 10
    
  
    
    print("a", a)
    
    print(generatedocstring.__doc__)

#generatedocstring()


# queues
queue = deque([mammels])
queue.append(mammels.append("monkey"))
queue.append(mammels.append("giraffe"))
print(queue)

print(queue.popleft())
print(queue.pop())


#lambda functions

def eglambda(n):
    return(lambda x: x+n)

f = eglambda(100)
print(f(1100))


 