import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pyiron_workflow import as_function_node

@as_function_node("dataframe")
def read_csv(filename: str, header: list = [0, 1], decimal: str = ",", delimiter: str = ";"):
    return pd.read_csv(filename, delimiter=delimiter, header=header, decimal=decimal)


@as_function_node("stress", "strain")
def convert_load_to_stress(df, area: float):
    """
    Read in csv file, convert load to stress
    """
    kN_to_N = 0.001  # convert kiloNewton to Newton
    mm2_to_m2 = 1e-6  # convert square millimeters to square meters
    df["Stress"] = df["Load"] * kN_to_N / (area * mm2_to_m2)
    #although it says extensometer elongation, the values are in percent! 
    strain = df["Extensometer elongation"].values.flatten()
    #subtract the offset from the dataset
    stress = df["Stress"].values.flatten()
    strain = strain - strain[0]
    return stress, strain 


@as_function_node("youngs_modulus")
def calculate_youngs_modulus(stress, strain, strain_cutoff: float = 0.2):
    percent_to_fraction = 100  # convert
    MPa_to_GPa = 1 / 1000  # convert MPa to GPa
    arg = np.argsort(np.abs(np.array(strain) - strain_cutoff))[0]
    fit = np.polyfit(strain[:arg], stress[:arg], 1)
    youngs_modulus = fit[0] * percent_to_fraction * MPa_to_GPa
    return youngs_modulus


@as_function_node("plot")
def plot(stress, strain, format="-"):
    fig, ax = plt.subplots()
    ax.plot(strain, stress, format)
    ax.set_xlabel("Strain [%]")
    ax.set_ylabel("Stress [MPa]")
    return fig

