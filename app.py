import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf

model = tf.keras.models.load_model("Garbage_1.h5")  

class_names = [
    "battery", "biological", "cardboard", "clothes", "glass",
    "metal", "paper", "plastic", "shoes", "trash"
]

def predict(image):
    image = image.resize((224, 224))  
    image = np.array(image)

    if image.ndim == 2:  # grayscale
        image = np.stack((image,) * 3, axis=-1)
    elif image.shape[-1] != 3:
        image = image[..., :3]  

    image = image.astype(np.float32) / 255.0  
    image = np.expand_dims(image, axis=0)     

    pred = model.predict(image)
    class_idx = np.argmax(pred[0])
    confidence = float(np.max(pred[0]))

    return f"Prediction: {class_names[class_idx]} ({confidence * 100:.2f}%)"

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Waste Classification",
    description="ارفع صورة وسيقوم النموذج بتصنيف نوع النفاية بدقة"
)


interface.launch(server_name="0.0.0.0", server_port=7860 , share = True)
