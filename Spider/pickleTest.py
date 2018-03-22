import pickle

lyst = [60, "A string ", 1977]
fileObj = open("items.dat", 'wb')
for item in lyst:
    pickle.dump(item,fileObj)
fileObj.close()