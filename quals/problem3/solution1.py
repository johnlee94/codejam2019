def decryptPanagram(N, L, ints):

  primes, charMap = set(), dict()

  # search through all primes up to N until you find a prime that is used in the input
  for num in range(2,N):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        for value in ints:
          # if any of the primes we are calculating is divisible into any of the values in the given list input, it means we found our first used prime number
          if (value % num == 0):
            primes.add(num)
            primes.add(value/num)
            break


  level, unseen = primes.copy(), set(ints)

  while level:
    curr = level.pop()
    for num in unseen:
      next_unseen = unseen.copy()
      if num % curr == 0:
        primes.add(num/curr)
        next_unseen.remove(num)
        level.add(num/curr)
    unseen = next_unseen

  alphabets = "abcdefghijklmnopqrstuvwxyz"
  index=0
  for prime in primes:
    charMap[prime] = alphabets[index]
    index += 1

 #find the order in which the primes are used in sequence
  sequencedPrimes = list()

  for prime in primes:
    if ints[0] % prime == 0:
        sequencedPrimes.append(ints[0] / prime)
        sequencedPrimes.append(prime)

  for i in range(1, len(ints)):
    sequencedPrimes.append(ints[i] / sequencedPrimes[-1])

  encrypted = ""
  for prime in sequencedPrimes:
    encrypted += charMap[prime]

  return encrypted


print(decryptPanagram(103, 31, [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]))
