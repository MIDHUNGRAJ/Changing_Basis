# Change of Basis in Linear Algebra with Python

This repository contains a Python script that demonstrates the concept of **change of basis** for vectors using the **NumPy** library.  
It provides a practical, code-based example of how to translate a vector's coordinates from one basis (the standard basis) to another.

---

## 🎥 For Visual Intuition

Before diving into the code, it's highly recommended to watch Grant Sanderson's [3Blue1Brown video](https://youtu.be/P2LTAUO1TdA) on the topic.  
It provides an excellent visual and intuitive explanation of what a change of basis represents.

> **Video:** *Change of Basis | Chapter 13, Essence of Linear Algebra*

---

## 💡 Core Concepts

The script is built around translating between two coordinate systems:

- **Standard Basis:**  
  The familiar Cartesian coordinate system where the basis vectors are:  

  $e_1 = [1, 0], \quad e_2 = [0, 1]$


- **New Basis (Jennifer's Basis):**  
  An alternative coordinate system defined by:  

  $b_1 = [1, 1], \quad b_2 = [1, -1]$


- **Change of Basis Matrix (P):**  
  The matrix whose columns are the new basis vectors, expressed in the old (standard) coordinates.  
  This matrix is the key to translating between the two systems.

---

## ⚙️ How the Code Works

1. **Defines Bases**  
   Sets up the standard basis and the new basis as NumPy arrays.

2. **Checks Validity**  
   Includes a function `is_valid_basis` that calculates the determinant of the new basis matrix.  
   - If the determinant is zero, the vectors are linearly dependent and do not form a valid basis.

3. **Defines a Vector**  
   Creates a sample vector:  
   
   $V_{\text{mine}} = [3, 1]$
   
   in the standard basis.

4. **Transforms Standard -> New**  
   - Calculates the inverse of the change of basis matrix (`P_inverse`).
   - Multiplies this inverse matrix by the vector:
     
     $P_{\text{inverse}} @ V_{\text{mine}}$
     
     to find the coordinates in the new basis.

5. **Transforms New -> Standard**  
   - Multiplies the original change of basis matrix (`P`) by the vector in the new coordinates.
   - This returns the vector to its original coordinates in the standard basis.

---

## 🚀 Usage

1. Install **Python** and **NumPy**:
   ```bash
   pip install numpy
   ```


2. Save the code as a Python file:
   ```python
   change_of_basis.py
   ```

3. Run the script:
   ```python
   python change_of_basis.py
   ```

