#  Traditional Cloth Recognizer
An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model can classify 23 different types of Traditional Cloth <br/>
The types are following: <br/>

# 1. Interesting Topic Selection with 9+ categories (done)
## Topic: Traditional Cloth Recognizer
### Categories: (23)
-	1	.	   "kimono (Japan)",
-	2	.	    "hanbok (South Korea)",
-	3	.	    "cheongsam/qipao (China)",
-	4	.	    "sari (India)",
-	5	.	    "thawb/dishdasha (Saudi Arabia)",
-	6	.	    "dirndl (Germany)",
-	7	.	    "kilt (Scotland)",
-	8	.	    "ao dai (Vietnam)",
-	9	.	    "boubou (West Africa)",
-	10	.	    "huipil (Mexico)",
-	11	.	    "sarong (Indonesia)",
-	12	.	    "chador (Iran)",
-	13	.	    "traje de flamenca (Spain)",
-	14	.	    "batik (Malaysia)",
-	15	.	    "thobe (Palestine)",
-	16	.	    "national dress (Norway)",
-	17	.	    "national costume (Philippines)",
-	18	.	    "barong tagalog (Philippines)",
-	19	.	    "abaya (United Arab Emirates)",
-	20	.	    "folkdräkt (Sweden)",
-	21	.	    "ao po'i (Paraguay)",
-	22	.	    "pounamu piupiu (New Zealand)",
-	23	.	    "kaftan (Morocco)"

# 2. Data Collection, Model Training, Data Cleaning (done)
**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>


# Training and Data Cleaning
**Training:** Fine-tuned a resnet34 model for 6 epochs (3 times) and got upto ~70% accuracy. <br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or fine-tuning, except for the last time which was the final iteration of the model. <br/>

# 3. Deploy Model with Gradio & HuggingFace Spaces (done)
I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/msideadman/cap-recognizer).
 ### Gradio App URL: https://897f24d5bf9ba00855.gradio.live 
      <br/>

<img src = "deployment/gradio_deploy.png" width="700" height="350">

# 4. Build a GitHub Pages Website and integrate API (done)
The deployed model API is integrated [here](https://arju10.github.io/tradiotional-cloth-recognizer/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.


# 5. Setting Up the project in GitHub  (done)
> https://github.com/arju10/traditional-cloth-recognizer.git
