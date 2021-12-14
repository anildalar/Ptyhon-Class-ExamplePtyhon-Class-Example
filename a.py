# Funtion defination

def hello(n):
    print("Hello {},How are you ? ".format(n))

hello("Anil")

# Arbirary argument
def hello1(*x):
    print(f"Hello {x[0]},How are you")

hello1("Nandan")

# Keyword Argument
def hello2(std,friend):
    print("Hello %s,How are you?"%(std))
    print("Hello %s,How are you?"%(friend))

hello2(friend="Manish",std="Abhishesk")

# Arbirary Keyword Argument
# **kwargs

def hello3(**x):
    print(f"Hello {x['std1']}, How are you ? ")

hello3(std1="Avadhi")