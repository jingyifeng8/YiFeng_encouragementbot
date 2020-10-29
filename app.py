print("Title of program: Yi Feng's Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy" or "good":
      feelings_list.append("happy")
      encouragement_list.append("success is not permanent")
      counter += 1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("there is always a next time to do well")
      counter += 1
    if each_word == "tired" or "exhausted":
      feelings_list.append("tired")
      encouragement_list.append("you should rest well")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("you will do better next time")
      counter += 1
    if each_word == "terrible" or "bad":
      feelings_list.append("bad")
      encouragement_list.append("things will definitely get better")
      counter += 1
     if each_word == "neutral" or "meh":
      feelings_list.append("neutral")
      encouragement_list.append("try to smile more so you can lift your spirits")
      counter += 1
     if each_word == "nervous" or "anxious":
      feelings_list.append("nervous")
      encouragement_list.append("you can do it! Don't underestimate yourself")
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
