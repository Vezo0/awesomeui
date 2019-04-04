from bin.gui.gui import _gui
import sys
if __name__ == "__main__":
    _mod = sys.modules['demo'] = sys.modules[__name__]
    _gui()

