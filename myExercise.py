import sys
class Studentnotinlisterror(Exception):
    pass
with open(sys.argv[1],"r") as studentfile:
    student_raw,studentdict=studentfile.readlines(),{}

for i in student_raw:
    studentdict[i.split(":")[0]]=i.split(":")[1]

input2=sys.argv[2].split(",")

for i in input2:
    try:
        if i not in studentdict.keys():
            raise Studentnotinlisterror
        print("Name:",i,"University:",studentdict[i])
    except Studentnotinlisterror:
        print("No record of '{}' was found!".format(i))
