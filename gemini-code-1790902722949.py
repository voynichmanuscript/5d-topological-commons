import numpy as np

def apply_secondary_folding(state_matrix, fold_coefficient=1.618):
    """
    Applies a secondary dimensional fold across the 144-node FSM matrix.
    """
    stabilized_fold = state_matrix * fold_coefficient + np.roll(state_matrix, shift=1, axis=0) * (1 / fold_coefficient)
    return np.tanh(stabilized_fold)