# GUSTAVO SANCHEZ PSID: 1861118
def get_age(): #define age function
    age = int(input()) #input age
    if (age > 18 and age <=75): #condition to check for age 18-75
        return age
    else:
        raise ValueError("Invalid age.")

def fat_burning_heart_rate(age): #find heart rate
    heart_rate = ((70/100)*(220 - age))
    return heart_rate

if __name__=="__main__": #main code
    try:
        age = get_age()
        print("Fat burning heart rate for a", age , "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as error:
        print(error.args[0])
        print("Could not calculate heart rate info.\n")
