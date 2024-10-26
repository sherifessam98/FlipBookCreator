import os
import hou

ffmpegNode = hou.node('/obj/flipbookgen/topnet1/ffmpegencodevideo1')


def openMp4():
    mp4FilePath = ffmpegNode.parm("outputfilepath").eval()
    os.startfile(mp4FilePath)