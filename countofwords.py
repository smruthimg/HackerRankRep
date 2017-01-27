def countofwords(str):
    dictK={}
    dictS={}
    str=str.strip()

    for i in range(len(str)):
        for j in range(len(str)+1):
            if str[i] not in ('A','E','I','O','U')  and str[i:j] !='' :
                if str[i:j] not in dictS :
                    dictS[str[i:j]]=1
                else:
                    dictS[str[i:j]] += 1
            elif str[i]  in ('A','E','I','O','U')  and str[i:j] !='':
                if str[i:j] not in dictK :
                    dictK[str[i:j]] = 1
                else:
                    dictK[str[i:j]] += 1

    if sum(dictS.values())>sum(dictK.values()):
        print('Stuart',sum(dictS.values()))
    elif sum(dictS.values())<sum(dictK.values()):
        print('Kevin ', sum(dictK.values()))
    else:
        print('Equal')

    print(dictS)
    print(dictK)


countofwords('BANANA')