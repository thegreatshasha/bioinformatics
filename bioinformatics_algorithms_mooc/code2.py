from collections import Counter

def frequentWords(string, k):
  cnt = Counter()
  words = []

  for i in range(len(string)-k+1):
    window = string[i:i+k]
    cnt[window] += 1

  common = cnt.most_common()
  max_count = common[0][1]
  
  for pair in common:
    if pair[1] == max_count:
      words.append(pair[0])
    else:
      return words
  return words

def main():
  txt = input()
  num = int(input())
  print(' '.join(frequentWords(txt, num)))

if __name__ == "__main__":
  main()
