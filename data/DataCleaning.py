import pandas as pd

def clean_data(csv):
    df = pd.read_csv(csv, low_memory=False)
    # Clean column names more thoroughly
    df.columns = df.columns.str.replace('*', '', regex=False)
    df.columns = df.columns.str.replace('#', 'Num', regex=False)
    
    # Remove content in parentheses (like "(e.g.road,drive,lane,etc.)")
    df.columns = df.columns.str.replace(r'\([^)]*\)', '', regex=True)
    
    # Replace spaces and special characters with underscores
    df.columns = df.columns.str.replace(r'[^\w]', '_', regex=True)
    
    # Remove multiple consecutive underscores
    df.columns = df.columns.str.replace(r'_+', '_', regex=True)
    
    # Remove leading/trailing underscores
    df.columns = df.columns.str.strip('_')
    
    # Convert to title case for better readability
    df.columns = df.columns.str.title()
    
    # Handle specific problematic columns with custom names
    column_mapping = {
        'Objectid': 'ObjectID',
        'Streetnumber': 'StreetNumber',
        'Streetname': 'StreetName',
        'Streettype': 'StreetType',
        'Streetsuffix': 'StreetSuffix',
        'Zipcode': 'ZipCode',
        'Calfireunit': 'CALFIREUnit',
        'Incidentname': 'IncidentName',
        'Incidentnumber': 'IncidentNumber',
        'Incidentstartdate': 'IncidentStartDate',
        'Ifaffected1_9_Wheredidfirestart': 'Fire_Start_Location',
        'Ifaffected1_9_Whatstartedfire': 'Fire_Start_Cause',
        'Structuretype': 'StructureType',
        'Structurecategory': 'StructureCategory',
        'Roofconstruction': 'RoofConstruction',
        'Ventscreen': 'VentScreen',
        'Exteriorsiding': 'ExteriorSiding',
        'Windowpane': 'WindowPane',
        'Deck_Porchongrade': 'Deck_Porch_OnGrade',
        'Deck_Porchelevated': 'Deck_Porch_Elevated',
        'Patiocover_Carportattachedtostructure': 'Patio_Carport_Attached',
        'Fenceattachedtostructure': 'Fence_Attached',
        'Firename': 'FireName_Secondary',
        'Apn': 'APN_Parcel',
        'Assessedimprovedvalue': 'Assessed_Value',
        'Yearbuilt': 'Year_Built',
        'Siteaddress': 'Site_Address'
    }
    
    df.rename(columns=column_mapping, inplace=True)
    
    # Convert ObjectID column to category data type
    df["ObjectID"] = df["ObjectID"].astype("category")
    
    # Convert ZipCode column to category data type (if it exists)
    if "ZipCode" in df.columns:
        df["ZipCode"] = df["ZipCode"].astype("category")
    
    # Convert IncidentStartDate to datetime (if it exists)
    if 'IncidentStartDate' in df.columns:
        df['IncidentStartDate'] = pd.to_datetime(df['IncidentStartDate'], 
                                                format='mixed', 
                                                errors='coerce')

    # Select all columns of type 'object'
    object_columns = df.select_dtypes(['object']).columns
    
    # Convert object columns to category
    for column in object_columns:
        df[column] = df[column].astype('category')
    
    # List of columns to drop
    columns_to_drop = [
    'Hazard_Type',
    'Num_Units_In_Structure',
    'Num_Of_Damaged_Outbuildings_120_Sqft',
    'Num_Of_Non_Damaged_Outbuildings_120_Sqft',
    'Distance_Residence_To_Utility_Misc_Structure_Gt_120_Sqft',
    'Globalid',
    'X',
    'Y'
    ]
    
    df = df.drop(columns=columns_to_drop)

    # Return the cleaned dataframe
    return df

# Assign the return value to a variable
df = clean_data('Wildfire Property Damage.csv')
print("Column names after cleaning:")
print(list(df.columns))
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:\n{df.head()}")
df.to_csv("CleanPropertyRecords.csv")