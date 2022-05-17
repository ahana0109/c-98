def countwords():
    filename= input("enter the name of the file: ")
    file=open(filename,'r')
    countwords=0
    for line in file:
        words=line.split( )
        countwords=countwords+len(words)
    print(countwords)

countwords()
