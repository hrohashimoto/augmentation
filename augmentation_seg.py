#ディレクトリ内にあるjson、png、jpgファイルに対して、水増し処理を施すプログラムが目的で、
#Ver.3=ディレクトリ内にある全jsonの情報抽出

import pandas as pd
import json 
import os.path as osp
import os,sys
import cv2
import glob
import random
import numpy as np

#フォルダ内のjsonファイルの一覧の取得
def file_list(source_dir):
    files=glob.glob(source_dir+"/*.json")
    return files

#jsonファイル内の情報の取得
def json_info(filename):
    #jsonファイル（辞書型の読み込み）
    with open(filename) as f:
        seg_dic = json.load(f)
    return seg_dic

#画像path　key 'imagePath'　
def img_path(seg_dic):
    img_path=seg_dic['imagePath']
    return img_path

#画像サイズ　'imageHeight'　'imageWidth'
def img_size(seg_dic):
    img_height=seg_dic['imageHeight']
    img_width=seg_dic['imageWidth']
    return img_height,img_width

#segmentationの数　'shapes'
def num_seg(seg_dic):
    num_segment=len(seg_dic['shapes'])
    return num_segment

#i番目のセグメントのポイント数
def num_of_points(seg_dic,i):
    num_points=len(seg_dic['shapes'][i]['points'])
    return num_points

def points_xy(seg_dic,num_segment):
    x=np.zeros((20,100))
    y=np.zeros((20,100))
    for i in range(num_segment):
        #各セグメントのポイント数
        num_points=num_of_points(seg_dic,i)
        for j in range(num_points):
            x[i][j]=int(seg_dic['shapes'][i]['points'][j][0])
            y[i][j]=int(seg_dic['shapes'][i]['points'][j][1])
        return x,y

def main():
    source_dir="E:\\DeepLearningProgramBackup\\kasa_jiku_segmentation"
    
    #path一覧リスト
    texts=file_list(source_dir)
    for list_json in range(len(texts)):
        filename=texts[list_json]
        print(list_json," json file name=",filename)
        #各jsonファイルの情報取得
        segmentation_dic=json_info(filename)
        image_path= img_path(segmentation_dic)
        image_height,image_width=img_size(segmentation_dic)
        num_segment=num_seg(segmentation_dic)
        x,y=points_xy(segmentation_dic,num_segment)
        #jsonファイルの情報出力
        print("画像パス    ",image_path)
        print("画像サイズ  ",image_height,image_width)
        print("セグメント数 ",num_segment)
        for i in range(num_segment):
            num_points=num_of_points(segmentation_dic,i)
            for j in range(num_points):
                print('            ',"seg",i,"point",j,x[i][j],y[i][j])

    #path一覧リストのシャッフル
    # shuffle_texts=random.shuffle(texts)
    # for list_files in range(len(texts)):
    #     print(list_files," shuffle filename=",texts[list_files])


if __name__ == '__main__':
    main()