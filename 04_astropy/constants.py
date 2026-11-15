from astropy.constants import G
from astropy import constants as const
from astropy import units as u

print(G)
print(const.G)

# 物理场景：计算一个 3 倍太阳质量的天体与一个 100 kg 物体相距 2.2 AU 时的引力。
F = (const.G * 3 * const.M_sun * 100 * u.kg) / (2.2 * u.au) ** 2
print(F.to(u.N))