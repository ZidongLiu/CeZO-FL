from torch import nn
from shared import compression


# This commented CNN have exploding gradient issue when batch_size = 4
# class CNN_MNIST(nn.Module):
#     def __init__(self):
#         super(CNN_MNIST, self).__init__()
#         self.conv1 = nn.Conv2d(1, 6, 5)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(6, 16, 5)
#         self.fc1 = nn.Linear(16 * 4 * 4, 84)
#         self.fc2 = nn.Linear(84, 10)

#     def forward(self, x):
#         x = self.pool(nn.functional.relu(self.conv1(x)))
#         x = self.pool(nn.functional.relu(self.conv2(x)))
#         x = x.view(-1, 16 * 4 * 4)
#         x = nn.functional.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x


class COMPRESSED_CNN_MNIST(nn.Module):
    model_name = "COMPRESSED_CNN_MNIST"

    def __init__(self):
        super(COMPRESSED_CNN_MNIST, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=5,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(16, 32, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.out = nn.Linear(32 * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        # compress activation by top-k
        x = compression.top_k(tensor=x, k=8)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output
