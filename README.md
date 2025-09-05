
# DSA_Unlocked

A curated collection of **Data Structures & Algorithms** implementations and notes.  
This repository is my personal learning playlist and reference for interviews.

---

## 📂 Repository Structure

| Folder | Description |
|--------|-------------|
| [arrays](./Arrays) | Problems & solutions related to arrays |
| [linked_lists](./Linked_lists) | Implementations and practice of linked lists |
| [trees](./Trees) | Tree data structures and traversal algorithms |
| [Stacks](./Stacks) | Stack implementations and related problems |
| [queues](./Queues) | Queue and priority queue problems |
| [graphs](./Graphs) | Graph algorithms (BFS, DFS, Dijkstra, etc.) |

*(Add or modify rows above to match your actual folder names)*

---

## ⚙️ Environment Setup (Conda)

This project uses a dedicated **Conda environment** to keep dependencies isolated.

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/DSA_Unlocked.git
   cd DSA_Unlocked

2. **Create and activate a Conda environment**
    ```bash
    conda create -n Dsa python=3.10
    conda activate Dsa   

3. **Install Jupyter and ipykernel inside the environment**
    ```bash
    pip install jupyter ipykernel

5. **Add the environment as a Jupyter kernel**
   ```bash
    python -m ipykernel install --user --name=Dsa --display-name "Python (Dsa)"

7. **Contributing & Git Workflow**
    ```bash
    git add .
    git commit -m "Describe your changes"
    git push origin main

