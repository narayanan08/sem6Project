import time
from ultralytics import YOLO

start_time = time.time()
model = YOLO('model.pt')
path=r"C:\Users\haris\OneDrive\Desktop\final proj\ftest"
model.predict(source=path, imgsz=640, conf=0.5,show=True)
end_time = time.time()
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")
