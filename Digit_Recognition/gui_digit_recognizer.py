# make a prediction for a new image.
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile


# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, grayscale=True, target_size=(28, 28))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 1 channel
	img = img.reshape(1, 28, 28, 1)
	# prepare pixel data
	img = img.astype('float32')
	img = img / 255.0
	return img

root = Tk()
root.geometry('400x200')

def open_file():
	frame = Frame(root)
	frame.pack()
	file = askopenfile(filetypes =[('Image Files', '')])
	img = load_image(file.name)
	
	# load model
	model = load_model('final_model.h5')
	# predict the class
	digit = model.predict_classes(img)
  
	w = Label(frame, text = 'Prediction \n', font = "50") 
	w.pack()
	w1 = Label(frame, text = str(digit[0]), font = "50") 
	w1.pack()
	btn1 = Button(frame, text ='Try Again', command = lambda:frame.destroy(), width = 50)
	btn1.pack(pady = 10)


btn = Button(root, text ='Open', command = lambda:open_file(), width = 50)
btn.pack(side = TOP, pady = 10)

mainloop()
