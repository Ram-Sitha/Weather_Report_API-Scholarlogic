from etl_pipeline import main as run_etl
from analysis import main as run_analysis


if __name__ == "__main__":
    print("Step 1: Running ETL pipeline...")
    run_etl()

    print("Step 2: Creating graphs and FAQ report...")
    run_analysis()

    print("Project completed successfully.")
