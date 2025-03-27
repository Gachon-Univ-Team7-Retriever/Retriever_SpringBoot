from charset_normalizer import detect

def to_utf8(html_text):
    detected = detect(html_text)
    encoding = detected.get('encoding')
    if not encoding:
        raise ValueError("인코딩을 감지할 수 없습니다.")
    return html_text.decode(encoding).encode('utf-8')
