def base_26(num):
    '''return how many letter the base26 would have for a base 10 number'''
    counter = 0
    while num>26 :
        num= num/26
        counter +=1
    if num >=1:
        counter +=1
        
    return counter

def letter_number(num_letter,pop):
    '''take in the number of letter in base 26 and population return number and letter'''
    tem_pop=0
    num_num=0

    while num_letter >0:
        #make temp pop to caucluate if further deduction of letter needed
        compare_pop = pow(10,num_num+1)*pow(26,num_letter-1)

        if pop<=compare_pop:
            num_letter -=1
            num_num += 1
  
        else:
            break
        
            
    return(num_letter,num_num)
            
            
def car_plate(pop):
    '''return pattern of letter, number, total plate and excess plate'''
    letter = base_26(pop)
    (let,num) = letter_number(letter,pop)
    total = pow(10,num)*pow(26,let) # combine of letter and numbers
    excess = abs(pop-total)
    return(let, num,total,excess)

    
    