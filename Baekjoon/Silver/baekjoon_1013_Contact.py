def contact():
    strn = input()
    while strn:
        if strn[:2] == '01':
            strn = strn[2:]
        elif strn[:3] == '100':
            strn = strn[3:].lstrip('0')
            if strn.startswith('11'):
                if strn.lstrip('1').startswith('01') or strn.lstrip('1') == '':
                    strn = strn.lstrip('1')
                elif strn.lstrip('1').startswith('00'):
                    strn = '1' + strn.lstrip('1')
            elif strn.startswith('1'):
                if strn.lstrip('1') == '' or strn.lstrip('1').startswith('01'):
                    strn = strn.lstrip('1')
                else:
                    return 'NO'
            else: 
               return 'NO'
        else:
            return 'NO'
    return 'YES'

res = ''
for _ in range(int(input())):
    res += contact() + '\n'

print(res)

