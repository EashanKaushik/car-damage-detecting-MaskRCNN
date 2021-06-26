import cv2
import numpy as np

def class_name(classid):
    id_dict = {1:'Scratch', 2:'Dent', 3:'Shatter', 4:'Dislocation'}
    return id_dict[classid]

def damage_cost(classid):
    # cost_dict = {1: [800, 1400], 2:[1200, 3000],3:19000, 4:17000}
    cost_dict = {1: 900, 2:1600, 3:19000, 4:17000}

    return cost_dict[classid]

def area_ratio(image, roi, mask):
    y1, x1, y2, x2 =  tuple(roi)
    crop_mask = mask[y1:y1+(y2-y1),x1:x1+(x2-x1)].copy()
    pixels = cv2.countNonZero(np.float32(crop_mask))
    image_area = image.shape[0] * image.shape[1]
    area_ratio = 1 + (pixels / image_area)
    return area_ratio

def costEstimate(image, rois, masks, classids):
    cost_id_dict = {
    "Shatter": {"Count": 0, "Cost": 0},
    "Scratch": {"Count": 0, "Cost": 0},
    "Dent": {"Count": 0, "Cost": 0},
    "Dislocation": {"Count": 0, "Cost": 0}
    }
    total = 0
    count = int()
    cost_init = int()
    
    for index in range(rois.shape[0]):

        name = class_name(classids[index])
        cost = damage_cost(classids[index])
        ratio = area_ratio(image, rois[index], masks[: ,: ,index])

        total = total + round(cost * ratio,2)

        # unique_id = str()
        
        # for roi in rois[index]:
        #     unique_id = unique_id + str(roi)
            
        
        if name is 'Scratch':
            count = cost_id_dict[name]['Count'] + 1
            cost_init = cost_id_dict[name]['Cost'] + round(cost * ratio,2)
            cost_id_dict[name]['Count'] = count
            cost_id_dict[name]['Cost'] = cost_init
            # cost_id_dict[name] = "Range: Rs." + str(round(cost[0] * ratio,3)) + ' - Rs.' + str(round(cost[1] * ratio, 3))
        elif name is 'Dent':
            count = cost_id_dict[name]['Count'] + 1
            cost_init = cost_id_dict[name]['Cost'] + round(cost * ratio,2)
            cost_id_dict[name]['Count'] = count
            cost_id_dict[name]['Cost'] = cost_init
            # cost_id_dict[name] = "Range: Rs." + str(cost[0] * ratio) + ' - Rs.' + str(cost[1] * ratio)
        elif name is 'Shatter':
            count = cost_id_dict[name]['Count'] + 1
            cost_init = cost_id_dict[name]['Cost'] + round(cost * ratio,2)
            cost_id_dict[name]['Count'] = count
            cost_id_dict[name]['Cost'] = cost_init
            # cost_id_dict[name] = "Cost: Rs." + str(cost)
        else:
            count = cost_id_dict[name]['Count'] + 1
            cost_init = cost_id_dict[name]['Cost'] + round(cost * ratio,2)
            cost_id_dict[name]['Count'] = count
            cost_id_dict[name]['Cost'] = cost_init
            # cost_id_dict[name] = "Cost: Rs." + str(cost)

    for name, values in cost_id_dict.copy().items():
        if values['Count'] == 0:
            cost_id_dict.pop(name)

    return total, cost_id_dict