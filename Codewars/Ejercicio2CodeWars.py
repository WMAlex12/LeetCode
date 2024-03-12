def likes(names):
    # your code here
    
    name = [str(n) for n in names if isinstance(n, str)]
    if (len(name)<= 0):
        return "no one like this"
    if (len(name)== 1):
        return " ".join(name) + " likes this"   
    if (len(name)== 2):
        return " and ".join(name) + " like this"
    if (len(name) == 3): 
        return ", ".join(name[0:2]) + " and " + " ".join(name[2:]) + " like this"
    if (len(name) > 3): 
        return ", ".join(name[0:2]) + " and " + str(len(name)-2) + " others like this"
    else: 
        pass
print(likes([]))

print(likes(["John", "Jane", "Alex", "Juan"]))
