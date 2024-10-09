We used scripts from the following repo to finetune https://github.com/huggingface/diffusers/tree/main/examples/text_to_image
We fine tuned on the imsitu filtered data from 1000 epocs in batch 1 
We finetuned in 3 learning rated e-5, e-4, 5e-5


To train the model:
Run to following note book, the fine tuned model will be save in MODEL_TARGET_FOLDER

You can change learning rate from the flags of !accelerate launch diffusers/examples/text_to_image/train_text_to_image.py

All models aved in huggin face in: ("nadavo11/actions_model" , "ft_lr_1e-4"),("nadavo11/actions_model5" , "ft_lr_5e-5"),("nadavo11/ImSitu_actions_model", "ft_lr_1e-5")