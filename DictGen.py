import time  # 根據時間書寫版本號

# 19 個聲母
pHan = (
    'ᄀ', 'ᄁ', 'ᄂ', 'ᄃ', 'ᄄ',
    'ᄅ', 'ᄆ', 'ᄇ', 'ᄈ', 'ᄉ',
    'ᄊ', 'ᄋ', 'ᄌ', 'ᄍ', 'ᄎ',
    'ᄏ', 'ᄐ', 'ᄑ', 'ᄒ'
)
prefix = (
    'g', 'kk', 'n', 'd', 'tt',
    'r', 'm', 'b', 'pp', 's',
    'ss', '', 'j', 'cc', 'c',
    'k', 't', 'p', 'h'
)

# 21 個元音
iHan = (
    'ᅡ', 'ᅢ', 'ᅣ', 'ᅤ', 'ᅥ',
    'ᅦ', 'ᅧ', 'ᅨ', 'ᅩ', 'ᅪ',
    'ᅫ', 'ᅬ', 'ᅭ', 'ᅮ', 'ᅯ',
    'ᅰ', 'ᅱ', 'ᅲ', 'ᅳ', 'ᅴ',
    'ᅵ'
)
vHan = (
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ',
    'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
    'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
    'ㅣ'
)
infix = (
    'a', 'ae', 'ya', 'yae', 'eo',
    'e', 'yeo', 'ye', 'o', 'wa',
    'wae', 'oe', 'yo', 'u', 'weo',
    'we', 'wi', 'yu', 'eu', 'ui',
    'i'
)

# 28 個韻尾
sHan = (
    '', 'ᆨ', 'ᆩ', 'ᆪ', 'ᆫ',
    'ᆬ', 'ᆭ', 'ᆮ', 'ᆯ', 'ᆰ',
    'ᆱ', 'ᆲ', 'ᆳ', 'ᆴ', 'ᆵ',
    'ᆶ', 'ᆷ', 'ᆸ', 'ᆹ', 'ᆺ',
    'ᆻ', 'ᆼ', 'ᆽ', 'ᆾ', 'ᆿ',
    'ᇀ', 'ᇁ', 'ᇂ'
)
cHan = (
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ',
    'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',  # ㄸ after ㄷ
    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
    'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',  # ㅃ after ㅂ
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',  # ㅉ after ㅈ
    'ㅌ', 'ㅍ', 'ㅎ'
)
suffix = (
    '', 'g', 'kk', 'gs', 'n',
    'nj', 'nh', 'd', 'l', 'lg',
    'lm', 'lb', 'ls', 'lt', 'lp',
    'lh', 'm', 'b', 'bs', 's',
    'ss', 'ng', 'j', 'c', 'k',
    't', 'p', 'h'
)


fin = open('DictSrc.in', 'r', encoding='utf-8')
fout = open('hangeul.dict.yaml', 'w', encoding='utf-8')

fout.write('# Rime dictionary\n')
fout.write('# encoding: utf-8\n')
fout.write('#\n# 諺文 - 한글 - Hangeul\n#\n\n')

fout.write('---\n')
fout.write('name: hangeul\n')
fout.write(f'version: "{time.strftime("%Y.%m.%d", time.localtime())}"\n')
fout.write('sort: original\n')
fout.write('...\n\n')

for p in range(19):
    if pHan[p] == 'ᄋ': fout.write('ᄋ\tq-\n')
    else: fout.write(f'{pHan[p]}\t{prefix[p]}-\n')
for i in range(21):
    fout.write(f'{iHan[i]}\t-{infix[i]}-\n')
for s in range(1, 28):
    fout.write(f'{sHan[s]}\t-{suffix[s]}\n')

for s in range(1, 28):
    if cHan[s] == 'ㅇ': fout.write('ㅇ\txq\n')
    fout.write(f'{cHan[s]}\tx{suffix[s]}\n')
    if cHan[s] == 'ㄷ': fout.write('ㄸ\txtt\n')
    elif cHan[s] == 'ㅂ': fout.write('ㅃ\txpp\n')
    elif cHan[s] == 'ㅈ': fout.write('ㅉ\txcc\n')
for i in range(21):
    fout.write(f'{vHan[i]}\tx{infix[i]}\n')

for p in range(19):
    for i in range(21):
        for s in range(28):
            x = fin.read(1)
            fout.write(f'{x}\t{prefix[p]}{infix[i]}{suffix[s]}\n')
            fin.read(1)

fin.close()
fout.close()
