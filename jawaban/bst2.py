import matplotlib.pyplot as plt # install matplotlib caranya di terminal ketik "pip install matplotlib"

class Node:
    def __init__(self, key): # inisiasi node buat bst-nya
        self.left = None
        self.right = None
        self.value = key
        self.x = 0
        self.y = 0

class BinarySearchTree:
    def __init__(self): # inisiasi node buat bst-nya
        self.root = None

    def insert(self, key): # buat insert data ke bst-nya
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key): # buat insert data ke bst-nya
        if key < current.value:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.value:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def search(self, key): # buat cari data di bst-nya
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key): # buat cari data di bst-nya
        if current is None:
            return False
        if key == current.value:
            return True
        elif key < current.value:
            return self._search_recursive(current.left, key)
        else:
            return self._search_recursive(current.right, key)

    def _calculate_positions(self, node, level=0, x_offset=0, max_depth=1): # function buat nentuin posisi nodenya
        if node is None:
            return

        self._calculate_positions(node.left, level + 1, x_offset - 2**(max_depth - level - 1), max_depth)
        self._calculate_positions(node.right, level + 1, x_offset + 2**(max_depth - level - 1), max_depth)

        node.x = x_offset
        node.y = -level

    def _plot_tree(self, node, ax): # function buat bikin plotnya
        if node is None:
            return

        if node.left:
            ax.plot([node.x, node.left.x], [node.y, node.left.y], 'k-', lw=1)
            self._plot_tree(node.left, ax)

        if node.right:
            ax.plot([node.x, node.right.x], [node.y, node.right.y], 'k-', lw=1)
            self._plot_tree(node.right, ax)

        ax.text(node.x, node.y, str(node.value), ha='center', va='center', fontsize=10,
                bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='circle'))

    def display(self): # buat tampilin bst-nya
        if self.root is None:
            print("BST kosong.")
            return

        # Hitung depth BST, buat ngitung batas
        def _get_depth(node):
            if node is None:
                return 0
            return max(_get_depth(node.left), _get_depth(node.right)) + 1

        max_depth = _get_depth(self.root)

        # Hitung posisi tiap node
        self._calculate_positions(self.root, max_depth=max_depth)

        # Buat plot (garisnya)
        fig,ax = plt.subplots(figsize=(10, 6))
        self._plot_tree(self.root, ax)

        ax.set_xlim(-2**max_depth, 2**max_depth)
        ax.set_ylim(-max_depth, 1)
        ax.axis('off')
        plt.title('Binary Search Tree')
        plt.show()
    
    def build_from_preorder(self, preorder_list): # buat bikin bst dari preorder list
        def build(preorder, min_val, max_val):
            if not preorder:
                return None
            if preorder[0] < min_val or preorder[0] > max_val:
                return None

            root_val = preorder.pop(0)
            node = Node(root_val)
            node.left = build(preorder, min_val, root_val - 1)
            node.right = build(preorder, root_val + 1, max_val)
            return node

        self.root = build(preorder_list, float('-inf'), float('inf'))
        print("BST berhasil dibuat dari preorder.")

    def clear(self): # buat hapus bst
        self.root = None
        print("BST berhasil dikosongkan.")

# program utamanya
bst = BinarySearchTree()

while True:
    print("\n=== MENU BST ===")
    print("1. Tambahkan item")
    print("2. Cari item")
    print("3. Buat BST dari preorder")
    print("4. Tampilkan visualisasi BST")
    print("5. Kosongkan BST")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        bulk_input = input("Masukkan data (pisahkan dengan spasi jika lebih dari satu): ")
        bulk_list = list(map(int, bulk_input.strip().split()))
        for item in bulk_list:
            if bst.search(item):
                print(f"Item {item} sudah ada di dalam BST, dilewati.")
            else:
                bst.insert(item)
                print(f"Item {item} berhasil ditambahkan ke dalam BST.")
        print("Semua data selesai diproses.")

    elif pilihan == '2':
        item = int(input("Masukkan item yang ingin dicari: "))
        if bst.search(item):
            print(f"Item {item} ditemukan di dalam BST.")
        else:
            print(f"Item {item} tidak ditemukan.")

    elif pilihan == '3':
        preorder_input = input("Masukkan data preorder (pisahkan dengan spasi): ")
        preorder_list = list(map(int, preorder_input.strip().split()))
        bst.build_from_preorder(preorder_list)
        print("BST berhasil dibuat dari preorder.")

    elif pilihan == '4':
        bst.display()
        
    elif pilihan == '5':
        bst.clear()
        
    elif pilihan == '6':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
