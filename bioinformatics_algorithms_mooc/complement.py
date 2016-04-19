compl = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

code = raw_input()

code2 = [compl[s] for s in code]
code2.reverse()

print ''.join(code2)

