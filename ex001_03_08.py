def printNumber():

    print("Insira um número entre 0 e 100")   
    validNumber = True    
    while validNumber == True:     
        try:       
            number = int(input())      
            if number > 0 and number <= 100:         
                print("O número que você escolheu foi: " + str(number))         
                   
            if number %2 == 0 and number %3 == 0:        
                print(f'O número {number} é divisível por 2 e 3')
                break       
            else:         
                print("Por favor digite um número maior que 0 e menor que 100")     
        
        
        except Exception as error:       
            print(error)  
            
        
printNumber()