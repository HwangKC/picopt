import extern


PROGRAMS = ['optipng', 'pngout', 'advpng']
FORMATS = set(['PNG'])
LOSSLESS_FORMATS = set(('PNM', 'PPM', 'TIFF', 'BMP', 'GIF'))
CONVERTABLE_FORMATS = LOSSLESS_FORMATS | FORMATS

OPTIPNG_ARGS = ['optipng', '-o6', '-fix', '-preserve', '-force', '-quiet']
ADVPNG_ARGS = ['advpng', '-z', '-4', '-f']
PNGOUT_ARGS = ['pngout', '-q', '-force', '-y']


def pngout(ext_args):
    """runs the EXTERNAL program pngout on the file"""
    args = PNGOUT_ARGS + [ext_args.old_filename, ext_args.new_filename]
    extern.run_ext(args)


def optipng(ext_args):
    """runs the EXTERNAL program optipng on the file"""
    args = OPTIPNG_ARGS + [ext_args.new_filename]
    extern.run_ext(args)


def advpng(ext_args):
    """runs the EXTERNAL program advpng on the file"""
    args = ADVPNG_ARGS + [ext_args.new_filename]
    extern.run_ext(args)


PROG_MAP = (optipng, advpng, pngout)


def optimize(filename, arguments):
    """run EXTERNAL programs to optimize lossless formats to PNGs"""
    return extern.optimize_with_progs(PROG_MAP, filename, 'PNG', False,
                                      arguments)
