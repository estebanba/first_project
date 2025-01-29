from matplotlib import pyplot as plt
import dictionaries

def region_mapping(df):

    country_to_region = {country: region for region, countries in dictionaries.regions.items() for country in countries}

    # Add a 'region' column to the DataFrame
    df['region'] = df['country'].map(country_to_region)
    # Drop unnecessary columns
    # df_cleaned = df.drop(columns=['last_online_purchase', 'grouped_individuals'])

    # Group by region and calculate the mean for each year
    # df_grouped = df.groupby('region').mean(numeric_only=True)

    # Convert the index (years) to integers for proper plotting
    # df_grouped.index = df_grouped.index.astype(int)

    return df

def plot_line_chart(df, xlabel, ylabel, title, legend_title):
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