## _lights [(label, wavelength, dsp line, sim diffraction angle at slm),...]
<<<<<<< HEAD
ipAddress = '172.16.0.21'
light_keys = ['label','wavelength', 'color', 'line','simtheta','port','device']
=======
ipAddress = 'dsp.b24'
light_keys = ['label','wavelength', 'color', 'triggerLine','simtheta','port','device']
>>>>>>> 805c872... Changed line to triggerLine in configs and dsp.
WAVELENGTH_TO_COLOR = {
    405: (180, 30, 230),
    488: (40, 130, 180),
    561: (176, 255, 0),
    640: (255, 40, 40),
    'white': (255, 255, 255)
}

lights = [
    ('ambient', 'Ambient', WAVELENGTH_TO_COLOR['white'], 0),
#    ('405nm', 405, WAVELENGTH_TO_COLOR[405], 1<<13, 10),
#    ('488nm', 488, WAVELENGTH_TO_COLOR[488], 1<<9, 9, 7776, 'deepstar'),
#    ('561nm', 561, WAVELENGTH_TO_COLOR[561], 1<<13, 8),
    ('DIC', 'DIC', WAVELENGTH_TO_COLOR['white'], 1<<11),]
