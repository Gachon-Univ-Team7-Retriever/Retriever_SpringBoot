# 현재 구동 중인 운영체제를 확인하고 만약 Windows일 경우 허용되지 않는 문자를 대체하는 코드

import platform
import re

def sanitize_filename(filename):
    if platform.system() == "Windows":
        # Windows에서 허용되지 않는 문자를 대체
        return re.sub(r'[<>:"/\\|?*]', '_', filename)