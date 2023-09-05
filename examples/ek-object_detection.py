from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()

detector.setModelPath( os.path.join(execution_path , "models/retinanet_resnet50_fpn_coco-eeacb38b.pth"))

fileName = "AC_SL1500_.jpg"
file_path = "data-images/"
file, ext = fileName.split(".")
detectedFileName = f"{file}_detected.{ext}"

detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , file_path+fileName ), output_image_path=os.path.join(execution_path , file_path+detectedFileName), minimum_percentage_probability=40)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")