# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
# Enter your definitions for the SimpleVirus and Patient classes in this box.
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO
        self.maxBirthProb=maxBirthProb
        self.clearProb=clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        # TODO
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        # TODO
        return self.clearProb 
         
    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        # TODO
        return random.random()<self.getClearProb()
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO
        
        if random.random()<=self.maxBirthProb * (1 - popDensity):    
                    return SimpleVirus(self.maxBirthProb,self.clearProb)
        else:
             raise NoChildException()                   



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        # TODO
        self.viruses=viruses
        self.maxPop=maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        # TODO
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        # TODO
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO
        return len(self.viruses)        


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        offtemp=[]
        temp=[]
        for i in self.viruses:
            if not i.doesClear():
                temp.append(i)
        popdensity=float(len(temp))/float(self.maxPop)
        for j in temp:
                  offtemp.append(j)  
                  try:
                     i.reproduce(popdensity)
                     offtemp.append(i.reproduce(popdensity))
                  except NoChildException:
                     continue
        self.viruses=offtemp     
        return self.viruses



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
   
 
    finalResults = None
 
    for i in xrange(0, numTrials):
        #print "running trial", i
        results = runSimulation(numViruses, maxPop, maxBirthProb, clearProb)
        if finalResults == None:
            finalResults = results
        else:
            for j in xrange(0, len(results)):
                finalResults[j] += results[j]
 
    for i in xrange(0, len(finalResults)):
        finalResults[i] /= numTrials
   
    pylab.plot(finalResults, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend(loc = "best")
    pylab.show()
 
 
 
 
def runSimulation (numViruses, maxPop, maxBirthProb, clearProb):
    """ helper function for doing one simulation run """
    viruses = []
   
    for i in xrange(0, numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
 
    patient = Patient(viruses, maxPop)
 
    numSteps = 300
    numVirusesEachStep = []
    for i in xrange(0, numSteps):
        numVirusesEachStep.append(patient.update())
 
    return numVirusesEachStep   
         


#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        # TODO
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances=resistances
        self.mutProb=mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        # TODO
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """ 
        
        if drug in self.resistances:
          return self.resistances[drug]
        else:
          return False

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
 
        prob = random.random()
        if prob < self.maxBirthProb * (1 - popDensity):
 
            childResistances = {}
            for drug in self.resistances.keys():
                resistanceProb = random.random()
                if resistanceProb < self.mutProb:
                    childResistances[drug] = not self.resistances[drug]
                else:
                    childResistances[drug] = self.resistances[drug]
                   
            child = ResistantVirus(self.maxBirthProb, self.clearProb, childResistances,
                                   self.mutProb)
            return child
        else:
            raise NoChildException()        
            
                                                                  
class TreatedPatient(Patient):
   
 
    def __init__(self, viruses, maxPop):
       
 
        Patient.__init__(self, viruses, maxPop)
        self.activeDrugs = []
 
 
    def addPrescription(self, newDrug):
       
 
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)
 
 
    def getPrescriptions(self):
       
 
        return self.activeDrugs
 
 
    def getResistPop(self, drugResist):
       
 
        vp=0
        for v in self.viruses:
            i=0
            for d in drugResist:
                if v.isResistantTo(d):
                    i+=1
            if i==len(drugResist):
                vp+=1       
        return vp

 
 
    def update(self):
       
 
        survivedViruses = []
        for virus in self.viruses:
          try:
            if not virus.doesClear():
                survivedViruses.append(virus)
          except AttributeError:
                pass
        self.viruses = survivedViruses
        popDensity = float(len(survivedViruses)) / self.maxPop
        
 
        childViruses = []
 
        for virus in self.viruses:
            childViruses.append(virus)
            try:
                child = virus.reproduce(popDensity, self.activeDrugs)
                childViruses.append(child)
            except NoChildException:
                pass
 
        self.viruses = childViruses
        return self.getTotalPop()
            


#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    # TODO
    def eachTrial(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, timestep, addrug):
        viruses=[]
        for i in range(numViruses):
              v=ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
              viruses.append(v)
        patient=TreatedPatient(viruses,maxPop)
        tlen=[]
        rlen=[]
        for i in range(timestep):
            if i==150:
                patient.addPrescription('guttagonol')
            if i==450:
                patient.addPrescription('grimpex') 
            tlen.append(patient.update())
            rlen.append(patient.getResistPop(['guttagonol']))
        
        return (tlen, rlen)
    avtot=[]
    avresist=[]
    histtot=[]
    histresist=[]
    for i in range(numTrials):
        tot,resist=eachTrial(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, timestep=600, addrug='guttagonol')
        if  i==0:
            avtot=tot
            avresist=resist
        else:
            for i in range(len(tot)):
                avtot[i]=avtot[i]+tot[i]
            for i in range(len(resist)):
                avresist[i]=avresist[i]+resist[i]
        histtot.append(tot[-1])
        histresist.append(resist[-1])               
    for i in range(len(avtot)):
        avtot[i]=avtot[i]/float(numTrials) 
    for i in range(len(avresist)):
        avresist[i]=avresist[i]/float(numTrials)
    '''pylab.plot(avtot, label = "totResistantVirus")
    pylab.plot(avresist, label = "ResistantVirus")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend(loc = "best")
    pylab.figure('2')'''
    pylab.hist(histtot,bins=5)
    pylab.show()
simulationWithDrug(100, 1000, 0.1, 0.05,{'guttagonol': False, 'grimpex': False},0.005, 100)
