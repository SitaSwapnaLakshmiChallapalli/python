for j in range(len(l)+3):
    z=input()
    ind=[c[0] for c in enumerate(l) if c[1]==z]
    for k in ind:
        
        l2[k]=z
        final_str="".join(l2)
        print(l2)
        if(final_str==n):
            print("congratulations")
        
print("better luck next time")
print("The word is: ",n)
