"""Handy utilities
"""


def get_numeric_column_names():
    """Returns the numeric column names in the data

    Returns
    -------
    numeric_cols : list
        List of column names for the numeric fields.
    """
    numeric_cols = ['q_OpeningDays',
                    'q_OpeningHours',
                    'q_2017 Average Household Size',
                    'q_2017 Total Households',
                    'q_5th Quint by Total HH',
                    'q_2017 Purchasing Power: Per Capita',
                    'q_Uni by Total Pop',
                    'q_2017 Medical Products: Per Capita']
    return numeric_cols


def get_highly_correlated_column_names():
    """Returns the highly correlated column names in the data

    Returns
    -------
    highly_correlated_cols : list
        List of column names for the highly correlated columns.
    """
    highly_correlated_cols = ['q_2017 HHs: 5th Quintile (68.759 and above)',
                              'q_2017 Total Population',
                              'q_2017 Pop 15+/Edu: University, Fachhochschule',
                              'q_2017 Personal Care: Per Capita',
                              'q_2017 Personal Effects: Per Capita']
    return highly_correlated_cols
