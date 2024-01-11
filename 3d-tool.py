import sys
import numpy as np
import trimesh

def load_mesh(file_path):
    # Load the mesh (either OBJ or STL) using trimesh
    return trimesh.load(file_path, process=False)

def save_mesh(mesh, file_path):
    # Save the mesh to a file (preserving the format)
    mesh.export(file_path)

def translate(mesh, translation):
    # Translate the mesh
    mesh.apply_translation(translation)
    return mesh

def rotate(mesh, angles):
    # Rotate the mesh (angles in degrees)
    rotation_matrix = trimesh.transformations.euler_matrix(np.radians(angles[0]), np.radians(angles[1]), np.radians(angles[2]))
    mesh.apply_transform(rotation_matrix)
    return mesh

def scale(mesh, factors):
    # Scale the mesh
    mesh.apply_scale(factors)
    return mesh

def stats(mesh):
    # Calculate and return the min and max coordinates in each dimension
    return np.min(mesh.vertices, axis=0), np.max(mesh.vertices, axis=0)

def main():
    if len(sys.argv) < 3:
        print("Usage: 3d-tool <operation> <file> [options]")
        sys.exit(1)

    operation = sys.argv[1]
    file_path = sys.argv[2]

    mesh = load_mesh(file_path)

    if operation == "stats":
        min_vals, max_vals = stats(mesh)
        print("Min:", min_vals)
        print("Max:", max_vals)
    elif operation == "translate":
        if len(sys.argv) != 4:
            print("Usage: 3d-tool translate <x,y,z> <file>")
            sys.exit(1)
        translation = tuple(map(float, sys.argv[3].split(',')))
        mesh = translate(mesh, translation)
    elif operation == "rotate":
        if len(sys.argv) != 4:
            print("Usage: 3d-tool rotate <x,y,z> <file>")
            sys.exit(1)
        angles = tuple(map(float, sys.argv[3].split(',')))
        mesh = rotate(mesh, angles)
    elif operation == "scale":
        if len(sys.argv) != 4:
            print("Usage: 3d-tool scale <x,y,z> <file>")
            sys.exit(1)
        factors = tuple(map(float, sys.argv[3].split(',')))
        mesh = scale(mesh, factors)
    else:
        print("Invalid operation. Supported operations: stats, translate, rotate, scale")
        sys.exit(1)

    # For operations other than stats, save the modified mesh
    if operation != "stats":
        save_mesh(mesh, "modified_" + file_path)

if __name__ == "__main__":
    main()