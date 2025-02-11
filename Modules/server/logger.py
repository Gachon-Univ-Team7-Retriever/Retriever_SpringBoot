import logging
from logging.handlers import RotatingFileHandler
import sys
import os
import time


# ANSI 컬러 코드
class AnsiCode:
    RESET_ALL = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    INVERSE = '\033[7m'
    WHITE_TEXT = '\033[37m'
    BRIGHT_RED_TEXT = '\033[91m'
    BRIGHT_GREEN_TEXT = '\033[92m'
    BRIGHT_YELLOW_TEXT = '\033[93m'
    BRIGHT_BLUE_TEXT = '\033[94m'
    BRIGHT_MAGENTA_TEXT = '\033[95m'
    BRIGHT_CYAN_TEXT = '\033[96m'
    BRIGHT_WHITE_TEXT = '\033[97m'
    BRIGHT_RED_BACKGROUND = '\033[101m'
    BRIGHT_GREEN_BACKGROUND = '\033[102m'
    BRIGHT_YELLOW_BACKGROUND = '\033[103m'
    BRIGHT_BLUE_BACKGROUND = '\033[104m'
    BRIGHT_MAGENTA_BACKGROUND = '\033[105m'
    BRIGHT_CYAN_BACKGROUND = '\033[106m'
    BRIGHT_WHITE_BACKGROUND = '\033[107m'


# Following from Python cookbook, #475186
def has_colors(stream):
    import curses
    curses.setupterm()
    return curses.tigetnum("colors") > 2


def print_colored(color=AnsiCode.BRIGHT_WHITE_TEXT):
    if has_colors(sys.stdout):
        # 문자열 포매팅 후 반환
        log_format = "[%(asctime)s] %(levelname)7s in %(module)s: %(message)s"
        return log_format
    else:
        return "[%(asctime)s] %(levelname)7s in %(module)s: %(message)s"


'''
Loggin 모듈에서 로깅 작업은 Handler, Formatter 두 가지 계열의 클래스로 이루어진다.
Formatter는 로그 정보(로그 시간, 파일 이름, 메세지 등)의 문자열 형식과 배치를 규정하고,
Handler는 그렇게 만들어진 로그를 어떻게 처리할 것인지(콘솔에 출력, 또는 로그 파일에 기록) 결정한 다음 처리를 수행한다.

한 번 Handler가 로그 메세지를 처리하고 나면, Foramtter에 의해서 바뀐 문자열 형식은 다음 Handler에 이미 포매팅된 상태로 전달된다.
즉, 여러 개의 Handler에서 서로 다른 포맷을 사용하게 하고 싶다면, 각각 다른 포맷을 지정해 주어야 한다.
'''


# 시간 형식을 바꾸고 로그가 호출된 파일의 디렉토리를 record.directory에 저장하는 기본 Formatter
# 다른 Formatter들이 이 클래스를 오버라이드함
class BasicCustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        # 원래의 형식을 유지하되, 시간 포맷에서 밀리초 구분자를 변경
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            s = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            s = f"{s}.{int(record.msecs):03d}"  # 콤마 대신 점 사용, 표시하는 밀리초 단위를 4자리까지로 변경
        return s

    def format(self, record):
        record.directory = self.get_directory_format(record)
        return super().format(record)

    # record.pathname의 디렉토리 정보를 구하는 메서드.
    @staticmethod
    def get_directory_format(record):
        return os.path.dirname(record.pathname)


# 로그 파일에 기록하는 포맷으로 포매팅하는 Formatter
class LogFileFormatter(BasicCustomFormatter):
    default_format = "%(asctime)s, %(levelname)s, %(filename)s, %(directory)s, %(message)s"

    def __init__(self):
        super().__init__(self.default_format)

LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs/flask.log")

# 콘솔에 출력하는 형식과 색상을 지정하는 Formatter
class ColorfulFormatter(BasicCustomFormatter):
    default_format = (AnsiCode.BRIGHT_WHITE_TEXT
                      + "[%(asctime)s] %(levelname)s from %(filename)s in %(directory)s: %(message)s"
                      + AnsiCode.RESET_ALL)

    # 기본 색상의 시작을 밝은 흰색으로 설정
    def __init__(self):
        super().__init__(self.default_format)

    COLORS = {
        logging.DEBUG: AnsiCode.BRIGHT_BLUE_TEXT,
        logging.INFO: AnsiCode.BRIGHT_GREEN_TEXT,
        logging.WARNING: AnsiCode.BRIGHT_YELLOW_TEXT,
        logging.ERROR: AnsiCode.BRIGHT_RED_TEXT,
        logging.CRITICAL: AnsiCode.BRIGHT_MAGENTA_TEXT,
    }

    default_color = AnsiCode.RESET_ALL + AnsiCode.BRIGHT_WHITE_TEXT

    def format(self, record):
        text_highlight = self.COLORS.get(record.levelno, AnsiCode.BRIGHT_WHITE_TEXT)
        background_highlight = self.COLORS.get(record.levelno, AnsiCode.BRIGHT_WHITE_TEXT) + AnsiCode.INVERSE

        # record의 Attribute에 ANSI 코드를 추가하여 출력되는 색상 변경.
        # 주의사항: record.asctime은 문자열 포매팅 시점에 동적으로 생성되므로, 아래와 같은 방식을 시도할 시 오류 발생.
        record.levelname = f"{background_highlight} {AnsiCode.BOLD}{record.levelname} {self.default_color}"
        record.filename = f"{text_highlight}{AnsiCode.BOLD}{record.filename}{self.default_color}"
        record.msg = f"{text_highlight}{record.msg}{self.default_color}"

        # record.directory라는 Attribute를 생성하면, 이후에 format 문자열에서 %(directory)s라는 placeholder를 사용할 수 있게 된다.
        record.directory = self.get_directory_format(record)

        return super().format(record)

    # record.pathname의 디렉토리 정보를 구하는 메서드를 오버라이드하여, 어두운 흰색과 이탤릭채가 반영된 형태로 반환하도록 변경
    @staticmethod
    def get_directory_format(record):
        return (f"{AnsiCode.WHITE_TEXT}{AnsiCode.ITALIC}"
                f"{BasicCustomFormatter.get_directory_format(record)}{ColorfulFormatter.default_color}")

# 특정 패키지의 하위 모듈들에서만 로깅 메세지가 출력되도록 설정하는 Filter 클래스.
# 이 Filter 클래스를 만들고 Modules 패키지에 추가하는 코드를 더하지 않을 경우, site-packages에 들어 있는 라이브러리의 로깅 모듈까지 전부 출력되는 문제가 발생함.
class ModuleFilter(logging.Filter):
    def __init__(self, module_name):
        super().__init__()
        self.module_name = module_name

    def filter(self, record):
        # 로그 레코드의 모듈이 필터에서 지정한 패키지의 자손 파일이라면 허용. 예외로, flask 서버 자체의 로깅 기능을 관장하는 werkzeug를 추가 허용.
        return record.pathname.startswith(self.module_name) or record.name.startswith("werkzeug")

# 패키지 또는 모듈 이름으로 필터링 -> "Modules" 디렉토리에서 __file__ 속성을 가져와서 활용.
from Modules import __file__ as ROOT_FILE_DIR
MODULE_NAME = os.path.dirname(ROOT_FILE_DIR)
print(f"Root directory of logging server", MODULE_NAME)

# 로그를 파일에 기록하는 Handler
os.makedirs(os.path.join(os.path.dirname(LOG_PATH), "logs"), exist_ok=True)
logFileHandler = RotatingFileHandler(LOG_PATH, maxBytes=10000000, backupCount=5, encoding='utf-8')
logFileHandler.setFormatter(LogFileFormatter())

# 로그를 콘솔에 출력하는 Handler
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(ColorfulFormatter())

# 파일과 콘솔 핸들러에 필터 추가. 현재 flask 서버의 패키지 이름을 기준으로 필터링하기 때문에 라이브러리 등의 로깅 메세지는 무시된다.
logFileHandler.addFilter(ModuleFilter(MODULE_NAME))
consoleHandler.addFilter(ModuleFilter(MODULE_NAME))

# handler 인자로 입력한 리스트의 핸들러가 순차적으로 실행되므로,
# 로그의 형식 변경 -> 로그 파일에 기록 -> 콘솔에 출력 시의 색상 변경의 순으로 작동한다.
logging.basicConfig(level='DEBUG', handlers=[logFileHandler, consoleHandler])

logger = logging.getLogger(__name__)


# 쓰이지 않지만 나중을 위해 남겨둔 함수. flask logger를 변경하는 함수이다.
def customize_flask_logger(flask_app):
    # Flask 기본 로거 설정 제거
    del flask_app.logger.handlers[:]

    # 로거의 레벨을 디버그 이상으로 설정해야 디버그 메세지가 필터링되지 않는다.
    flask_app.logger.addHandler(logFileHandler)
    flask_app.logger.addHandler(consoleHandler)


if __name__ == '__main__':
    # 모듈 사용 테스트
    logger.debug('DEBUG logging test.')
    logger.info('INFO logging test.')
    logger.warning('WARNING logging test.')
    logger.error('ERROR logging test.')
    logger.critical('CRITICAL logging test.')