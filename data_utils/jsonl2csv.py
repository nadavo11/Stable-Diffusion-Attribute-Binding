import json
import pandas as pd


# Function to convert JSONL file to a CSV compatible with Hugging Face
def convert_jsonl_to_csv(jsonl_path, csv_path):
    data = []

    # Read the JSONL file
    with open(jsonl_path, 'r') as f:
        for line in f:
            entry = json.loads(line.strip())
            # Assuming two images and two captions per entry, similar to earlier structure
            data.append({
                "file_name": f"data/ex_{entry['id']}_img_0.png",
                "caption": entry['caption_0']
            })
            data.append({
                "file_name": f"data/ex_{entry['id']}_img_1.png",
                "caption": entry['caption_1']
            })

    # Create a DataFrame and save it as CSV
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print(f"CSV file saved to {csv_path}")


# Paths for input and output
jsonl_path = 'metadata.jsonl'  # The new JSONL file created earlier
csv_path = '../winoground_subset/metadata.csv'  # Output CSV file path

# Convert the JSONL to CSV
convert_jsonl_to_csv(jsonl_path, csv_path)