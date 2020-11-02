import os
import torch
from PIL import Image

import torch.utils.data as data
from torchvision import transforms
from torchvision.utils import save_image
import torch.optim as optim
from collections import OrderedDict

import utils
import transforms as ext_transforms
from models.enet import ENet
from models.enet import ENet
from data import CamVid as dataset
from data.utils import enet_weighing, median_freq_balancing

class_encoding = OrderedDict([('sky', (128, 128, 128)), ('building', (128, 0, 0)), ('pole', (192, 192, 128)), ('road', (128, 64, 128)), ('pavement', (60, 40, 222)), ('tree', (128, 128, 0)), ('sign_symbol', (192, 128, 128)), ('fence', (64, 64, 128)), ('car', (64, 0, 128)), ('pedestrian', (64, 64, 0)), ('bicyclist', (0, 128, 192)), ('unlabeled', (0, 0, 0))])


device = torch.device('cuda')

# Load model
num_classes = len(class_encoding)
model = ENet(num_classes).to(device)
optimizer = optim.Adam(model.parameters())
model = utils.load_checkpoint(model, optimizer, 'save/1027', 'ENet')[0]

# Load data
input_image = Image.open("frame1017.png")
preprocess = transforms.Compose([
    transforms.ToTensor()
])
model.eval()

input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0)
input_batch = input_batch.to('cuda')
# print(input_batch)

with torch.no_grad():
    predictions = model(input_batch)

_, predictions = torch.max(predictions.data, 1)

# print(predictions)

label_to_rgb = transforms.Compose([
        ext_transforms.LongTensorToRGBPIL(class_encoding),
        transforms.ToTensor()
])

color_predictions = utils.batch_transform(predictions.cpu(), label_to_rgb)
utils.imshow_batch(input_batch.data.cpu(), color_predictions)
save_image(color_predictions, "prediction.png")



