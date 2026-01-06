# Read file appended in last
# f = open("sample.txt", "a")

# # data = f.read()

# # print(data)
# # f.seek(0)

# # line1 = f.readline()
# # line2 = f.readline()

# f.write("\nNew text is added")

# print(f)

# f.close()


#create file
# f = open("sample2.txt", "x")

# f.write("Hello this is new file")

# f.close()

# dont need close when open with
# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)


#delete file
import os
os.remove("sample2.txt")