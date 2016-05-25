# 6.00.2x Problem Set 4

import numpy
import random
import matplotlib.pylab as pylab
import matplotlib.pyplot as pyplot
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb = 100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005

    def runSim(beforeSteps = 150, afterSteps = 150, numTrials = 100):
        popTotal  = []
        popResist = []

        for n in xrange(numTrials):
            viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for j in xrange(numViruses) ]
            patient = TreatedPatient(viruses, maxPop)

            # Before prescription
            for i in xrange(beforeSteps):
                patient.update()

            # Prescribe
            patient.addPrescription('guttagonol')

            # After prescription
            for i in xrange(beforeSteps, beforeSteps + afterSteps):
                patient.update()

            popTotal.append(patient.getTotalPop())
            popResist.append(patient.getResistPop(['guttagonol']))

        return (popTotal, popResist)

    beforeSteps = [ 300, 150, 75,  0  ]
    afterSteps  = [ 150, 150, 150, 150]

    f, parr = pyplot.subplots(len(beforeSteps))

    for i in xrange(len(beforeSteps)):
        popTotal, popResist = runSim(beforeSteps[i], afterSteps[i], numTrials)

        parr[i].hist(popTotal, bins = 9)

        pyplot.xlabel('Tot. virus pop. (beforeSteps = ' + str(beforeSteps[i]) + ')')
        pyplot.ylabel('# of trials')

    pyplot.show()

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb = 100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005

    beforeFirstSteps = 150
    afterSteps       = 150

    def runSim(beforeSecondSteps = 150, numTrials = 100):
        popTotal  = []

        for n in xrange(numTrials):
            viruses = [ ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for j in xrange(numViruses) ]
            patient = TreatedPatient(viruses, maxPop)

            # Before fisrst prescription
            for i in xrange(beforeFirstSteps):
                patient.update()

            # Prescribe first
            patient.addPrescription('guttagonol')

            # Before second prescription
            for i in xrange(beforeSecondSteps):
                patient.update()

            # Prescribe second
            patient.addPrescription('grimpex')

            # After prescription
            for i in xrange(afterSteps):
                patient.update()

            popTotal.append(patient.getTotalPop())
            print '.',

        return popTotal

    beforeSecondSteps = [ 300, 150, 75,  0  ]


    pyplot.title('ResistantVirus simulation with 2 drugs')

    for i in xrange(len(beforeSecondSteps)):
        print "\n\t Running for " + str(beforeSecondSteps[i])

        popTotal = runSim(beforeSecondSteps[i], numTrials)

        pyplot.subplot(len(beforeSecondSteps), 1, i + 1)

        pyplot.hist(popTotal)

        pyplot.xlabel('TVP (' + str(beforeSecondSteps[i]) + ')')

    pyplot.ylabel('# of trials')
    pyplot.show()
