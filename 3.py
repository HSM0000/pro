def solution(n, t, m, p):
    count=0
    list1 = [i for i in range(t*m+p-1)]
    arr=[i for i in range(t)]
    for i in range(t*m) :
        rev_base = ''
        num=i
        if i ==0 :
            list1[count]=str(0)
            count=count+1
        while num > 0:#n진수 변환
            num, mod = divmod(num, n)
            if mod>=10 :
                rev_base += str(chr(mod+55))
            else :
                rev_base += str(mod)
        st= rev_base[::-1]
        for i in range(len(st)) :
            list1[count]=st[i]
            count=count+1
            if count==t*m :
                break;
        if count==t*m :
            break;
    for i in range(t) :
        arr[i]=list1[i*m+p-1]
    arr1="".join(arr)
    return arr1