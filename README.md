# Achieving Dimension-Free Communication in Federated Learning via Zero-Order Optimization

NOTE: In code implementation we use `cezo_fl` for `FedDisco` in paper

## Run Experiments

- ZOO random gradient estimate + SGD training. rge_main.py: train model using ZOO RGE. example usage: `python rge_main.py --dataset=cifar10 --num-pert=10 --lr=1e-6 --mu=1e-3`

- FedDisco: Follow FL routine. And split data into chunks and train on different clients. example usage: `python cezo_fl_main.py --dataset=sst2 --iterations=10000 --train-batch-size=8 --test-batch-size=200 --eval-iterations=50 --num-clients=3 --num-sample-clients=2 --local-update-steps=1 --num-pert=10 --lr=1e-6 --mu=1e-3 --grad-estimate-method=rge-forward`
