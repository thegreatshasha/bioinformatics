def allindices(sub, string, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex

if __name__ == "__main__":
  pat = input()
  string = input()

  data = [7, 7, 7, 7]
  inds = allindices(pat, string)

  print(*inds, sep=' ')
