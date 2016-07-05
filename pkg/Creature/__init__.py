from os.path import basename, isfile
import glob
modules = glob.glob("**/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f == 'Creature\\Creature.py' and not
    f == 'Creature\\StatSheet.py' and not f[-5:-3] == 'AI' and not f[-5:-3] == '__']
print __all__
