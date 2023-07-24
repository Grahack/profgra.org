# votre code

d = NombreDecimal(20)
assert d.bin() == "10100"
assert d.hex() == "14"
b = NombreBinaire("10100")
assert b.dec() == 20
assert b.hex() == "14"
h = NombreHexadécimal("14")
assert h.bin() == "10100"
assert h.dec() == 20
