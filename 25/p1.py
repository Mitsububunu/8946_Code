import hashlib

text = ['あ','い','う','え','お',
        'か','き','く','け','こ',
        'さ','し','す','せ','そ',
        'た','ち','つ','て','と',
        'な','に','ぬ','ね','の',
        'は','ひ','ふ','へ','ほ',
        'ま','み','む','め','も',
        'や','ゆ','よ',
        'ら','り','る','れ','ろ',
        'わ','を','ん'
        'が','ぎ','ぐ','げ','ご',
        'ざ','じ','ず','ぜ','ぞ',
        'だ','ぢ','づ','で','ど',
        'ば','び','ぶ','べ','ぼ',
        'ぱ','ぴ','ぷ','ぺ','ぽ',
        'ぁ','ぃ','ぅ','ぇ','ぉ',
        'ゃ','ゅ','ょ',
        'っ']

password = ""
for i in text:
    for j in text:
        for k in text:
            for l in text:
                p = i + j + k + l

                if hashlib.md5(p.encode('utf-8')).hexdigest() == '816abf889b5f21a6a5d5cf604f9bd6eb':
                    password = p
                    break       


print(password)
