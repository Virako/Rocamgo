import src.rocamgo
try:
    import cProfile as profiler
except:
    import profile as profiler
profiler.run('src.rocamgo.main()', '/home/virako/Rocamgo/rocamgoprof.txt')

