# Membuat Logic untuk visualisasi Streamlit 
import networkx as nx
class Graf:
# Membuat class Graf untuk menyimpan data graf dan melakukan operasi pada graf
# init untuk inisialisasi graf
    def __init__(self):
        self.graph = nx.Graph()
    
    # Fungsi untuk menambahkan vertex ke dalam graf
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.add_node(vertex)
            return True
        return False
        
    # Fungsi untuk menambahkan edge ke dalam graf dengan bobot tertentu
    def add_edge(self, v1, v2, w):
        if self.graph.has_node(v1) and self.graph.has_node(v2):
            self.graph.add_edge(v1, v2, weight=w)
            return True
        return False
    
    # Fungsi untuk mendapatkan graf
    def get_graph(self):
        return self.graph
    
    # Fungsi untuk mendapatkan semua vertex dan edge dalam graf
    def get_all_vertex(self):
        return self.graph.nodes()
    
    # Fungsi untuk mendapatkan semua edge dalam graf
    def get_all_edges(self):
        return self.graph.edges()
    
    # Fungsi untuk mendapatkan semua vertex dan edge dengan bobot dalam graf
    def get_all_vertex_with_weight(self):
        return self.graph.edges(data=True)
    
    # Fungsi untuk mendapatkan semua edge dengan bobot dalam graf
    def get_all_edges_with_weight(self):
        return self.graph.edges(data=True)