data =  True
line = 1
word = "software"

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"{word} found at  line number {line}")
            break
        line+=1