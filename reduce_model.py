import torch
from utils.model import VGGEncoder

print("Loading original VGG...")

encoder = VGGEncoder("vgg_normalised.pth")

print("Saving only VGG layers...")

torch.save(
    encoder.vgg.state_dict(),
    "vgg_encoder_small.pth"
)

print("Done!")