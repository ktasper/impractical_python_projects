import cProfile
import palingrams

#cProfile.run(palingrams.find_palingrams('./words.txt'))
cProfile.runctx('palingrams.find_palingrams("./words.txt")', globals(), locals())
