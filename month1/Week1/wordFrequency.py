

def displayWordfre(ordered):
    print("##########################################")
    print("\nword \t\t frequency\n")
    for i in ordered:
        print("{} \t\t {}".format(i, ordered[i]))
    print("##########################################")

def topN(ordered):
    print("##########################################")
    print("Enter the number top elements: ")
    num = int(input())

    print("\nword \t\t frequency\n")
    for i, v in enumerate(ordered):
        print("{} \t\t {}".format(v, ordered[v]))
        if i == num - 1:
            break
    print("##########################################")

def specificWord(ordered):
    print("##########################################")
    print("Enter the word: ")
    word = input()
    if word not in ordered.keys():
        print("\n{} is not found".format(word))
    else:
        print("\n{} -> {}".format(word, ordered[word]))
    print("##########################################")

def main():
    print("enter a paragraph: ", end="")
    par = str(input())
    token = par.split(" ")
    fre = {}
    ordered = {}

    for v in token:
        if v in fre.keys():
            fre[v] += 1
        else:
            fre[v] = 1
    ordered = sorted(fre.items(), key= lambda x : x[1], reverse= True)
    ordered = {x : y for x, y in ordered}

    while (True):
        print("\t\t menu")
        print("1 To display word frequency\n2 To display top N word frequency\n3 To display a specific word frequency\n0 To exit")
        print("choice: ")
        num = int(input())
        if num == 1:
            displayWordfre(ordered)
        elif num == 2:
            topN(ordered)
        elif num == 3:
            specificWord(ordered)
        elif num == 0:
            break


main()

    