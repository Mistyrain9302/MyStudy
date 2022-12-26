# %%
import os 
if not os.path.exists('YOLO/yolov5'):
  !git clone https://github.com/ultralytics/yolov5 
  %cd yolov5
  !pip install -r requirements.txt # install dependencies
# %%
