from image_processing import *

# display the picture
# input the areas of interest
# average the red values on the image,


def get_absorbance(n, blank):
    return -math.log10(n / blank)


directories_in_str = ["blank", "10mg", "20mg", "40mg", "60mg"]

all_images = get_images()

first = []
for thing in all_images:
    first.append(fix_image(cv2.imread(thing[1])))

mid = []
for thing in all_images:
    mid.append(fix_image(cv2.imread(thing[int(len(thing) / 2)])))

first_quart = []
for thing in all_images:
    first_quart.append(fix_image(cv2.imread(thing[int(len(thing) / 4)])))

last_quart = []
for thing in all_images:
    last_quart.append(fix_image(cv2.imread(thing[int((len(thing) / 4) * 3)])))

darkness_2 = []
for thing in all_images:
    darkness_2.append(fix_image(cv2.imread(thing[-1])))

# display_images(mid)

cropped_images = []
cropped_images2 = []
cropped_images3 = []
cropped_images4 = []
cropped_images5 = []

for img in first:
    crop_img = crop_image(img, 195, 350, 205, 365)
    # crop_img = img[350:370, 184:206]
    cropped_images.append(crop_img)

for img in first_quart:
    crop_img = crop_image(img, 195, 350, 205, 365)
    # crop_img = img[350:370, 184:206]
    cropped_images2.append(crop_img)

for img in mid:
    crop_img = crop_image(img, 195, 350, 205, 365)
    # crop_img = img[350:370, 184:206]
    cropped_images3.append(crop_img)

for img in last_quart:
    crop_img = crop_image(img, 195, 350, 205, 365)
    # crop_img = img[350:370, 184:206]
    cropped_images4.append(crop_img)

for img in darkness_2:
    crop_img = crop_image(img, 195, 350, 205, 365)
    # crop_img = img[350:370, 184:206]
    cropped_images5.append(crop_img)

# display_images(cropped_images)

concentrations = [10, 20, 40, 60]

red_vals = []
red_vals2 = []
red_vals3 = []
red_vals4 = []
red_vals5 = []

for img in cropped_images:
    red_vals.append(get_red_val(img))

for img in cropped_images2:
    red_vals2.append(get_red_val(img))

for img in cropped_images3:
    red_vals3.append(get_red_val(img))

for img in cropped_images4:
    red_vals4.append(get_red_val(img))

for img in cropped_images5:
    red_vals5.append(get_red_val(img))


def return_abs_array(vals):
    things = []
    for val in vals:
        if val != vals[0]:
            things.append(get_absorbance(val, vals[0]))
    return things


abs_stuff = return_abs_array(red_vals)
abs_stuff2 = return_abs_array(red_vals2)
abs_stuff3 = return_abs_array(red_vals3)
abs_stuff4 = return_abs_array(red_vals4)
abs_stuff5 = return_abs_array(red_vals5)


slope, intercept, r_value, p_value, std_err = stats.linregress(concentrations, abs_stuff)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(concentrations, abs_stuff2)
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(concentrations, abs_stuff3)
slope4, intercept4, r_value4, p_value4, std_err4 = stats.linregress(concentrations, abs_stuff4)
slope5, intercept5, r_value5, p_value5, std_err5 = stats.linregress(concentrations, abs_stuff5)


current_slope = (slope + slope2 + slope3 + slope4 + slope5) / 5
intercept_end = (intercept + intercept2 + intercept3 + intercept4 + intercept5) / 5

pic = cv2.imread("k2/scene00001.png")
pic2 = cv2.imread("s1/scene00001.png")
pic3 = cv2.imread("p1/scene00001.png")
pic4 = cv2.imread("p1/scene00211.png")
pic5 = cv2.imread("40mg/scene00256.png")

pic = crop_image(fix_image(pic), 186, 329, 207, 345)
pic2 = crop_image(fix_image(pic2), 186, 350, 207, 370)
pic3 = crop_image(fix_image(pic3), 186, 350, 207, 370)
pic4 = crop_image(fix_image(pic4), 186, 350, 207, 370)
pic5 = crop_image(fix_image(pic5), 186, 350, 207, 370)

cv2.imshow("k", pic5)
cv2.waitKey(0)


k2 = get_absorbance(get_red_val(pic), red_vals[0])
s1 = get_absorbance(get_red_val(pic2), red_vals[0])
p1 = get_absorbance(get_red_val(pic3), red_vals[0])
k1 = get_absorbance(get_red_val(pic4), red_vals[0])
oof = get_absorbance(get_red_val(pic5), red_vals[0])
print(k2)
print(s1)
print(p1)
print(k1)
print(oof)


def get_concentration(abs):
    return (abs - intercept_end) / current_slope


def get_concentration2(abs):
    return (abs - intercept) / slope


print(get_concentration(k2))
print(get_concentration(s1))
print(get_concentration(p1))
print(get_concentration(k1))
print(get_concentration(oof))

