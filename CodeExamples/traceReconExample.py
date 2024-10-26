import numpy as np


# NOTE: This script will create two files when run: 
#       - "originalSequence.txt" which will have the original sequence 
#         the traces are taken from (only look at this if you want to check your answer)
#       - "traces.txt" which will have a bunch of traces generated from the original
#         sequence, with each line being a new trace

#################################################################################################################
##
## User parameters 
##

## To Julia: You can change these parameters to get different length sequences
#                    or to get more traces, or other stuff

sequenceLength = 10     # Length of the sequence (the thing to be recovered)
numTraces = 3           # Number of traces to generate
probDeletion = 0.2      # Probability of deleting any element of the sequence for a trace

alphabet = ["A", "B", "C"]       
                        # The alphabet to pull from for sequence generation
                        # For example, this could be ["A", "B", "C"], and the generated
                        # sequence would be a string of "A"s, "B"s, and "C"s selected randomly

rngSeed = 10            # The seed value of the random number generator. We use this to make the output of this
                        # script reproducible, in case there is a particular sequence of interest
                        # Set to -1 if you want non-reproducible numbers, otherwise set it to
                        # your favorite natural number


#################################################################################################################

#########################
### Start of Script stuff
#########################

if(rngSeed >= 0):
    simRng = np.random.default_rng(seed=rngSeed)
else:
    simRng = np.random.default_rng()


# Creating the original sequence, and saving it to "originalSequence.txt"
origSequence = simRng.choice(alphabet, size=(sequenceLength,), replace=True)
np.savetxt("./originalSequence.txt", origSequence, delimiter=",", fmt="%s", newline=",")

# Creating an array of elements which says whether to 
# keep or throw out the respective index in the respective
# trace (0 represents it should be deleted, 1 says it should stay)
traceIndexes = simRng.choice([0,1], size=(sequenceLength, numTraces), replace=True, p=[probDeletion, 1 - probDeletion])


# For each trace, we generate the trace and then save it to the file in order

# Opening the targeted file to be read into
with open("./traces.txt", "w") as wfile:
    wfile.write("Traces start below this line \n")

    for targInd in range(numTraces):
        targTraceIndxs = traceIndexes[:, targInd]

        indsToKeep = np.where(targTraceIndxs == 1)[0]

        targTrace = origSequence[indsToKeep]

        # Crudely converting the array into a string, because its 9 pm and I want to go home
        traceStr = ''
        for targChar in targTrace:
            traceStr += targChar + ","

        wfile.write(traceStr + "\n")

        print("This is here")

print(origSequence)


