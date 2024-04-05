import cv2 as cv
import xml.etree.ElementTree as ET

# Loading Images and XML files
image_path = r"C:\Users\vinot\OneDrive\Documents\Intern_Projects\opencsv\image acquisition\shp1.v1i.voc\test\image"
xml_dir = r"C:\Users\vinot\OneDrive\Documents\Intern_Projects\opencsv\image acquisition\shp1.v1i.voc\test\xml"
output_dir = r"C:\Users\vinot\OneDrive\Documents\Intern_Projects\opencsv\image acquisition\Outputs\vocoutputs"

img_name="parallelogram-8f77d1e4f28c549fae49d10d89ff4068_jpg.rf.8a38ff2820c25bbe90dc1a6341034a81.jpg"
img=image_path+"\\"+img_name

xml_name="parallelogram-8f77d1e4f28c549fae49d10d89ff4068_jpg.rf.8a38ff2820c25bbe90dc1a6341034a81.xml"
xml_src=xml_dir+"\\"+xml_name


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objects = root.findall('object')
    annotations = []
    for obj in objects:
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        class_name = obj.find('name').text
        annotations.append((xmin, ymin, xmax, ymax, class_name))
       
    return annotations

def draw_bounding_boxes(image_path, xml_file, output_dir):
    image = cv.imread(image_path)
    bboxes = parse_xml(xml_file)
    for bbox in bboxes:
        xmin, ymin, xmax, ymax, class_name = bbox
        cv.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        cv.putText(image, class_name, (xmin, ymin - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv.imwrite(output_dir+"\\8.jpg", image)
    cv.imshow("Output",image)

draw_bounding_boxes(img, xml_src, output_dir)


cv.waitKey(0)
            









