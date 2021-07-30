def solution(new_id):
    # step 1
    new_id = new_id.lower()
    
    # step 2 
    invalid = '~!@#$%^&*()=+[{]}:?,<>/'
    
    for term in invalid:
        new_id = new_id.replace(term, '')

    
    # step 3
    new = ''
    for idx, val in enumerate(new_id.split('.')):
        if val != '':
            new += ('.' + val)
    
    # step 4
    new_id = new.strip('.')
    
    # step 5
    if new_id == '':
        new_id = 'a'
        
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    
    # step 7
    if len(new_id) <= 2:
        while(len(new_id) < 3):
            new_id += new_id[-1]
    
    return new_id
