import os
import glob

list = glob.glob("/Users/katasugirupan/Desktop/test2/F2/*")


output_dir = 'dataset_fate'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# print('/Users/katasugirupan/Desktop/test2/' + output_dir + '/' + 'a' + str(1) + '.jpg')

n = 0
for i in list:
    print(i)
    os.rename(i, '/Users/katasugirupan/Desktop/test2/' + output_dir + '/' + 'F' + str(n) + '.jpg') 
    n += 1

