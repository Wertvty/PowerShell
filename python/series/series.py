def slices(series, length):
    sl = []
    if length <= 0 or length > len(series) or series == []:
        raise ValueError("Invalid Series Or Length Value")
    else:
        for x in range(len(series)):
            if len(series[x:length+x]) == length: 
                sl.append(series[x:length+x])
            else:
                continue
    return sl
        
