import os
def count_lines(filename):
    with open(filename, "r") as file:

        txt_file = file.read()
        colist = txt_file.split("\n")
        count=0
        for i in colist:
            if i:
                count+=1

    return count


os.chdir('/media/tamim/Study/Datasets/Ozfish/roboflow/ozfish.v1-batch01_check01.darknet/train/annot')
total=0
for f in os.listdir():
    total+=count_lines(f)

print("Total lines in this dir:", total)    