"""
创建高维稀疏张量
"""
import tensorflow as tf

if __name__ == '__main__':
    sp = tf.SparseTensor(indices=[[0, 2], [1, 3]], values=[1, 2], dense_shape=[3, 4])

    """
    稀疏张亮sp的键值对形式：
    [0,2]:1
    [1,3]:2
    
    表示二阶稀疏张量索引为[0,2]和[1,3]的元素非零，值是[1,2]
    
    等价于[3,4]的二阶稠密张量
    [[0,0,1,0],
    [0,0,0,2],
    [0,0,0,0]]
    """
    with tf.Session() as sess:
        print(sp.eval())
