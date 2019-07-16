import cv2
import os

def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)

    cap = cv2.VideoCapture(pathIn)
    count = 0

    while (cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(400 + count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def main():
    extractFrames('/Users/pm/Documents/AI/compvision/TFOD_latest/Capstone_project_object_detection/creating_dataset/background_img/background.mp4', '/Users/pm/Documents/AI/compvision/TFOD_latest/Capstone_project_object_detection/creating_dataset/background_img/fram')

if __name__=="__main__":
    main()


```python
import os
annot_dir = '/Users/pm/Documents/AI/compvision/TFOD_latest/Capstone_project_object_detection/creating_dataset/background_img/frames/annotations'
img_dir = '/Users/pm/Documents/AI/compvision/TFOD_latest/Capstone_project_object_detection/creating_dataset/background_img/frames'
filesA = [os.path.splitext(filename)[0] for filename in os.listdir(annot_dir)]
filesB = [os.path.splitext(filename)[0] for filename in os.listdir(img_dir)]
print ("images without annotations:",set(filesB)-set(filesA))
```
