# Mask-RCNN Imports
from mrcnn.config import Config
from mrcnn.model import MaskRCNN

# Matplotlib Import
import matplotlib.pyplot as plt

class PredictionConfig(Config):
    # define the name of the configuration
    NAME = "damage"
    # number of classes (background + kangaroo)
    NUM_CLASSES = 1 + 4
    # number of training steps per epoch
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


cfg = PredictionConfig()
# define the model
model = MaskRCNN(mode='inference', model_dir='./', config=cfg)
# load model weights
model_path = './model/mask_rcnn_damage_0011-2.h5'
model.load_weights(model_path, by_name=True)
print('Model Loaded Successfully!!')
model.keras_model._make_predict_function()

def model_predict(img_path):
	# image = load_img(img_path)
	# image = img_to_array(image)
	image = plt.imread(img_path)
	results = model.detect([image], verbose=1)
	return results