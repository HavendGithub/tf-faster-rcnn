import _init_paths
from datasets.factory import get_imdb

if __name__ == "__main__":
  imdb = get_imdb('mio-tcd-loc_train')
  print('Loaded dataset `{:s}` for training'.format(imdb.name))