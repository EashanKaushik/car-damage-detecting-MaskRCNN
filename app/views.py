# Basic System Imports
import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Flask Import
from flask import render_template, request, Flask, url_for


# Model Import
from app.utils import model_predict

# Cost Asssessment Import
from app import cost_assessment

# Mask-RCNN Import
from mrcnn import visualize

UPLOAD_PATH = 'static/uploads/'
UPLOAD_PRED_PATH = 'static/prediction/'

def base():
    return render_template('base.html')


def index():
    return render_template('index.html')


def damageapp():
    return render_template('damageapp.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size # width and height
    aspect = size[0]/size[1] # width / height
    w = 300 * aspect
    return int(w)

def damage():
	fileupload = False

	if request.method == 'POST':
		# File Upload
		fileupload=True
		f = request.files['fileToUpload']
		if not os.path.exists(os.path.join(UPLOAD_PATH, f.filename.split('.')[0])):
			os.mkdir(os.path.join(UPLOAD_PATH, f.filename.split('.')[0]))
		image_path = f.filename.split('.')[0] + '/' + f.filename
		print(UPLOAD_PATH + image_path)
		f.save(UPLOAD_PATH + image_path)
		print(f'File saved Successfully @ {image_path}')

		# Class Prediction
		results = model_predict(UPLOAD_PATH + image_path)
		
		class_names = ['BG', 'Scratch', 'Dent', 'Shatter', 'Dislocation']
		
		r = results[0]

		image = plt.imread(UPLOAD_PATH + image_path)
		# image = load_img(UPLOAD_PATH + image_path)
		# image = img_to_array(image)
		
		if not os.path.exists(UPLOAD_PRED_PATH + f.filename.split('.')[0]):
					os.mkdir(os.path.join(UPLOAD_PRED_PATH, f.filename.split('.')[0]))

		pred_path = UPLOAD_PRED_PATH + f.filename.split('.')[0]

		# Save Predicted Class Image
		visualize.save_instances(image, r['rois'], r['masks'], r['class_ids'], class_names,  r['scores'], path=pred_path + '/' + f.filename)
		get_masks_filenames = visualize.get_masks(image, r['masks'], r['rois'], class_names, r['class_ids'], path=pred_path + '/')
		top_masks_filenames = visualize.display_top_masks_edit(image, r['masks'], r['class_ids'], class_names, path=pred_path + '/')
		get_roi_filenames = visualize.get_rois(image, r['rois'], path=pred_path + '/')
		total, cost = cost_assessment.costEstimate(image, r['rois'], r['masks'], r['class_ids'])
		print(f'File Successfully Manipulated @ {pred_path}')
		data = {
		'visualize': f.filename.split('.')[0] + '/' + f.filename,
		'width': getwidth(UPLOAD_PATH + f.filename.split('.')[0] + '/' + f.filename),
		'masks': get_masks_filenames,
		'top_masks': top_masks_filenames,
		'roi': get_roi_filenames,
		'cost': cost,
		'total': total,
		'tax': round(total * 0.1, 3),
		'tax_total': total + round(total * 0.1, 3)
		}


		return	render_template('damage.html', pagename='Damage Detect', fileupload=fileupload, data=data)
	return render_template('damage.html', pagename='Damage Detect', fileupload=fileupload)