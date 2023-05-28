def suggestions(a,g,h):
    if(a=="Below40" and g=="Male" and h=="No"):
        return "According to specified details your calorie intake per day should be around 2800 Calories"
    elif(a=="Above40" and g=="Male" and h=="No"):
        return "According to specified details your calorie intake per day should be around 2200 Calories"
    elif(a=="Above40" and g=="Female" and h=="No"):
        return "According to specified details your calorie intake per day should be around 1600 Calories"
    elif(a=="Below40" and g=="Female" and h=="No"):
        return "According to specified details your calorie intake per day should be around 2000 Calories"
    else:
        if(h=="Diabetes"):
            return "According to specified details your calorie intake per day should be around 1500 to 1800 calories"
        elif(h=="BP"):
            return "According to specified details your calorie intake per day should be around 1500 calories"
        elif(h=="Obesity"):
            return "According to specified details your calorie intake per day should be around 1000 to 1600 calories"
        elif(h=="Thyroid"):
            return "According to specified details your calorie intake per day should be around 2000 calories"
        elif(h=="Heart_diseases"):
            return "According to specified details your calorie intake per day should be around 1800 calories"