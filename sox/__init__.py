#!/usr/bin/env python
""" init method for sox module """
from .log import logger
import os
import sys

# Check that SoX is installed and callable
NO_SOX = False
sox_path = "sox"
if hasattr(sys, '_MEIPASS'):
    sox_path = os.path.abspath(os.path.join(sys._MEIPASS, "sox"))

stream_handler = os.popen('%s -h' % sox_path)
if not len(stream_handler.readlines()):
    logger.warning("""SoX could not be found!

    If you do not have SoX, proceed here:
     - - - http://sox.sourceforge.net/ - - -

    If you do (or think that you should) have SoX, double-check your
    path variables.
    """)
    NO_SOX = True
stream_handler.close()

from . import file_info
from .combine import Combiner
from .transform import Transformer
from .core import SoxError
from .core import SoxiError
from .version import version as __version__
