def age_category(age):
    if age < 0:
        return "არასწორი ასაკი"
    elif age < 13:
        return "თქვენ ხართ ბავშვი."
    elif age < 20:
        return "თქვენ ხართ ახალგაზრდული ასაკის."
    elif age < 65:
        return "თქვენ ხართ ზრდასრული."
    else:
        return "თქვენ ხართ მოხუცი."
    
age_category(input(""))