import hou
import os


def checkDir():

    ffmpegNode = hou.node('/obj/flipbookgen/topnet1/ffmpegencodevideo1')
    openGLNode = hou.node("/obj/flipbookgen/topnet1/ropnet1/opengl1")
    # You can choose you own path
    basePath = "S:\Flipbooks"
    flipbooksPath = os.path.join(basePath, "FlipBooks").replace("\\", "/")
    asset = "hello"

    if not os.path.exists(flipbooksPath):
        os.makedirs(flipbooksPath)
    # Creating these directories is a must!!
    subdirectories = ["ImageText", "Images", "Videos"]
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(flipbooksPath, subdirectory).replace("\\", "/")
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)
    print(f"Directories created/checked in {flipbooksPath}")


    video_path = os.path.join(flipbooksPath, "Videos").replace("\\", "/")
    image_path = os.path.join(flipbooksPath, "Images").replace("\\", "/")
    imagetext_path = os.path.join(flipbooksPath, "ImageText").replace("\\", "/")

    opengl_out = os.path.join(image_path, f"{asset}_$F.jpeg").replace("\\", "/")
    openGLNode.parm("picture").set(opengl_out)

    ffmpegtext_out = os.path.join(imagetext_path, f"{asset}.txt").replace("\\", "/")
    ffmpegNode.parm("framelistfile").set(ffmpegtext_out)

    ffmpeg_out = os.path.join(video_path, f"{asset}.mov").replace("\\", "/")
    ffmpegNode.parm("outputfilepath").set(ffmpeg_out)


