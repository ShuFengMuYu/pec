from torch.utils.data import Dataset
import os
import json

class PecDataset(Dataset):
    def __init__(self, filename:str) -> None:
        super().__init__()
        if filename is None or not os.path.isfile(filename):
            raise RuntimeError('数据文件不存在')
        with open(file=filename, mode='r') as fp:
            json_list = fp.readlines()
            self.data = list(map(json.loads, json_list))
        
    def __len__(self) -> int:
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]