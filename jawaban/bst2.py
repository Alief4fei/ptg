import matplotlib.pyplot as plt #install matplotlib caranya di terminal ketik "pip install matplotlib"

class Node:
    def __init__(self, key): #inisiasi node buat bst-nya
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree: #inisiasi bst-nya
    def __init__(self):
        self.root = None

    def insert(self, key): #buat insert data ke bst-nya
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key): #buat insert data ke bst-nya
        if key < current.value: #jika key lebih kecil dari current maka masuk ke kiri
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.value: #jika key lebih besar dari current maka masuk ke kanan
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
        else: #jika key sama dengan current ditulis udah ada
            print(f"Item {key} sudah ada di dalam BST.")

    def search(self, key): #buat cari data di bst-nya
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key): #buat cari data di bst-nya
        if current is None: #jika current kosong maka tidak ada
            return False
        if key == current.value: #jika key sama dengan current maka ada
            return True
        elif key < current.value: #jika key lebih kecil dari current maka cari di kiri
            return self._search_recursive(current.left, key)
        else: #jika key lebih besar dari current maka cari di kanan
            return self._search_recursive(current.right, key)

    def display(self): #buat tampilin bst-nya
        if self.root is None: #jika root kosong
            print("BST kosong.")
            return

        fig, ax = plt.subplots() #buat plot-nya
        ax.set_axis_off()

        def _plot_tree(node, x, y, dx):
            if node: 
                ax.text(x, y, str(node.value), ha='center', va='center', 
                        bbox=dict(facecolor='skyblue', boxstyle='circle'))
                if node.left: 
                    ax.plot([x, x - dx], [y - 0.5, y - 1], color='black')
                    _plot_tree(node.left, x - dx, y - 1, dx / 2)
                if node.right:
                    ax.plot([x, x + dx], [y - 0.5, y - 1], color='black')
                    _plot_tree(node.right, x + dx, y - 1, dx / 2)

        _plot_tree(self.root, 0, 0, 4)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-5, 2)
        plt.show()


bst = BinarySearchTree() #buat bst-nya
items = [2, 3, 5, 1, 10] #ceritanya misal ada list data di soal
for item in items: #buat bst dari data yang ada jadi ngelakukan insert sebanyak data yang ada pake function binarysearchtree insert
    bst.insert(item)

while True:
    print("\n=== MENU BST ===")
    print("1. Tambahkan item")
    print("2. Cari item")
    print("3. Tampilkan visualisasi BST")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        item = int(input("Masukkan item yang ingin ditambahkan: "))
        bst.insert(item)
        print(f"Item {item} berhasil ditambahkan ke BST.")
    elif pilihan == '2':
        item = int(input("Masukkan item yang ingin dicari: "))
        if bst.search(item):
            print(f"Item {item} ditemukan di dalam BST.")
        else:
            print(f"Item {item} tidak ditemukan.")
    elif pilihan == '3':
        bst.display()
    elif pilihan == '4':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
