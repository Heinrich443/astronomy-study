from timeit import Timer
from astropy import units as u

# Quantity
print(100.0 * u.meter)
q = 200.0 * u.kilometer
print(q.value)
print(q.unit)

# value conversion
t = 3.0 * u.kilometer / (130.51 * u.meter / u.second)
print(t)
print(t.to(u.s))

# dimensionless unit
dl = u.m / u.m
print(dl)
dl = 1.0 * u.dimensionless_unscaled
print(dl)

# compound units
q = (u.s ** -1).compose()
print(q)

# unit systems conversion
q = (1.0 * u.Pa).cgs
print(q)

# conversion between wavelength and frequency
# wrong way
f = (1000 * u.nm).to(u.Hz)
print(f)
# right way
f = (1000 * u.nm).to(u.Hz, equivalencies=u.spectral())
print(f)

# format string
q = 15.1 * u.meter / (32.0 * u.second)
print(f'{q:.3f}')
print(f'{q.value:.3f} {q.unit:FITS}')

# performance tips
# before optimization
timer = Timer(
    "array * u.m / u.s / u.kg / u.sr",
    setup="import numpy as np; import astropy.units as u; array = np.arange(1000.0)",
)
best = min(timer.repeat(repeat=5, number=10000)) / 10000
print(f"before optimization: {best*1e6:.3f} µs/次")

# optimization 1
timer = Timer(
    "array * (u.m / u.s / u.kg / u.sr)",
    setup="import numpy as np; import astropy.units as u; array = np.arange(1000.0)",
)
best = min(timer.repeat(repeat=5, number=10000)) / 10000
print(f"optimization 1: {best*1e6:.3f} µs/次")

# optimization 2
timer = Timer(
    "array * UNIT",
    setup="import numpy as np; import astropy.units as u; array = np.arange(1000.0); UNIT = u.Unit('m s-1 kg-1 sr-1')",
)
best = min(timer.repeat(repeat=5, number=10000)) / 10000
print(f"optimization 2: {best*1e6:.3f} µs/次")

# optimization 3
timer = Timer(
    "array << UNIT",
    setup="import numpy as np; import astropy.units as u; array = np.arange(1000.0); UNIT = u.Unit('m s-1 kg-1 sr-1')",
)
best = min(timer.repeat(repeat=5, number=10000)) / 10000
print(f"optimization 3: {best*1e6:.3f} µs/次")
