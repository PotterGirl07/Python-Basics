#Scope Of A Variable
#vari created in a func can only be used in it
#vari declared out of a func can be used w/ global command

actor="Emma Watson"

def localshowactor():
    actor="Shah Rukh Khan"
    print(actor)
def globalshowactor():
    global actor
    print(actor)

localshowactor()
globalshowactor()
print(actor)