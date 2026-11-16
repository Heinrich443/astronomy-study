from astropy.constants import G
from astropy import constants as const
from astropy import units as u
# version modules
from astropy.constants import codata2014 as cd
from astropy.constants import iau2012 as iau
from astropy.constants import astropyconst20 as ac

print(G)
print(const.G)

# 物理场景：计算一个 3 倍太阳质量的天体与一个 100 kg 物体相距 2.2 AU 时的引力。
F = (const.G * 3 * const.M_sun * 100 * u.kg) / (2.2 * u.au) ** 2
print(F.to(u.N))

# unit conversion
print(const.c)
print(const.c.to('km/s'))
print(const.c.to('pc/yr'))
print(const.c.cgs)

# specify a system
print(100 * const.e)
print(100 * const.e.si)
print(100 * const.e.esu)
print(100 * const.e.emu)
print(100 * const.e.gauss)

# version modules
print(cd.e)
print(iau.L_sun)
print(ac.e)