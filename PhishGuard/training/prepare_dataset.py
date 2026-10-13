
from pathlib import Path
import sys

import pandas as pd

# Project root folder ko Python path mein add karo
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from feature_extraction import extract_features, FEATURE_COLUMNS


# Actual dataset ka path
DATASET_PATH = PROJECT_ROOT / "data" / "PhiUSIIL_Phishing_URL_Dataset.csv"

# Prepared dataset save karne ka path
OUTPUT_PATH = PROJECT_ROOT / "data" / "prepared_dataset.csv"


def main():
    print("Loading original dataset...")

    df = pd.read_csv(DATASET_PATH, low_memory=False)

    print("Extracting URL features...")

    feature_rows = []

    for url in df["URL"]:
        feature_rows.append(extract_features(str(url)))

    features_df = pd.DataFrame(
        feature_rows,
        columns=FEATURE_COLUMNS
    )

    # Original labels ko preserve karna
    features_df["label"] = df["label"].astype(int).values

    # Prepared dataset save karna
    features_df.to_csv(OUTPUT_PATH, index=False)

    print("\nDataset preparation completed!")
    print("Total records:", len(features_df))
    print("Total features:", len(FEATURE_COLUMNS))
    print("Saved to:", OUTPUT_PATH)
    print("\nLabel counts:")
    print(features_df["label"].value_counts())
    print("\nFirst five prepared rows:")
    print(features_df.head().to_string(index=False))


if __name__ == "__main__":
    main()
