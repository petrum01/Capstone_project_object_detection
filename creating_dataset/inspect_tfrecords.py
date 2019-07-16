import tensorflow as tf

#inspecting one record
for example in tf.python_io.tf_record_iterator("creating_dataset/test.record"):
    result = tf.train.Example.FromString(example)

print(result)

# Counting the number of records
a = sum(1 for _ in tf.python_io.tf_record_iterator("creating_dataset/train.record"))
print('Number of records in train:', a)

b = sum(1 for _ in tf.python_io.tf_record_iterator("creating_dataset/test.record"))
print('Number of records in test:', b)
