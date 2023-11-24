orbits(mercury, sun).
orbits(venus, sun).
orbits(earth, sun).
orbits(mars, sun).
orbits(moon, earth).
orbits(phobos, mars).
orbits(deimos, mars).
planet(P):-orbit(p,sun).
satellite(s):-orbits(s,p),planet(p).
