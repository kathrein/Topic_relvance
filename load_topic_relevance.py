import os
import pandas as pd

def load_aligned_data(split, base_path="Data"):
    """
    Loads and merges prompt, essay, and alignment data.
    
    Returns a DataFrame with: Document_ID, prompt_id, Original_Essay, Error_Essay, Arabic Text (prompt)
    """
    # Load topic alignment
    alignment_path = os.path.join(base_path, "Topic_alignment", f"{split}_topic_alignment.csv")
    alignment_df = pd.read_csv(alignment_path)

    # Load essay
    essay_path = os.path.join(base_path, "ARWI", f"{split}.csv")
    essay_df = pd.read_csv(essay_path)

    # Load prompts
    prompts_path = os.path.join(base_path, "Prompts", "prompts_labelled_with_ids.csv")
    prompts_df = pd.read_csv(prompts_path)[["prompt_id", "Arabic Text"]]
    prompts_df["prompt_id"] = prompts_df["prompt_id"].astype(str)
    alignment_df["prompt_id"] = alignment_df["prompt_id"].astype(str)

    # Merge
    data = alignment_df.merge(prompts_df, on="prompt_id", how="left")
    data = data.merge(essay_df, on="Document_ID", how="left")

    return data

train = pd.DataFrame()
train = load_aligned_data("train",base_path="../Data/Data")
print(train)

