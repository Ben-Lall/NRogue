from os.path import basename, isfile
import glob
modules = glob.glob("**/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f == 'Creature\\creature.py' and not
    f == 'Creature\\statSheet.py' and not f[-5:-3] == 'AI' and not f[-5:-3] == '__']
