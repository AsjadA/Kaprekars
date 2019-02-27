def Kaprekar(num):
    num=str(num)
    count=0
    value=num

    while value!="6174":
        if len(value)==3:
            value=value+"0"
        elif len(value)==2:
            value=value+"00"
        elif len(value)==1:
            value=value+"000"
        array=[]
        ascendfinal=""
        descendfinal=""
        for i in range(0,len(value)):
            array.append(value[i])
        ascend=sorted(array)
        for i in ascend:
            ascendfinal=ascendfinal+i
        descend=ascend[::-1]
        for j in descend:
            descendfinal=descendfinal+j
        value=str(int(descendfinal)-int(ascendfinal))
        count+=1
    print(count)
Kaprekar(3524)
