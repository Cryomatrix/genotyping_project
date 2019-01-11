'''
Created on Jun 25, 2018
@author: Soraya
Detecting ladders with Template Matching and using that location to number gels

'''
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import datetime

''' From OpenCV "Template Matching with multiple objects" documentation '''

img_rgb = cv2.imread('C:/Users/Cryomatrix/Desktop/Genotyping_project/sample_gel.tif') # Load sample gel #
img_rgb = cv2.flip(img_rgb, 1)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('C:/Users/Cryomatrix/Desktop/Genotyping_project/template_gel.tif', 0) # Load template #
w, h = template.shape[::-1]

locations = []

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
''' Draws rectangle around ladders detected; uses location of match and appends to locations [] '''
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
    x = (pt[0] + w, pt[1] + h)
    locations.append(x)

# Create coordinates that match a point in template-matched rect #
''' NEED TO CHANGE THE LOCATIONS, NOT ADJUSTED FOR ALL IMAGES. SOMETIMES ITS OUT OF RANGE '''
''' Maybe need to set it as a ratio of something, or median of list len'''
''' 'offset' is (x,y) how much to move from initial point detected from a given point from template-matching line 31 '''
''' if function chooses which indexed coordinates to take from list according to number of template matched  '''

offset = (3, -70)
if len(locations) >= 70:
    pt_1 = locations[25]
    pt_2 = locations[45]
    pt_3 = locations[67]
    pt_4 = locations[70]
    # print(len(locations))
    new_pt_1 = tuple(map(sum, zip(pt_1, offset)))
    new_pt_2 = tuple(map(sum, zip(pt_2, offset)))
    new_pt_3 = tuple(map(sum, zip(pt_3, offset)))
    new_pt_4 = tuple(map(sum, zip(pt_4, offset)))
elif len(locations) >= 30:
    pt_1 = locations[10]
    pt_2 = locations[17]
    pt_3 = locations[30]
    new_pt_1 = tuple(map(sum, zip(pt_1, offset)))
    new_pt_2 = tuple(map(sum, zip(pt_2, offset)))
    new_pt_3 = tuple(map(sum, zip(pt_3, offset)))
else:
    pass

''' INFORMATION ABOUT GEL'''
numberofsamples = 73
adjustednumberofsamples = numberofsamples + 2
samples = list(range(1, adjustednumberofsamples))
# Sample information
first_sample = 26
last_sample = 96

colony = 'CZ'  # Samples issued from which colony #
gelist = 'SL'  # Initials of person who ran assay #
date_of_gel = datetime.date.today()  # Assuming date of gel is today #
#  If another date, comment-out next line and update the date accordingly #
# date_of_gel = 2018-06-19


''' Pass image on PIL '''
pil_img = Image.fromarray(img_rgb)
draw = ImageDraw.Draw(pil_img)
fnt = ImageFont.truetype("calibri.ttf", 16)


''' Arbitraty/eye-balled offset for numbers of different lengths (i.e., 1 digit, 2 digits, 3 digits) '''
smalleroffset = (28.4, 0)
smallestoffset = (26.5, 0)
hundredoffset = (20, 0)

''' Writing sample number on row '''
# First Row#
for i in samples[0:25]:
    if i != len(samples):
        if i < 10:
            draw.text((new_pt_1), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_1 = tuple(map(sum, zip(new_pt_1, smalleroffset)))
            i += 0
        elif i >= 100:
            draw.text((new_pt_1), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_1 = tuple(map(sum, zip(new_pt_1, hundredoffset)))
            i += 0
        else:
            draw.text((new_pt_1), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_1 = tuple(map(sum, zip(new_pt_1, smallestoffset)))
            i += 0
    elif i >= len(samples):
        draw.text((new_pt_1), ('WT CRE Tris'), font=fnt, fill=(0, 0, 0))
        new_pt_1 = tuple(map(sum, zip(new_pt_1, smallestoffset)))
        i += 0
# Second Row#
for i in samples[25:51]:
    if i != len(samples):
        if i < 10:
            draw.text((new_pt_2), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_2 = tuple(map(sum, zip(new_pt_2, smalleroffset)))
            i += 0
        elif i >= 100:
            draw.text((new_pt_2), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_2 = tuple(map(sum, zip(new_pt_2, hundredoffset)))
            i += 0
        else:
            draw.text((new_pt_2), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_2 = tuple(map(sum, zip(new_pt_2, smallestoffset)))
            i += 0
    elif i >= len(samples):
        draw.text((new_pt_2), ('WT CRE Tris'), font=fnt, fill=(0, 0, 0))
        new_pt_2 = tuple(map(sum, zip(new_pt_2, smallestoffset)))
        i += 0
# Third Row#
for i in samples[51:77]:
    if i != len(samples):
        if i < 10:
            draw.text((new_pt_3), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_3 = tuple(map(sum, zip(new_pt_3, smalleroffset)))
            i += 0
        elif i >= 100:
            draw.text((new_pt_3), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_3 = tuple(map(sum, zip(new_pt_3, hundredoffset)))
            i += 0
        else:
            draw.text((new_pt_3), str(i), font=fnt, fill=(0, 0, 0))
            new_pt_3 = tuple(map(sum, zip(new_pt_3, smallestoffset)))
            i += 0
    elif i >= len(samples):
        draw.text((new_pt_3), ('WT CRE Tris'), font=fnt, fill=(0, 0, 0))
        new_pt_3 = tuple(map(sum, zip(new_pt_3, smallestoffset)))
        i += 0
# Fourth Row #
''' Because we do not always have a fourth row of sample '''
if len(samples) > 77:
    for i in samples[77:]:
        if i != len(samples):
            if i < 10:
                draw.text((new_pt_4), str(i), font=fnt, fill=(0, 0, 0))
                new_pt_4 = tuple(map(sum, zip(new_pt_4, smalleroffset)))
                i += 0
            elif i >= 100:
                draw.text((new_pt_4), str(i), font=fnt, fill=(0, 0, 0))
                new_pt_4 = tuple(map(sum, zip(new_pt_4, hundredoffset)))
                i += 0
            else:
                draw.text((new_pt_4), str(i), font=fnt, fill=(0, 0, 0))
                new_pt_4 = tuple(map(sum, zip(new_pt_4, smallestoffset)))
                i += 0
        elif i >= len(samples):
            draw.text((new_pt_4), ('WT CRE Tris'), font=fnt, fill=(0, 0, 0))
            new_pt_4 = tuple(map(sum, zip(new_pt_4, smallestoffset)))
            i += 0
else:
    pass

''' Save image '''
pil_img.save('C:/Users/Cryomatrix/Desktop/Genotyping_project/' + gelist + '_' + colony + "_" + str(date_of_gel) + "_samples_" + str(
    first_sample) + "-" + str(last_sample) + '.png', 'PNG')

''' Show image '''
cv2_img_proc = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
cv2.imshow('Genotyping samples %s' %(date_of_gel), cv2_img_proc)
cv2.waitKey(0)