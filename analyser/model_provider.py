from keras.models import model_from_json

models_dir = './analyser/models/'
optimizer = 'adam'

def get_model(model_name):
    model_filename = models_dir + model_name + '/' + model_name + '.json'
    weights_filename = models_dir + model_name + '/' + model_name + '.h5'

    with open(model_filename, "r") as json_file:
        loaded_model_json = json_file.read()

    model = model_from_json(loaded_model_json)
    model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    model.load_weights(weights_filename)

    return model
