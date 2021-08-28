def timescore(timelist,weightings):
    preweightedscorelist=[]
    weightedscorelist=[]
    for time in timelist:
        if time=="none":
            preweightedscorelist.append(0)  
        elif time>30:
            preweightedscorelist.append(0)
        elif time<10:
            preweightedscorelist.append(1)
        elif time<=30 and time>=10:
            preweightedscorelist.append(((10-time)/20)+1)
    for i in range(len(weightings)):
        weightedscorelist.append(weightings[i]*preweightedscorelist[i])
    return 100*(sum(weightedscorelist)/sum(weightings))
