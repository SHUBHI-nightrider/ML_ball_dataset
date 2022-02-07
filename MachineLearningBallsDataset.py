from sklearn import tree
def MarvellousML(weight,surface):
    BallsFeatures = [[35,1],[47,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(BallsFeatures,Names)
    result = clf.predict([[weight,surface]])
    if result == 1:
        print("Your Object looks like Tennis ball")
    elif result ==2:
        print("Your object looks like cricktet ball")
def main():
    print("shubham infosystem by shubham yeljale")
    print("Enter weight of the object")
    weight = input()
    print("what is the surface type of your object rough or smooth")
    surface = input()
    if surface.lower() =="rough":
        surface =1 
    elif surface.lower()=="smooth":
        surface = 0
    else:
        print("Error: wrong input")
        exit()
    MarvellousML(weight,surface)
if __name__ == "__main__":
    main()