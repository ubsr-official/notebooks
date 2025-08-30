import os
import json

EXCLUDED_ROOT_FILES = {
    "autocommit.ps1",
    "tree.py",
    "fmtree.py",
    "index.html",
    "favicon.png",
    "fallback.html",
    "Checklist.md"
}

def sort_tree_items(tree):
    """Sort tree items by name in ascending order, with folders first, then files."""
    return sorted(tree, key=lambda x: (x["type"] == "file", x["name"].lower()))

def sort_tree_items_by_name_only(tree):
    """Sort tree items by name in ascending order (case-insensitive)."""
    return sorted(tree, key=lambda x: x["name"].lower())

def build_tree(path, rel_path="", sort_folders_first=True):
    """
    Build a tree structure from the given path.
    
    Args:
        path: The directory path to scan
        rel_path: The relative path for building file paths
        sort_folders_first: If True, folders appear before files in each directory
    """
    tree = []
    
    # Get and sort directory contents
    for name in sorted(os.listdir(path), key=str.lower):
        if name.startswith('.'):
            continue  # skip hidden files/folders
            
        full_path = os.path.join(path, name)
        rel_file_path = os.path.join(rel_path, name).replace("\\", "/")

        if os.path.isdir(full_path):
            tree.append({
                "type": "folder",
                "name": name,
                "children": build_tree(full_path, rel_file_path, sort_folders_first)
            })
        else:
            if rel_path == "" and name in EXCLUDED_ROOT_FILES:
                continue  # skip root-level exclusions
            tree.append({
                "type": "file",
                "name": name,
                "path": rel_file_path
            })
    
    # Apply final sorting based on preference
    if sort_folders_first:
        return sort_tree_items(tree)
    else:
        return sort_tree_items_by_name_only(tree)

if __name__ == "__main__":
    root_dir = "."  # start from current directory
    
    # Build the tree with folders first (default behavior)
    tree = {
        "type": "folder",
        "name": os.path.basename(os.path.abspath(root_dir)),
        "children": build_tree(root_dir, sort_folders_first=True)
    }
    
    # Write to files.json with proper formatting
    with open("files.json", "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=2, ensure_ascii=False)
    
    print("✓ files.json generated with sorted entries.")
    print("  - Folders appear first, then files")
    print("  - All items sorted alphabetically (case-insensitive)")