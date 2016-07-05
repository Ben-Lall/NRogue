from os.path import basename, isfile
import glob
modules = glob.glob("**/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f == 'Item\\item.py' and not
    f == 'Item\\consumable.py' and not f[-5:-3] == '__']
