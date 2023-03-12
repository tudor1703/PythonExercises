with open('input.txt', 'r') as f:
    score = f.read()
    print(score.split())
    score_ints = [int(x) for x in score.split()] 
    the_sum = (sum(score_ints))
with open('output.txt', 'w') as infile:
    infile.write(str(the_sum))
        