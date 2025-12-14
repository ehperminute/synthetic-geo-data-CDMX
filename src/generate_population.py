"""
generate_population.py
----------------------

Generates a synthetic student population with demographic, socioeconomic,
and geographic attributes. Designed to be portable and reproducible.

This module does NOT rely on real student data.
"""

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker('es_MX')


def generate_students(n_students=100_000, n_semesters=8):
    """Generate synthetic students with demographic and SES attributes."""

    sexes = ['F', 'M']
    modalities = ['Escolarizado', 'Semiescolarizado', 'En Línea']

    data = {
        "student_id": np.arange(1, n_students + 1),
        "sex": np.random.choice(sexes, n_students),
        "age": np.random.normal(19, 1.8, n_students).round().astype(int),
        "ses_index": np.random.normal(0, 1, n_students),  # socioeconomic indicator
        "internet_access": np.random.choice([0, 1], n_students, p=[0.25, 0.75]),
        #"transport_time": np.abs(np.random.normal(40, 12, n_students)).round().astype(int),
        "modality": np.random.choice(modalities, n_students, p=[0.7, 0.2, 0.1])
    }

    df = pd.DataFrame(data)
    df["name"] = [fake.name() for _ in range(n_students)]

    return df


def assign_colonias(df_students, colonias_df):

    df_students["colonia_id"] = np.random.Generator.choice(
        colonias_df["colonia_id"].values,
        size=len(df_students),
        replace=True,
        p=colonias_df["pop_weight"].values
    )

    # now just merge metadata
    df_students = df_students.merge(
        colonias_df,
        on="colonia_id",
        how="left"
    )

    return df_students


if __name__ == "__main__":
    print(generate_students(5))
