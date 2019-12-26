# get content
import orbit_utils
import read_utils
from orbit import Orbit

stringlist = read_utils.getinput2("day6.txt")
orbits = list()
for item in stringlist:
    items = item.strip().split(")")
    orbits.append(Orbit(items[0], items[1]))

count = orbit_utils.count_orbits(orbits)
print("Question 6A: Total orbits: ", count)

# Question 6B
santaorbit = orbit_utils.find_orbiter("SAN", orbits)
santapath = orbit_utils.find_path(santaorbit, orbits, list())
youorbit = orbit_utils.find_orbiter("YOU", orbits)
youpath = orbit_utils.find_path(youorbit, orbits, list())

cross_orbit = orbit_utils.find_crossing(santapath, youpath)
steps = youpath.index(cross_orbit) + santapath.index(cross_orbit)

print("Question 6B: Path from you to Santa: ", steps)
