print("Title of program: Yi Feng's Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("success is not permanent")
      counter += 1
    if each word == "surprise":
      feelings_list.append("surprise")
      encouragement_list.append ("i hope it was a pleasant surprise!")
      counter+= 1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("dont give up! there is always a second chance.")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you should rest well")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("today is just a grey cloud passing over, tomorrow will be better.")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
