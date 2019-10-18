def vote_percentage(l: list):
    yes = 0
    no = 0
    for i in l:
        if i == 'yes':
            yes += 1
        elif i == 'no':
            no += 1

    if no == 0:
        return 'unanimous'
    elif yes > (yes + no) / 3 * 2:
        return 'clear majority'
    elif yes > (yes + no) / 2:
        return 'simple majority'
    else:
        return 'the motion failed   '


l = [str(i) for i in input(
    """Input the votes(yes, no, or abstention) separated by spaces, then push enter: """
).split(' ')]
print(vote_percentage(l))
