#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

SUFFIX = {
    "FFD8FF": "JPG",
    "89504E47": "PNG",
    "47494638": "GIF",
    "49492A00": "TIF",
    "424D": "BMP",
    "424D228C010000000000": "BMP",
    "424D8240090000000000": "BMP",
    "424D8E1B030000000000": "BMP",
    "41433130": "DWG",
    "38425053": "PSD",
    "7B5C727466": "RTF",
    "3C3F786D6C": "XML",
    "68746D6C3E": "HTML",
    "44656C69766572792D646174653A": "EML",
    "CFAD12FEC5FD746F": "DBX",
    "2142444E": "PST",
    "0xD0CF11E0A1B11AE1": "OLE2",
    "D0CF11E0": ["XLS", "DOC", "DOCX", "XLSX"],
    "5374616E64617264204A": "MDB",
    "FF575043": "WPB",
    "252150532D41646F6265": ["EPS", "PS"],
    "255044462D312E": "PDF",
    "AC9EBD8F": "qdf",
    "458600000600": "qbb",
    "E3828596": "PWL",
    "504B0304": "ZIP",
    "52617221": "RAR",
    "57415645": "WAV",
    "41564920": "AVI",
    "2E7261FD": "RAM",
    "2E524D46": "RM",
    "2E524D46000000120001": "RMVB",
    "000001BA": "MPG",
    "6D6F6F76": "MOV",
    "3026B2758E66CF11": "ASF",
    "60EA": "ARJ",
    "4D546864": "MID",
    "00000020667479706D70": "MP4",
    "49443303000000002176": "MP3",
    "464C5601050000000900": "FLV",
    "1F8B08": "GZ",
    "48544D4C207B0D0A0942": "CSS",
    "696B2E71623D696B2E71": "JS",
    "d0cf11e0a1b11ae10000": ["VSD", "WPS"],
    "6431303A637265617465": "TORRENT",
    "3C2540207061676520": "JSP",
    "7061636B61676520": "JAVA",
    "CAFEBABE0000002E00": "CLASS",
    "504B03040A000000": "JAR",
    "4D616E69666573742D56": "MF",
    "4D5A9000030000000400": "EXE",
    "7F454C4601010100": "ELF",
    "2000604060": "1WK1",
    "00001A0000100400": "3WK3",
    "00001A0002100400": "4WK4",
    "576F726450726F": "LWP",
    "53520100": "SLY"
}


def write_file(filename, suffix):
    """生成新文件文件"""
    if "\\" in filename:
        filename_new = filename.split("\\")[-1] + suffix
    elif "/" in filename:
        filename_new = filename.split("/")[-1] + suffix
    else:
        filename_new = filename + suffix
    pwd = os.getcwd()
    filename_new = os.path.join(pwd, "new", filename_new)
    shutil.copyfile(filename, filename_new)


def identify_suffix(filename):
    """识别文件后缀"""
    with open(filename, 'rb') as f:
        file_content = f.read()
        file_content = file_content.encode('hex')
    for suffix_key in SUFFIX.keys():
        if file_content.startswith(suffix_key.lower()):
            if isinstance(SUFFIX[suffix_key], list):
                suffix = SUFFIX[suffix_key][0]
                print_str = " ".join(SUFFIX[suffix_key])
                print("{} 的后缀可能为 {}".format(filename, print_str))
            else:
                suffix = SUFFIX[suffix_key]
            write_file(filename=filename, suffix=".{}".format(suffix.lower()))
            return
        else:
            pass
    print("{} 未能成功识别后缀名".format(filename))


def get_all_file(path):
    """获取所有文件名"""
    allpath = []
    allfilelist = os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            get_all_file(filepath)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            allpath.append(filepath)
    return allpath


def main(file_dir):
    """主函数"""
    all_path_list = get_all_file(file_dir)
    for filename in all_path_list:
        identify_suffix(filename=filename)


if __name__ == '__main__':
    import sys
    main(sys.argv[1])

