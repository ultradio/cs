"""
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n]) # !!

["sun", "bed", "car"]
n = 1
strings = ["abce", "abcd", "cdx"]
n = 2

print(solution(strings, n))

def solution(s):
    s = s.lower()
    p_cnt=0
    y_cnt=0
    for c in s:
        if c == 'p':
            p_cnt += 1 
        elif c == 'y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    else:
        return False
s="pPoooyY"
s="Pyy"

def solution(s):
    return s.lower().count('p') == s.lower().count('y')
print(solution(s))
"""

def solution(s):
    encodes = []
    if len(s) == 1:
        return 1
    for step in range(1, (len(s)//2)+1):
        cnt=0
        encode=[]
        for i in range(0, len(s), step):            
            if s[i:i+step] == s[i+step:i+2*step]:
                if cnt==0:
                    cnt=2
                    encode.append((s[i:i+step], cnt))
                else:
                    cnt+=1
                    encode[-1]=((s[i:i+step], cnt))
            else:
                cnt=0
                if len(encode) > 0:
                    #print(encode[-1][0], s[i:i+step], encode[-1][1])
                    if encode[-1][0]==s[i:i+step] and encode[-1][1] > 0:
                        pass
                    else:
                        encode.append((s[i:i+step], cnt))
                else:
                    encode.append((s[i:i+step], cnt))
            
            #print(step, i, i+step, i+2*step, s[i:i+step], s[i+step:i+2*step], encode)
        encode_str=''
        for (ch, cnt) in encode:
            if cnt == 0:
                encode_str+=ch
            else:
                encode_str+=str(cnt)+ch
        
        #print(len(encode_str), encode, encode_str, '\n')                
        encodes.append(len(encode_str))
                
    return min(encodes)

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))
    
#s="aabbaccc"
s="ababcdcdababcdcd"
print(solution(s))