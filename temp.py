import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
from tqdm import tqdm
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda is_available() else "cpu")
print(f'Using device {device}')

def load_data(data_dir, batch_size=64, val_split=0.2):
    transforms = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
    ])

    full_data = datasets.ImageFolder(root=data_dir, transforms=transforms)

    train_size = int((1-val_split) * len(full_data))
    val_size = len(full_data) - train_size
    train_data, val_data = random_split(full_data, [train_size, val_size])

    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=True)

    print(f'클래스 인덱스: {full_data.class_to_idx}')
    return train_loader, val_loader

class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, stride=1, padding=1)
    