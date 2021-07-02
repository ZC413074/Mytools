import os


def covert_str_filename_to_num_name(path_input, path_output, digit_width):
    """
    Read file names from input file, which is ordered in lexicographical order. Then rename the file by the number in in lexicographical order.
    Finally, 0 is added to the beginning of the name, when the digital width of name is smaller than defined digital width.

    Parameters
    ----------

    path_input : file path of files that need to be rename.

    path_output : file path of files to store, whoes files renamed.

    digit_width : the width of digit.

    """
    raw_names = os.listdir(path_input)
    image_format = str(raw_names[0][-4:])
    for i in range(len(raw_names)):
        os.rename(os.path.join(path_input, str(
            raw_names[i])), os.path.join(path_output, str(i).rjust(digit_width, '0')+image_format))


if __name__ == "__main__":
    path_input = "G:/data/test_20210618/几何一扎带/3kmh-1/"
    path_output = "G:/data/test_20210618/reconstruction_image/"
    path_output = path_input
    covert_str_filename_to_num_name(path_input, path_input, 4)


# A = [x for x in raw_names if x>=5000 and x<=5010]
# B = [x for x in raw_names if x>=5011 and x<=5100]
# C = [x for x in raw_names if x>=5101 and x<=6000]
# D = [x for x in raw_names if x>=6001 and x<=8707]
# A=sorted(A)
# B=sorted(B)
# C=sorted(C)
# D=sorted(D)
# for i in range(len(D)):
#     os.rename(os.path.join(path_input,str(D[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i))+'.bmp'))
# for i in range(len(C)):
#     os.rename(os.path.join(path_input,str(C[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i+len(D)))+'.bmp'))
# for i in range(len(B)):
#     os.rename(os.path.join(path_input,str(B[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i+len(D)+len(C)))+'.bmp'))
# for i in range(len(A)):
#     os.rename(os.path.join(path_input,str(A[i])+'.bmp'), os.path.join(path_input,"{:0>4}".format(str(i+len(D)+len(C)+len(B)))+'.bmp'))
