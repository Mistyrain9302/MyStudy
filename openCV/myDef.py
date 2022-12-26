# %% 
import numpy as np
import cv2
import os
# %%
file_path='.\\data\\src'
file_list = os.listdir(file_path)
file_list

def preprocessing(car_no):
    img_array=np.fromfile(file_path+'\\'+file_list[car_no],np.uint8)
    image=cv2.imdecode(img_array,cv2.IMREAD_COLOR)    
    if image is None:
        return None, None
    kernel = np.ones((5,17),np.uint8)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray,(5,5))
    gray = cv2.Sobel(gray,cv2.CV_8U,1,0,3)
    
    th_img = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)[1]
    morph = cv2.morphologyEx(th_img,cv2.MORPH_CLOSE,kernel,iterations=3)
    
    # cv2.imshow('th_img',th_img); cv2.imshow('morph',morph)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return image, morph
# %%
def verify_aspect_size(size):
    w, h = size
    if h == 0 or w == 0 : return False
    
    aspect = h / w if h > w else w / h
    chk1 = 3000 < (h*w) < 12000
    chk2 = 2.0 < aspect < 6.5
    return(chk1 and chk2)
# %%
def find_candidates(image):
    results = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = results[0] if int(cv2.__version__[0]) >=4 else results[1]
    
    rects = [cv2.minAreaRect(i) for i in contours]
    candidates = [(tuple(map(int,center)),tuple(map(int,size)),angle) 
                  for center,size,angle in rects if verify_aspect_size(size)]
    return candidates
# %%
def color_candidate_img(image,candi_center):
    h,w=image.shape[:2]
    fill = np.zeros((h+2,w+2),np.uint8)
    dif1,dif2=(25,25,25),(25,25,25)
    flags = 0xff00+4+cv2.FLOODFILL_FIXED_RANGE
    flags+=cv2.FLOODFILL_MASK_ONLY
    
    pts=np.random.randint(-15,15,(20,2))
    pts=pts+candi_center
    for x,y in pts:
        if 0<=x<w and 0<=y<h:
            _,_,fill,_=cv2.floodFill(image,fill,(x,y),255,dif1,dif2,flags)
        return cv2.threshold(fill,120,255,cv2.THRESH_BINARY)[1]

def rotate_plate(image,rect):
    center,(w,h),angle = rect
    if w < h:
        w,h = h,w
        angle+=90
    size = image.shape[1::-1]
    rot_mat = cv2.getRotationMatrix2D(center,angle,1)
    rot_img = cv2.warpAffine(image,rot_mat,size,cv2.INTER_CUBIC)
    
    crop_img = cv2.getRectSubPix(rot_img,(w,h),center)
    crop_img = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
    return cv2.resize(crop_img,(144,28))

def checkImg(car_no):    
    image,morph = preprocessing(car_no)
    candidates=find_candidates(morph)

    fills = [color_candidate_img(image,size) for size,_,_ in candidates]
    new_candis = [find_candidates(fill) for fill in fills]
    new_candis = [cand[0] for cand in new_candis if cand]
    candidate_imgs = [rotate_plate(image,cand) for cand  in new_candis]

    for i,img in enumerate(candidate_imgs):
        cv2.polylines(image,[np.int32(cv2.boxPoints(new_candis[i]))],True,(0,225,255),2)
        cv2.imshow('candidate_img'+str(i),img)

    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
