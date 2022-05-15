import os
from paddleocr import PaddleOCR,draw_ocr
from PIL import Image



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ocr_detect(filePath:str):
    '''
     orc识别
    '''
    print("filePath is ",filePath)
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # need to run only once to download and load model into memory
    result = ocr.ocr(filePath, cls=True)
    result_list = result
    (path,fileName) = os.path.split(filePath)
    image = Image.open(filePath).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./template/fonts/Deng.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(os.path.join(path,"draw-"+fileName))

    return result_list,os.path.join(path,"draw-"+fileName)


def handle_upload_file(f):
    file_name = f.name
    if(not os.path.exists(os.path.join(BASE_DIR, 'template/media-img'))):
        # 判断文件夹路径是否存在，不存在则创建
        os.makedirs(os.path.join(BASE_DIR, 'template/media-img'))
    with open(os.path.join(BASE_DIR, 'template/media-img', file_name), 'wb') as f_write:
        for chunk in f.chunks():
            f_write.write(chunk)
    f_write.close()
    result_json, deteced_filePath = ocr_detect(os.path.join(BASE_DIR, 'template/media-img', file_name))
    return result_json,deteced_filePath,os.path.join(BASE_DIR, 'template/media-img', file_name)

