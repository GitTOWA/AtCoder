list = [4,10,1]

def rec_plus(list, now ,sum): # sum は現在までの和を保持するために用いる
  if now<3:
    # now番目を足す時 + now番目を足さない時
    return rec_plus(list, now+1, sum+list[now]) + rec_plus(list, now+1, sum) 
  else:
    return sum
  
print(rec_plus(list,0,0)) # 出力は60