# amount = float (input ('How much money was spend: '))
# member = int (input ('For how many people: '))

member = {}
# My goal is to have a dictrionary that has a person as key and his spendings within a list as the dict values

def addMember (myMemberDic):
    name = str (input('Who should we add: '))
    startAmount = float (input ('What has she/he spend already: '))

    return myMemberDic[name] = [startAmount] 
    # Check if this works. What I want to do is have each spending added as a list item. 
    # Within the dictionary 'member' each key is the name of a member and the key is a list of their spendings


def addCost (myMemberDic):
    newAmount = float (input('How much was spend: '))
    whoSpend = str (input ('Who spend this: '))
    myMemberDic
# I need to find a way to add the new amount value to the dict key as a new list element


def calculateSum (myMemberDic):
    cost = 0
    for i in myMemberDic:
        cost = cost + myMemberDic[i]

    return cost


newMember = addMember (member)

amount = calculateSum (member)

share = amount / len(member)

print ('Each person has to pay', share , 'Euros.')