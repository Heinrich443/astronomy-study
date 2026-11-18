from astropy import units as u

t = u.Quantity(15, u.m / u.s)
print(t)
qlst = [120 * u.s, 1 * u.min]
t = u.Quantity(qlst, u.minute)
print(t)
t = u.Quantity("15 m/s")
print(t)

q = 2.4 * u.m / u.s
print(q.si)
print(q.cgs)

q = 2.5 * u.m
print(q)
t = q.to_value(u.cm)
print(t)
print(q)
