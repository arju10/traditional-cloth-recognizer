from fastai.vision.all import *
import gradio as gr



model = load_learner('tradiotional_clothing_recognition-v1.pkl')


categories = model.dls.vocab

def recognize_image(image):
    pred, idx, probs = model.predict(image)
    return dict(zip(categories, map(float, probs)))

image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label(num_top_classes=5)
examples = [
    'unknown-1.jpg',
    'unknown-2.jpg'

    ]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False)


