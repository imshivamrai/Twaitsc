s1 = (int)(input('Score of first player:'))
s2 = (int)(input('Score of second player:'))
s3 = (int)(input('Score of third player:'))
sr1 = ((s1/60)*100)
sr2 = ((s2/60)*100)
sr3 = ((s3/60)*100)
print('strike rates are :',sr1,sr2,sr3)
print("Maximum number of sixes by player first:", s1//6)
print("Maximum number of sixes by player second:", s2//6)
print("Maximum number of sixes by player third:", s3//6)