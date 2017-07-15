def is_rotation(s1,s2):
    rotations = []
    if s1 == None:
        if s2 == None:
            return True
        else:
            return False

    elif s1 == '':
        if s2 == '':
            return True
        else:
            return False
    else:

        for i in range(0,len(s1)):
            temp = s1[i:] + s1[:i]
            rotations.append(str(temp))
        if s2 in rotations:
            return True
        else:
            return False
