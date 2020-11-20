import glob
#import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def get_section_results(file):
    """
        requires tensorflow==1.12.0
    """
    X = []
    Y = []
    for e in tf.train.summary_iterator(file):
        for v in e.summary.value:
            if v.tag == 'Train_EnvstepsSoFar':
                X.append(v.simple_value)
            elif v.tag == 'Eval_AverageReturn':
                Y.append(v.simple_value)
    return X, Y

if __name__ == '__main__':
    import glob

    logdir = 'data/*/events*'
    eventfile = glob.glob(logdir)[0]

    X, Y = get_section_results(eventfile)
    import ipdb; ipdb.set_trace()
    for i, (x, y) in enumerate(zip(X, Y)):
        print('Iteration {:d} | Train steps: {:d} | Return: {}'.format(i, int(x), y))