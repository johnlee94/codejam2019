def decryptPanagram(N, L, ints):

  allPrimes, primes, key = list(), list(), dict()

  #  STEP 1: find all primes up to N
  for num in range(2,N):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        allPrimes.append(num)

  # STEP 2: find the 26 unique primes that are being used

  ## find the first prime number in sequence
  for prime in allPrimes:
    if ints[0]%prime == 0:
      # to check to see which prime is first in sequence, see which prime
      # in the pair is divisible into next number in sequence
      if ints[1]%prime == 0:
        primes.append(ints[0] / prime)
        primes.append(prime)
      else:
        primes.append(prime)
        primes.append(ints[0] / prime)

  ## find the rest of prime numbers in sequence and add them in order of the given input list
  for i in range(1, len(ints)):
    primes.append(ints[i] / primes[-1])

 # I'm shaving off first 2 cause they are repeats and i'm bad
  primes = primes[2:]

 # Sort and order primes into a set, smallest prime should be 'a', and biggest prime should be 'z'
  uniqueSortedPrimes = set(sorted(primes))

  # map used primes to the alphabets to make the decrypting map
  alphabets = "abcdefghijklmnopqrstuvwxyz"
  for i, prime in enumerate(uniqueSortedPrimes):
    key[prime] = alphabets[i]

  encrypted = ""

  # finally decrypt the original (with possible repeating primes) primes sequence to reveal message!
  for prime in primes:
    encrypted += key[prime]

  print encrypted


decryptPanagram(103, 31, [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053])
