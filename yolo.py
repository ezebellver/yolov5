import os

# Ensure you are in the YOLOv5 directory
os.chdir('.')

# Command to train YOLOv5
command = (
    "python .\\train.py --img 400 --batch 30 --epochs 50 "
    "--data C:\\Users\\bellv\\OneDrive\\Escritorio\\Uni\\5toA2doC\\Tesis\\EchoFlow\\dataset.yaml --cfg models\\yolov5s.yaml "
    "--weights yolov5s.pt --name my_yolov5_model"
)

# Execute the training command
os.system(command)
