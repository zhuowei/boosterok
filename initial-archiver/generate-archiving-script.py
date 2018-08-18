import os
# mastodon switched to Snowflake between October 4 (when pr merged) and somewhere in November.
endId = 98982300140635839
# https://mastodon.social/@esdin/98982300140635839 - what I got when I googled "Nov 10 Mastodon.social"
startId = 100571995785293420

# we did 458 fetches in 24 min, or 95/min
# so we can support ~78 workers
numWorkers = 32

incrementPerWorker = (startId - endId) // numWorkers

def printOne(maxid, endid):
    dirn = "archive/archive_{}_{}".format(maxid, endid)
    os.mkdir(dirn)
    with open(dirn + "/run.sh", "w") as outfile:
        print("exec python3 ../../initial-archiver.py", maxid, endid, file=outfile)

for i in range(numWorkers):
    maxid = endId + (i+1) * incrementPerWorker
    if i == numWorkers - 1:
        maxid = startId
    printOne(maxid, endId + (i)*incrementPerWorker)
