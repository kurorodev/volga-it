import tensorflow as tf

MAX_EPOCHS = 20

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(256,256,3)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])


def compile_and_fit(model, patience=2):
  early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                    patience=patience,
                                                    mode='min')

  model.compile(loss=tf.keras.losses.MeanSquaredError(),
                optimizer=tf.keras.optimizers.Adam(),
                metrics=[tf.keras.metrics.MeanAbsoluteError()])

  history = model.fit(epochs=MAX_EPOCHS,
                      callbacks=[early_stopping])
  return history

print(compile_and_fit(model))