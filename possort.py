import re
with open('/Users/user/uniquelemmas_pos.txt', 'r', encoding = 'utf-8') as file:
    nouns = []
    verbs = []
    adj = []
    other = []
    lines = file.readlines()
    for line in lines:
        #print(line)
        if 'NOUN' in line:
            nouns.append(re.match('.*\t',line).group(0))
        elif 'VERB' in line:
            verbs.append(re.match('.*\t',line).group(0))
        elif 'ADJ' in line:
            adj.append(re.match('.*\t',line).group(0))
        else:
            other.append(re.match('.*\t',line).group(0))
    with open('/Users/user/Desktop/nouns.txt', 'w', encoding = 'utf-8') as n:
        for noun in nouns:
            n.write(noun)
            n.write('\n')

    with open('/Users/user/Desktop/verbz.txt', 'w', encoding = 'utf-8') as v:
        for verb in verbs:
            v.write(verb)
            v.write('\n')
    with open('/Users/user/Desktop/adjectives.txt', 'w', encoding = 'utf-8') as a:
        for adjective in adj:
            a.write(adjective)
            a.write('\n')
    with open('/Users/user/Desktop/other.txt', 'w', encoding = 'utf-8') as o:
        for item in other:
            if item:
                o.write(item)
                o.write('\n')
