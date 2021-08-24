class MyFirstClass :
    
    def Family(self, name, role):
        print(name, "is a(an)", role, "in my family")

Do = MyFirstClass()

Do.Family("Kim", "Husband")
Do.Family("Shin", "Wife")
Do.Family("Kim", "Future Baby")

# I found that a simple class in Python 
# doesn't need stuffs like __main__, __init__ and so on.
# What the __hell__?