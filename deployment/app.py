from fastai.vision.all import *
import gradio as gr

# Function to clean up the category name
def clean_category_name(category_name):
    return category_name.replace("_", " ")

model = load_learner('tradiotional_clothing_recognition-v1.pkl')

# Get the original categories from the model
original_categories = model.dls.vocab

# Create a new list with cleaned category names
cleaned_categories = [clean_category_name(category) for category in original_categories]

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(cleaned_categories, map(float, probs)))

image = gr.inputs.Image(shape=(192, 192))
label = gr.outputs.Label(num_top_classes=5)

examples = [
    'unknown-1.jpg',
    'unknown-2.jpg',
    'unknown-6.jpg',
    'unknown-12.jpg',
    'unknown-16.jpg',
    'unknown-18.jpg'
]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)
