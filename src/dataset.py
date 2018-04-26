
class Dataset():

    def __init__(self, images, labels, emotion_index_map, time_delay=None):
        self._images = images
        self._labels = labels
        self._emotion_index_map = emotion_index_map
        self._time_delay = time_delay

    def get_images(self):
        return self._images

    def get_labels(self):
        return self._labels

    def get_emotion_index_map(self):
        return self._emotion_index_map

    def get_time_delay(self):
        return self._time_delay