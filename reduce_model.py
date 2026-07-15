import torch
from utils.model import VGGEncoder

print("Loading VGG...")

encoder = VGGEncoder("vgg_normalised.pth")

print("Saving smaller VGG...")

torch.save(
    encoder.state_dict(),
    "vgg_encoder_small.pth"
)

print("Done!")