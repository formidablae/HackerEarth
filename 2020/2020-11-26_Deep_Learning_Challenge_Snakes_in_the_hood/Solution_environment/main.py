# Identify the snake breed

"""
Detect the breed of a snake from its image.

Data description
This data set consists of the following two columns:
---------------------------------------------------
| Column Name | Description                       |
|-------------|-----------------------------------|
| image_id    | Name of the image file            |
|-------------|-----------------------------------|
| breed	      | Snake breed [35 different breeds] |
---------------------------------------------------

The data folder consists of two folders and two .csv files.
The details are as follows:

train: Contains 5508 images for 35 classes
test: Contains 2361 images
train.csv: 5508 x 2
test.csv: 2361 x 1


Submission format
You are required to write your predictions in a .csv file
and upload it by clicking the Upload File button.

Sample submission

image_id,breed
a8b3ad1dde,nerodia-erythrogaster
8b492b973d,pantherophis-vulpinus
929b99ea92,thamnophis-sirtalis
bbac7385e2,pantherophis-obsoletus
ef776b1488,agkistrodon-contortrix


Evaluation metric
score = 100 * f1_score(actual_values, predicted_values, average = 'weighted')

Note: To avoid any discrepancies in the scoring, ensure that
all the index column (image_id) values in the submitted file
match the values in the provided test.csv file.
"""

import matplotlib.pyplot as plt
import numpy as np
import os  # used for navigating to image path

from PIL import Image  # used for loading images
from random import shuffle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import load_model
# from keras.preprocessing import image


DIR = './dataset/train_set'
TEST_DIR = './dataset/test'
MODEL_TEST_DIR = './dataset/test_set'
TRAIN_CSV = './dataset/output_training_full.txt'
MODEL_TEST_CSV = './dataset/output_testing_full.txt'
TEST_CSV = './dataset/test.csv'
IMG_SIZE = 128


def get_size_statistics():
    heights = []
    widths = []
    img_count = 0
    for img in os.listdir(DIR):
        path = os.path.join(DIR, img)
        if "DS_Store" not in path:
            data = np.array(Image.open(path))
            heights.append(data.shape[0])
            widths.append(data.shape[1])
            img_count += 1
    avg_height = sum(heights) / len(heights)
    avg_width = sum(widths) / len(widths)
    print("Average Height: " + str(avg_height))
    print("Max Height: " + str(max(heights)))
    print("Min Height: " + str(min(heights)))
    print('\n')
    print("Average Width: " + str(avg_width))
    print("Max Width: " + str(max(widths)))
    print("Min Width: " + str(min(widths)))


def get_dict_values_from_file(filename):
    values_file_handler = open(filename, 'r')
    values_file_handler.readline().strip()
    dict_values = {}
    while True:
        values_line = values_file_handler.readline()
        if not values_line:
            break
        values_line_info = \
            list(map(str, values_line.strip().split(',')))
        dict_values[values_line_info[0]] = values_line_info[1]
    values_file_handler.close()
    return dict_values


def get_input_images_filenames(filename):
    names_file_handler = open(filename, 'r')
    names_file_handler.readline().strip()
    names_list = []
    while True:
        values_line = names_file_handler.readline()
        if not values_line:
            break
        names_list.append(values_line.strip())
    names_file_handler.close()
    return names_list


def load_images():
    images_data = []
    rgb2xyz = (0.412453, 0.357580, 0.180423, 0,
               0.212671, 0.715160, 0.072169, 0,
               0.019334, 0.119193, 0.950227, 0)
    for img in os.listdir(TEST_DIR):
        label = img.split(".")[0]
        path = os.path.join(TEST_DIR, img)
        img = Image.open(path)
        img = img.convert("RGB", rgb2xyz)
        # img = img.convert('L')
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        img = np.expand_dims(img, axis=0)
        images_data.append([np.array(img), label])
    return images_data


def build_breed_arrays(dictnry_of_values):
    breeds = dictnry_of_values.values()
    breed_set_list = list(set(breeds))
    breeds_np_arrays = {}
    i = 0
    for breed_name in breed_set_list:
        array_to_build = [0] * len(breed_set_list)
        array_to_build[i] = 1
        breeds_np_arrays[breed_name] = np.array(array_to_build)
        i += 1
    return breeds_np_arrays


def obtain_breed_from_array(dictnry_of_values):
    breeds = dictnry_of_values.values()
    breed_set_list = list(set(breeds))
    breeds_np_arrays = {}
    i = 0
    for breed_name in breed_set_list:
        array_to_build = "0" * i + "1" + "0" * (len(breed_set_list) - i - 1)
        breeds_np_arrays[array_to_build] = breed_name
        i += 1
    return breeds_np_arrays


def label_img(dictionary_of_vals, breed_arrays, name):
    name_no_ext = name.split('.')[0]
    return breed_arrays[dictionary_of_vals[name_no_ext]]


def load_training_data(dict_of_vals):
    training_data = []
    rgb2xyz = (0.412453, 0.357580, 0.180423, 0,
               0.212671, 0.715160, 0.072169, 0,
               0.019334, 0.119193, 0.950227, 0)
    breed_arr = build_breed_arrays(dict_of_vals)
    for img in os.listdir(DIR):
        label = label_img(dict_of_vals, breed_arr, img)
        path = os.path.join(DIR, img)
        img = Image.open(path)
        img = img.convert("RGB", rgb2xyz)
        # img = img.convert('L')
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        training_data.append([np.array(img), label])

    shuffle(training_data)
    return training_data


def load_test_data(dict_of_vals):
    testing_data = []
    rgb2xyz = (0.412453, 0.357580, 0.180423, 0,
               0.212671, 0.715160, 0.072169, 0,
               0.019334, 0.119193, 0.950227, 0)
    breed_arr = build_breed_arrays(dict_of_vals)
    for img in os.listdir(MODEL_TEST_DIR):
        label = label_img(dict_of_vals, breed_arr, img)
        path = os.path.join(MODEL_TEST_DIR, img)
        img = Image.open(path)
        img = img.convert("RGB", rgb2xyz)
        # img = img.convert('L')
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        testing_data.append([np.array(img), label])
    shuffle(testing_data)
    return testing_data


dictionary_of_training_values = get_dict_values_from_file(TRAIN_CSV)
# dictionary_of_testing_values = get_dict_values_from_file(MODEL_TEST_CSV)
# # get_size_statistics()
# train_data = load_training_data(dictionary_of_training_values)
# test_data = load_test_data(dictionary_of_testing_values)
# # plt.imshow(train_data[43][0], cmap='gist_gray')
# # plt.show()
# # plt.imshow(test_data[10][0], cmap='gist_gray')
# # plt.show()
# trainImages = np.array([i[0] for i in train_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
# trainLabels = np.array([i[1] for i in train_data])
# testImages = np.array([i[0] for i in test_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
# testLabels = np.array([i[1] for i in test_data])
#
# model = Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(BatchNormalization())
# model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(BatchNormalization())
# model.add(Conv2D(96, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(BatchNormalization())
# model.add(Conv2D(96, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(BatchNormalization())
# model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(BatchNormalization())
# model.add(Dropout(0.2))
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(128, activation='relu'))
# # model.add(Dropout(0.3))
# model.add(Dense(35, activation='softmax'))
# model.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'])
# model.fit(trainImages, trainLabels, batch_size=50, epochs=5, verbose=1)
# loss, acc = model.evaluate(testImages, testLabels, verbose=1)
# print(acc * 100)
# model.save("breed_model.h5")
breed_model = load_model("breed_model.h5", compile=False)
breed_model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

input_images_data = load_images()
results = "image_id,breed\n"
test_file_ids = get_input_images_filenames(TEST_CSV)
id_breed_dict = {}
for [img_arr, id_of_image] in input_images_data:
    prediction = breed_model.predict(img_arr)
    maximum_index = np.argmax(prediction[0])
    prediction = "0" * maximum_index + "1" + "0" * (len(prediction[0]) - maximum_index - 1)
    breed = obtain_breed_from_array(dictionary_of_training_values)[prediction]
    id_breed_dict[id_of_image] = breed
    # if id_of_image not in test_file_ids:
    #     print("not in. id: {}, predi: {}".format(id_of_image, breed))
    #     break
for i in range(len(test_file_ids)):
    id_value = test_file_ids[i]
    breed = id_breed_dict[test_file_ids[i]]
    results = results + str(id_value) + "," + str(breed) + "\n"
f = open("results.csv", "w")
f.write(results)
f.close()
