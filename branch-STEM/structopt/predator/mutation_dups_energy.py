from MAST.structopt.tools import get_best
from MAST.structopt.switches import selection_switch, moves_switch, lambdacommamu
from MAST.structopt.tools import remove_duplicates
from MAST.structopt.fingerprinting import get_fingerprint
import random

def mutation_dups_energy(pop, Optimizer):
    """Predator function that removes duplicates based on energy and replaces with mutations
    """
    fitlist = [one.energy for one in pop]
    nfitlist, nindices = remove_duplicates(fitlist, Optimizer.demin)
    STR = ''
    newpop = []
    if len(nfitlist) != len(fitlist):
        STR+='Predator: Removed total of '+repr(len(fitlist)-len(nfitlist))+' from population\n'
    otherlist = []
    for i in range(len(pop)):
        if i not in nindices:
            STR+='Predator: Removed '+repr(pop[i].history_index)+'\n'
            otherlist.append(pop[i])
        else:
            newpop.append(pop[i])
    while len(newpop) < Optimizer.nindiv:
        indiv = random.choice(otherlist).duplicate()
        indiv, scheme = moves_switch(indiv,Optimizer)
        indiv.energy = 1000
        indiv.fitness = 1000
        newpop.append(indiv)
        STR+='Predator: Adding mutated duplicates to new pop history='+indiv.history_index+'\n'
        nindices.append(indiv.index)
    nindices.sort()
    if Optimizer.natural_selection_scheme=='fussf':
        for ind in newpop:
            if ind.fingerprint == 0:
                ind.fingerprint = get_fingerprint(Optimizer,ind,Optimizer.fpbin,Optimizer.fpcutoff)
    if 'lambda,mu' in Optimizer.algorithm_type:
        try:
            mark = [ index for index,n in enumerate(nindices) if n > Optimizer.nindiv-1][0]
        except:
            mark = Optimizer.nindiv
        Optimizer.mark = mark
        pop, str1 = lambdacommamu.lambdacommamu(newpop, Optimizer)
        STR+=str1
    else:
        pop = selection_switch(newpop, Optimizer.nindiv, Optimizer.natural_selection_scheme, Optimizer)
    pop = get_best(pop,len(pop))
    return pop, STR
