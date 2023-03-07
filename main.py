with open("input.txt", "r") as f:
    score = f.read()
    score_ints = [ int(x) for x in score.split() ] 
    print(sum(score_ints))