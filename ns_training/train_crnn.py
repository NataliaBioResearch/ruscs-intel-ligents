from ns_training.dataset_tools import load_training_sample

def train_step(model, pcm, label):
    mel = load_training_sample(pcm, augment=True)
    model.train_on_batch(mel, label)
