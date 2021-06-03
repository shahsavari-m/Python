input_tool = float(input("enter tool\n"))
input_arz = float(input("enter arz\n"))
input_dastoor = input("enter dastoor")
def mostatil_1 (tool, arz , dastoor):
      if dastoor == "mohit" :
           mohit = tool*2 + arz*2
           return mohit
      elif dastoor == "masahat" :
           masahat = tool * arz
           return masahat
result = mostatil_1 (input_tool, input_arz, input_dastoor)
print(result)
