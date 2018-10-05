#!c:\pythin35\python35\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'cpplint==1.3.0','console_scripts','cpplint'
__requires__ = 'cpplint==1.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cpplint==1.3.0', 'console_scripts', 'cpplint')()
    )
