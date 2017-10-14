#!/usr/bin/python3

periodic = ["h","he","li","be","b","c","n","o","f","ne","na","mg","al","si","p","s","cl","ar","k","ca","sc","ti","v","cr","mn","fe","co","ni","cu","zn","ga","ge","as","se","br","kr","rb","sr","y","zr","nb","mo","tc","ru","rh","pd","ag","cd","in","sn","sb","te","i","xe","cs","ba","la","ce","pr","nd","pm","sm","eu","gd","tb","dy","ho","er","tm","yb","lu","hf","ta","w","re","os","ir","pt","au","hg","tl","pb","bi","po","at","rn","fr","ra","ac","th","pa","u","np","pu","am","cm","bk","cf","es","fm","md","no","lr","rf","db","sg","bh","hs","mt","ds","rg","cn","nh","fl","mc","lv","ts","og"]

def calc_for_word(word):
    combos_at_letter = []
    if word[0] in periodic:
        combos_at_letter = [1, 1]
    else:
        combos_at_letter = [1, 0]
    for i in range(1, len(word)):
        combos_with_char = 0
        if word[i] in periodic:
            combos_with_char += combos_at_letter[i]
        if word[i-1:i+1] in periodic:
            combos_with_char += combos_at_letter[i-1]
        combos_at_letter.append(combos_with_char)
    return combos_at_letter[-1]

N = int(input())
for i in range(N):
    print(calc_for_word(input()))
