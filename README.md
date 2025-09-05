
# DSA_Unlocked

A curated collection of **Data Structures & Algorithms** implementations and notes.  
This repository is my personal learning playlist and reference for interviews.

---

## 📂 Repository Structure

| Folder | Description |
|--------|-------------|
| [arrays](./arrays) | Problems & solutions related to arrays |
| [linked_lists](./linked_lists) | Implementations and practice of linked lists |
| [trees](./trees) | Tree data structures and traversal algorithms |
| [stacks](./stacks) | Stack implementations and related problems |
| [queues](./queues) | Queue and priority queue problems |
| [graphs](./graphs) | Graph algorithms (BFS, DFS, Dijkstra, etc.) |

*(Add or modify rows above to match your actual folder names)*

---

## ⚙️ Environment Setup (Conda)

This project uses a dedicated **Conda environment** to keep dependencies isolated.

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/DSA_Unlocked.git
   cd DSA_Unlocked

2. **Create and activate a Conda environment**

    conda create -n Dsa python=3.10
    conda activate Dsa   

3. **Install Jupyter and ipykernel inside the environment**
    pip install jupyter ipykernel

4. **Add the environment as a Jupyter kernel**
    python -m ipykernel install --user --name=Dsa --display-name "Python (Dsa)"

5. **Contributing & Git Workflow**
    git add .
    git commit -m "Describe your changes"
    git push origin main

