Run the notebook Select_imSitu.ipynb.
The notebook filters the imSitu data set to a subset that is enriched with images that show a clear direction
of agent-patient-action.
The notebook is currently designed to run on google colab and can run using a CPU.
The working directory in the code is set to Project_036635803_305673212_312349509/data/imSitu, make sure that under that hierarchy
there is a folder called 'of500_images_resized' with the imSitu images.
Parallel to the 'of500_images_resized', there sould be 4 json files:
train.json, dev.json, test.json, imsitu_space.json.
All of the relevant files can be found in the official imSitu website at:
https://prior.allenai.org/projects/imsitu