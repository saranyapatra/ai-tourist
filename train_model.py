# train_model.py: Final Stable Configuration (Base Model FROZEN)

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNetV2
import os
import math # <-- NEW IMPORT

# --- 1. Configuration ---
IMAGE_SIZE = (224, 224)   
BATCH_SIZE = 32           
NUM_CLASSES = 6           
EPOCHS = 10 # Using 10 epochs for faster execution
MODEL_PATH = 'monument_model.h5' 
DATA_DIR = 'data' 
VALIDATION_SPLIT = 0.25 

# --- 2. Balanced Data Augmentation ---
train_datagen = ImageDataGenerator(
    rescale=1./255,           
    rotation_range=10,        
    width_shift_range=0.1,    
    height_shift_range=0.1,   
    shear_range=0.1,          
    zoom_range=0.1,           
    horizontal_flip=True,     
    fill_mode='nearest'       
)

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    DATA_DIR + '/training', 
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=True
)

validation_generator = validation_datagen.flow_from_directory(
    DATA_DIR + '/validation',
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False
)

# --- 3. Build the Model (Stable: Base Model FROZEN) ---
base_model = MobileNetV2(
    weights='imagenet', 
    include_top=False,         
    input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3)
)

# FREEZE THE ENTIRE BASE MODEL for stability
base_model.trainable = False 
for layer in base_model.layers:
    layer.trainable = False 

# Add new classification layers (the 'head')
x = base_model.output
x = GlobalAveragePooling2D()(x) 
x = Dense(1024, activation='relu')(x)
predictions = Dense(NUM_CLASSES, activation='softmax')(x) 

model = Model(inputs=base_model.input, outputs=predictions)

# --- 4. Compile and Train the Model ---
model.compile(
    optimizer='adam', 
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\nStarting STABLE Training (Base Model Frozen, Steps Corrected)...")

if train_generator.samples == 0 or validation_generator.samples == 0:
    print("ERROR: Generators found 0 images. Check your data folder structure.")
else:
    # CRITICAL FIX: Use math.ceil to ensure all data is processed
    steps_per_epoch = math.ceil(train_generator.samples / BATCH_SIZE)
    validation_steps = math.ceil(validation_generator.samples / BATCH_SIZE)

    model.fit(
        train_generator,
        steps_per_epoch=steps_per_epoch, # Using the calculated, rounded-up steps
        epochs=EPOCHS, 
        validation_data=validation_generator,
        validation_steps=validation_steps # Using the calculated, rounded-up validation steps
    )
    print("Training finished.")

    # 5. Save the Model
    model.save(MODEL_PATH)
    print(f"\nModel successfully saved to {MODEL_PATH}.")
