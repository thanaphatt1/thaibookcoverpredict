import keras
import numpy as np
from keras.preprocessing.image import img_to_array
from PIL import Image
model = keras.models.load_model('model')
classes = ['การ์ตูน',
 'คอมพิวเตอร์',
 'งานอดิเรก งานฝีมือ',
 'จิตวิทยา การพัฒนาตัวเอง',
 'ธรรมะ ศาสนา และปรัชญา',
 'นิยาย',
 'นิยายแปล',
 'บริหาร ธุรกิจ',
 'วรรณกรรม',
 'สุขภาพ ความงาม',
 'หนังสือท่องเที่ยว',
 'หนังสือบทความ สารคดี',
 'หนังสือเด็ก',
 'หนังสือเตรียมสอบ แนวข้อสอบ']

def image_predict(url):
    img = Image.open(url)
    testimg = img.resize((128,128))
    testimg = np.array(testimg)
    testimg = np.expand_dims(testimg, axis=0)
    prob = model.predict(testimg)
    predict = np.argmax(prob)
    result = classes[predict]
    return result