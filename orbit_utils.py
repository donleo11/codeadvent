from orbit import Orbit


def count_orbits(orbits):
    count1 = 0
    count2 = 0
    for orbit in orbits:
        count_tmp = count_direct_orbits(orbit, orbits)
        print("Orbiter ", orbit.orbiter, " has ", count_tmp, " direct orbits")
        count1 = count1 + count_tmp
        count_tmp = count_indirect_orbits(orbit, orbits)
        print("Orbiter ", orbit.orbiter, " has ", count_tmp, " indirect orbits")
        count2 = count2 + count_tmp
    return count1 + count2


def count_direct_orbits(orbit: Orbit, orbits):
    return len(find_direct_orbit(orbit.orbiter, orbits))


def count_indirect_orbits(orbit: Orbit, orbits):
    count = 0
    indirect_object_list = find_indirect_orbit(orbit.orbitee, orbits)
    count = count + len(indirect_object_list)
    for orbit in indirect_object_list:
        count = count + count_indirect_orbits(orbit, orbits)
    return count


def find_indirect_orbit(orbitee: str, orbits):
    indirect_orbits_list = list()
    for orbit in orbits:
        if orbit.orbiter == orbitee:
            indirect_orbits_list.append(orbit)
    return indirect_orbits_list


def find_direct_orbit(orbiter: str, orbits):
    direct_orbits_list = list()
    for orbit in orbits:
        if orbit.orbiter == orbiter:
            direct_orbits_list.append(orbit)
    return direct_orbits_list
