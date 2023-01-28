import data
import numpy as np
import matplotlib.pyplot as plt
import filters
import json







obj=data.DataUtils()

# # print(obj.signalMat())
print("loading start....")
fileList, rawSignalDict,filteredSignalDict=obj.signalMat(True)

print("file saving.....")

with open('filtered_data.txt', 'w') as convert_file:
     convert_file.write(json.dumps(filteredSignalDict))

np.savetxt('filelist.txt', np.array(fileList), delimiter=',')   # X is an array


# raw_signal=signalDict[fileList[100]]
# raw_signal=np.reshape(raw_signal,(1,-1))
# print(raw_signal.shape)
# filtered_signal = filters.apply_filter(raw_signal, filters.BPfilter, params={'order':1,'minHz':0.6,'maxHz':4.0,'fps':1000})

# a=filtered_signal.shape[0]
# b=filtered_signal.shape[1]
# # signal=np.reshape(filtered_BVPs,(a*b,))
# normalized_filtered_signal=filtered_signal.T
# normalized_filtered_signal=normalize(normalized_filtered_signal,0,1)
# normalized_filtered_signal=normalized_filtered_signal.T
# print(filtered_signal.shape)


# # plt.plot(np.arange(2100),raw_signal[0])
# plt.plot(np.arange(2100),normalized_filtered_signal[0])

# plt.show()


a={
    "name":"arnish",
    "age":20
}






  
# with open('convert.txt', 'w') as convert_file:
#      convert_file.write(json.dumps(a))



# with open('convert.txt') as f:
#     data = f.read()

# js = json.loads(data)