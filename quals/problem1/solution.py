def noFours(num):
  num = str(num)[::-1]

  res1, res2 = 0, 0


  for i in range(len(num)):
    # if the current digit is 4: split it into 2's, multiply by the proper exponent (based on ten's place), and each to res1 and res2
    if num[i] == "4":
        res1 += 2*10**i
        res2 += 2*10**i
    # else if current digit is not 4: simply add the digit * proper exponent to res1
    else:
        res1 += int(num[i])*10**i
  return "{} {}".format(res1, res2)
