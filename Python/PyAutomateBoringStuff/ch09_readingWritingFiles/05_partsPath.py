from pathlib import Path

# Parts of a Path
p = Path.cwd() / '01_joinPaths.py'
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

# Parents array (still parts of a path)
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
print(p.parents[5])