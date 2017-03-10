import _init_paths
from datasets.factory import get_imdb

if __name__ == "__main__":

  print "it's here"
  imdb = get_imdb('voc_2007_trainval')
  print('Loaded dataset `{:s}` for training'.format(imdb.name))

  imdb = get_imdb('mio_tcd_loc_train')
  print('Loaded dataset `{:s}` for training'.format(imdb.name))