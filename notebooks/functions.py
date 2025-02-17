from matplotlib import pyplot as plt
import dictionaries

def region_mapping(df):
    '''
    Adds a new column to the dataframe mapping the country values 
    to the european region where it belongs.
    '''
    country_to_region = {country: region for region, countries in dictionaries.regions.items() for country in countries}
    # Add a 'region' column to the DataFrame
    df['region'] = df['country'].map(country_to_region)

    return df

def plot_line_chart(df, xlabel, ylabel, title, legend_title):
    '''
    Basic line chart
    '''
    plt.figure(figsize=(14, 8))
    for region in df.columns:
        plt.plot(df.index, df[region], marker='o', label=region)

    # Add labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(title=legend_title, bbox_to_anchor=(1.05, 1), loc='upper left')

    # Add grid for better readability
    plt.grid(True)

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()