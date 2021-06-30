import os


def covert_str_filename_to_num_name(path_input, path_output):
    raw_names = os.listdir(path_input)
    raw_names = [int(x[:-4]) for x in raw_names]
    for i in range(len(raw_names)):
        os.rename(os.path.join(path_input, str(
            raw_names[i])+'.bmp'), os.path.join(path_output, "{:0>4}".format(str(i))+'.bmp'))


if __name__ == "__main__":
    path_input = "G:/data/test_20210618/reconstruction_image/"
    path_output = "G:/data/test_20210618/reconstruction_image/"


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
