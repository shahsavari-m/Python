
input_shape= input("Enter your shape:Triangle ? Rectangle ? Circle ? \n")
input_func= input("Enter your function: Enviroment ? Area \n")
if  input_shape== "Rectangle":
    tool = float(input("Enter tool\n"))
    arz = float(input("Enter arz\n"))
    dastoor= input_func
    def mostatil (tool, arz, dastoor):
        if dastoor== "Enviroment" :
            return (tool+arz)*2
        elif dastoor== "Area" :
            return (tool*arz)
        else:
            return "Amaliyat na moatabar"
    result1 =  mostatil (tool, arz, dastoor)
    print (result1)

elif input_shape== "Triangle" and input_func == "Area":
    ertefa = float(input("Enter ertefa\n:"))
    ghaede = float(input("Enter ghaede\n:"))
    dastoor= input_func
    def mosalas_masahat ( ertefa, ghaede, dastoor):
        if dastoor == "Area" :
            return (.5*ertefa*ghaede)
        else : print("tt")
    result3= mosalas_masahat (ertefa, ghaede, dastoor)
    print (result3)

elif input_shape== "Triangle" and input_func == "Enviroment":
    zel1 = float(input("Enter zel1\n:"))
    zel2 = float(input("Enter zel2\n:"))
    ghaede = float(input("Enter ghaede\n:"))
    dastoor= input_func
    def mosalas_mohit(ghaede , zel1, zel2, dastoor):
        if dastoor == "Enviroment" :
            return (zel1+zel2+ghaede)
        else:
            return "Amaliyat na moatabar"
    result2 = mosalas_mohit (ghaede, zel1, zel2, dastoor)
    print (result2)

elif input_shape == "Circle":
    shoaa= float(input("Enter Shoaa:\n"))
    dastoor= input_func
    def dayere (shoaa , dastoor):
        if dastoor == "Enviroment" :
            return (2*3.14*shoaa)
        elif dastoor == "Area" :
            return (3.14*shoaa*shoaa)
        else :
            return "Amaliyat na moatabar"
    result4 = dayere (shoaa , dastoor)
    print(result4)
