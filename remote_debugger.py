# -*- coding: utf-8 -*-
"""
@Author: Faith
@Date: 2026/2/12
@Time: 20:16
@Description:
@FilePath: remote_debugger.py
"""
import sys
from importlib import reload

def attach_to_debugger(host, port):
    try:
        # TODO : Use your PyCharm install directory.
        pydev_path = r"D:\bd\UEPythonProject\.venv\Lib\site-packages"

        if not pydev_path in sys.path:
            sys.path.append(pydev_path)

        import pydevd_pycharm
        pydevd_pycharm.stoptrace()
        pydevd_pycharm.settrace('localhost', port=60058, stdout_to_server=True, stderr_to_server=True, suspend=False)
        print("PyCharm Remote Debug enabled on %s:%s." % (host,port))
    except:
        import traceback
        traceback.print_exc()

attach_to_debugger('localhost', 60058)