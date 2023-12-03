def check_pass(pas):
    f=0
    if pas.isdigit() or pas.islower() or pas.isupper() or len(pas)<8:
        print('no')
    else:
        for item in '!@#$%^&*()_+?><":!"№;:?*-':
            if item in pas:
                f=1
        if f==1:
            print('yes')
        else:
            print('no')
        
    
    
check_pass('Qwerty2283110')
