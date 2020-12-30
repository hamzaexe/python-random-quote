import random
def primary():

  a = open("quotes.txt", "a")
  input_sentence=input("write your sentence: ")
  a.write(input_sentence + "\n")
  a.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes)-1
  print(last)
  rnd = random.randint(0, last)
  #print("Keep it logically awesome.")

 

  print(quotes[rnd], end = '')
  rnd = random.randint(0, last)
  print(quotes[rnd], end = '')

if __name__== "__main__":
  primary()
