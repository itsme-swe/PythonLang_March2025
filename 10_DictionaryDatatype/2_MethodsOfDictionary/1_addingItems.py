s1 = {101: "Rohan", 102: "Sohan", 103: "Manoj"}

s1[104] = {"James"}

s1[103] = {
    "Tison"
}  # if the key is already present it will update the existing item, with new value

print(s1) # {101: 'Rohan', 102: 'Sohan', 103: {'Tison'}, 104: {'James'}}
