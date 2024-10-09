This code used for evaluating the trauned model.
We used two types of scors to evaluate the generated images:
1. CLIP Score
2. BLIP model using BERTScore

We evaluate the model using two lists of captions:
1. Benchmark list - manual list we created, we genrated images from all models (base and 3 trained) in 4 diffrent seeds (41-43)
2. Winoground filtered captions - we used the reverse_caption filtwering to filter intresting captions from the winoground data set and generate images from all models in seed 42


We use the reverse caption function (same one from the data filtering) to reverse the test set captions and meaure each one of the scorse on the reverse caption + generated image from the forward caption.
Then we calcuate the diff between them, expacting to have bigger diff when the model is more sensitive to agent-action-patient direction.

Run the following note book cell by cell
The images will be saved in '/content/drive/My Drive/deep_learning_project/Project_036635803_305673212_312349509/output/models_results/<model>/generated_image/<test_set>'
According to the model you are running '/content/drive/My Drive/deep_learning_project/Project_036635803_305673212_312349509/output/models_results/<model>/simularity_scors/<test_set>'
You can skipe the genrate images block if you wish to save time as the images are already in the drive 
Make sure toy habe image_data.json per generated images directory 