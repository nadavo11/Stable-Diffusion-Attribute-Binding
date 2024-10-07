Run the notebook winoground_filtering.ipynb.
The notebook filters the Winoground data set to a subset that is enriched with images that show a clear direction
of agent-patient-action.
The notebook is currently designed to run on google colab and can run using a CPU.
The working directory in the code is set to submition/data/Winoground, make sure that under that hierarchy
there is a file called 'winoground.jsonl' with the Winoground captions.
The file can be downloaded from this site:
https://huggingface.co/datasets/facebook/winoground