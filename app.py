print("Title of program: Yi Feng's Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("success is not permanent. Keep working hard!")
      counter += 1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("there is always a next time to do well. Hope you are feeling better!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you should rest well, Hope you are feeling better!")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("you will do better next time. Hope you are feeling better!")
      counter += 1
    if each_word == "upset":
      feelings_list.append("upset")
      encouragement_list.append("you will do better next time. Hope you are feeling better!")
      counter += 1
    if each_word == "ecstatic":
      feelings_list.append("ecstatic")
      encouragement_list.append("success is not permanent. Keep working hard!")
      counter += 1
    if each_word == "anxious":
      feelings_list.append("anxious")
      encouragement_list.append("results are not everything. Hope you are feeling better!")
      counter += 1
      
  if counter == 0:
    
      output = "Sorry, I don't really understand. Please use a different word."

  elif counter == 1:
    
      output = "It seems that you are feeling " + feelings_list[0] + ". Do remember that "+ encouragement_list[0]

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
