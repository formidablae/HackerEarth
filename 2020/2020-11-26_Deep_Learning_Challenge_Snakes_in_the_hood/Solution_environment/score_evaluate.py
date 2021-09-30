# Supposed to be score = 100 * f1_score(actual_values, predicted_values, average = 'weighted')
from pandas import DataFrame


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


def score(predicted_values_file, actual_values_file):
    # Read values from files and put them into dictionaries
    dict_predicted_values = get_dict_values_from_file(predicted_values_file)
    dict_actual_values = get_dict_values_from_file(actual_values_file)

    # Check how many values were predicted correctly
    correctly_found = 0
    i = 0
    for image_id_key in dict_predicted_values.keys():
        if dict_predicted_values[image_id_key] == dict_actual_values[image_id_key]:
            correctly_found += 1
            print("{}/{}. image_id: {}. Found: {}".format(i + 1,
                                                          len(dict_actual_values),
                                                          image_id_key,
                                                          correctly_found))
        i += 1

    return correctly_found


score_obtained = score('dataset/example_result.csv', 'dataset/train.csv')
print("Total correct predictions: {}".format(score_obtained))
