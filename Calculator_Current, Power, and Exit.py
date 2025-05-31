'''
Create calculator program to analyze an electrical circuit:
Requirements:
•	Menu with the choices: 1) Ohm's Law, 2) Power Calculation, 3) Exit
•	Function ohms_law(v, r) to calculate current
•	Function power_calc(v, i) to calculate power
•	Input validation with try/except
•	Loop until user choose exit
•	Format the result with 2 decimals
Bonus: Save the calculation result in a list for history

Covers functions, loops, conditionals, string formatting, error handling
'''



print("1. Ohm's Law \n2. Power Calculation \n3. Exit"
    )
def user_choice(min = 1, max = 3):
    while True:
        try:
            user_input = int(input('Please select a menu: '))
            if min <= user_input <= max:
                return user_input
            else:
               print('Use number 1 - 3') 
        except ValueError:
            print('Please insert number 1, 2, or 3')

def input_angka(angka):
    while True:
        try:
            return float(input(angka))
        except ValueError:
            print('Masukkan angka dengan benar')
    
def Ohms_Law_arus(v, r):
    arus = v / r
    return arus
    
def rumus_daya(v, i):
    daya = v * i
    return daya
            

data_arus = []
data_daya = []

while True:
    print("1. Ohm's Law \n2. Power Calculation \n3. Exit")
    choice = user_choice()
    if choice == 1: #Menghitung nilai arus
        v = input_angka("Masukkan nilai tegangan: ")
        r = input_angka("Masukkan nilai resistansi: ")
            
        nilai_arus = Ohms_Law_arus(v,r)
        formatted_nilai_arus = f"{nilai_arus:.2f}"
        print(f"Nilai arus: {formatted_nilai_arus} A")
        data_arus.append(formatted_nilai_arus)
    
    elif choice == 2:   #menghitung nilai daya
        v = input_angka("Masukkan nilai tegangan: ")
        i = input_angka("Masukkan nilai arus: ")
        
        rumus_daya(v, i)
        nilai_daya = rumus_daya(v, i)
        formatted_nilai_daya = f"{nilai_daya:.2f}"
        print(f"Nilai daya: {formatted_nilai_daya} W")
        data_daya.append(formatted_nilai_daya)

    else:   #exit
        break
    
print(f"Data perhitungan arus: {data_arus}")
print(f"Data perhitungan daya: {data_daya}")

    