from os.path import basename, isfile
import glob
modules = glob.glob("**/*.py")
print (modules)
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f == 'Creatures\\creature.py' and not
    f == 'Creatures\\statsheet.py' and not f[-5:-3] == 'AI' and not f[-5:-3] == '__']
print(__all__)
