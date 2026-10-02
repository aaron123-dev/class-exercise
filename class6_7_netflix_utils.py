import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    logger.debug(f"Showing overview -- {df.shape}")
    print(f"Shape", {df.shape})
    print(f"Fist five:")
    print(df.head())
    print(df.columns)
    print("Data types:")
    print(df.dtypes)




    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    


def remove_duplicates(df):

    """Remove exact duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    logger.debug(f"{before - len(df)} duplicates removed")
    return df


    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    

def drop_missing_rows(df):
    """Remove rows containing missing values."""
    before = len(df)
    df = df.dropna()
    logger.debug(f"Missing values{before - len(df)} rows removed")
    return df
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    