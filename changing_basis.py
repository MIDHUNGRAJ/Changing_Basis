import numpy as np


# Function to check if a basis is valid (linearly independent)
def is_valid_basis(basis_matrix):
    det = np.linalg.det(basis_matrix)
    return not np.isclose(det, 0), det


# ===== My Language (Standard Basis) =====
e1 = np.array([1, 0])
e2 = np.array([0, 1])
standard_basis = np.column_stack((e1, e2))

# ===== Jennifer's Language (New Basis) =====
b1 = np.array([1, 1])
b2 = np.array([1, -1])
jennifer_basis = np.column_stack((b1, b2))

# Check if Jennifer's basis is valid
valid, det_val = is_valid_basis(jennifer_basis)
if not valid:
    raise ValueError(f"Invalid basis: determinant = {det_val}")

# ===== Vector in my language =====
V_mine = np.array([3, 1])

# ===== Change of basis: My -> Jennifer =====
P = jennifer_basis  # Columns = Jennifer's basis vectors in my coords
P_inverse = np.linalg.inv(P)  # Inverse for transformation
V_jennifer = P_inverse @ V_mine  # Coordinates in Jennifer's basis

print("P_inverse:\n", P_inverse)
print("V in Jennifer's coordinates:", V_jennifer)

# ===== Change of basis: Jennifer -> My =====
V_back_to_mine = P @ V_jennifer
print("V back in my coordinates:", V_back_to_mine)

# ===== Extra example: Changing basis via standard basis explicitly =====
# Transform from Jennifer -> My using identity (standard) as intermediate
V_jennifer_again = P_inverse @ standard_basis @ V_mine
print("V in Jennifer's coordinates (via standard basis):", V_jennifer_again)

