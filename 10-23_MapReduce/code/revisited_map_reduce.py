def compute_mean(dd):
    '''
    Compute the mean of listen counts for each user
    '''
    user = dd.get('User_id')

    total = 0
    len = 0
    for k, v in dd.items():
        if k != 'User_id':
            total += v
            len += 1 if v > 0 else 0
    return (user, total/len)
