from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf
import xlrd

model_best =tf.keras.models.load_model('model_trained_11class.hdf5',compile=False)

food_list =  ['french_fries', 'samosa', 'club_sandwich', 'chicken_curry', 'cup_cakes', 'chicken_wings', 'omelette', 'chocolate_cake', 'ice_cream', 'pizza', 'fried_rice']

def predict_class(model, images, show = True):
  for img in images:
    img = image.load_img(img, target_size=(299, 299))
    img = image.img_to_array(img)                    
    img = np.expand_dims(img, axis=0)         
    img /= 255.                                      

    pred = model.predict(img)
    index = np.argmax(pred)
    food_list.sort()
    pred_value = food_list[index]
    return pred_value


def predict(images):

    food=predict_class(model_best, images, True)

    loc = ("templates\\bootstrap-5.0.2-dist\\food.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    volume=160
    calorie=270
    for i in range(1,12):
        row=sheet.row_values(i)
        if(row[0]==food):
            volume=row[1]
            calorie=row[2]
    return [food,volume,calorie]

