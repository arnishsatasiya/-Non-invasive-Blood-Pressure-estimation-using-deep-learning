import numpy as np   
import filters


class Preprocesing:

    def normalize(self,arr, t_min, t_max):
        norm_arr = []
        diff = t_max - t_min
        diff_arr = max(arr) - min(arr)+0.000000000000000000000000001
        for i in arr:
            temp = (((i - min(arr))*diff)/diff_arr) + t_min
            norm_arr.append(temp)
        return np.array(norm_arr)
    
    def process(self,raw_signal):
        raw_signal=np.reshape(raw_signal,(1,-1))
        filtered_signal = filters.apply_filter(raw_signal, filters.BPfilter, params={'order':1,'minHz':0.6,'maxHz':4.0,'fps':1000})

       
        normalized_filtered_signal=filtered_signal.T
        normalized_filtered_signal=self.normalize(normalized_filtered_signal,0,1)
        normalized_filtered_signal=normalized_filtered_signal.T
        
        return normalized_filtered_signal
