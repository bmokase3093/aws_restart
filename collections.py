"""
Working with Lists, Tuples, and Dictionaries
"""
myFruitList = ["apple", "banana", "Cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#Changing the values in a list
myFruitList[2] = "orange"
print(myFruitList)

#Exercise 2: Introducing the tuple data type
myFinalAnswerTuple = ("apple","banana", "pineaple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#accesing a tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Exercise 3: Inroducing dictionary data type
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineaple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Accessing dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
