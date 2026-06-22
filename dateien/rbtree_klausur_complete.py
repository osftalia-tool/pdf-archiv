# ==============================================================================
# INGENIEURINFORMATIK 3 - RBTREE REPOSITORY (32 FUNCTIONS)
# ==============================================================================
# SCHNELLSUCH-INDEX (Nutze Strg+F für sekundenschnellen Zugriff in der Klausur):
#
# --- KAPITEL 1: DIE TRAVERSIERUNGS-MATRIX (ALLE REIHENFOLGEN × BEIDE VARIANTEN) ---
# [A1]  -> Inorder: Liste von Keys [inorder_keys]
# [A2]  -> Inorder: Callback mit Keys [visit_inorder_keys]
# [A3]  -> Inorder: Callback mit Values [visit_inorder_values]
# [A4]  -> Preorder: Liste von Keys [preorder_keys]
# [A5]  -> Preorder: Liste von Values [get_values_preorder] (Aus dem Ur-PDF)
# [A6]  -> Preorder: Callback mit Keys [visit_preorder_keys]
# [A7]  -> Postorder: Liste von Keys [get_keys_postorder] (Aus dem Ur-PDF)
# [A8]  -> Postorder: Callback mit Keys [visit_post_order] (Aus der Altklausur)
# [A9]  -> Level-Order: Liste von Keys [levelorder_keys]
# [A10] -> Level-Order: Callback mit Keys [visit_level_order] (Aus der Altklausur)
#
# --- KAPITEL 2: METRIKEN, STATISTIKEN & ZÄHLOPERATIONEN ---
# [A11] -> Anzahl aller echten Knoten [count_nodes]
# [A12] -> Anzahl aller echten Blätter [count_leaves]
# [A13] -> Anzahl aller roten Knoten [count_red_nodes]
# [A14] -> Anzahl aller schwarzen Knoten (exkl. NIL) [count_black_nodes]
# [A15] -> Arithmetischer Durchschnitt aller Schlüssel [average_key]
# [A16] -> Summe aller Schlüsselwerte [sum_keys]
#
# --- KAPITEL 3: BAUMTIEFEN & ROT-SCHWARZ-HOCHSPEZIFISCHE METRIKEN ---
# [A17] -> Maximale Baumtiefe / Gesamthöhe [get_max_depth]
# [A18] -> Minimale Baumtiefe [get_min_depth]
# [A19] -> Schwarzhöhe über den LINKEN Pfad [get_black_height] / [get_black_height_left]
# [A20] -> Schwarzhöhe über den RECHTEN Pfad [get_black_height_right]
# [A21] -> Validierung: Haben ALLE Pfade dieselbe Schwarzhöhe? [validate_black_height]
# [A22] -> Rothöhe: Maximale rote Knotenfolge auf einem Pfad [get_max_consecutive_red]
#
# --- KAPITEL 4: SUCH- & INTERVALLOPREATIONEN (MIT FEHLERBEHANDLUNGEN) ---
# [A23] -> Globales Minimum (ValueError bei Leere) [min]
# [A24] -> Globales Maximum (ValueError bei Leere) [max]
# [A25] -> Iterative Elementsuche (KeyError bei Fehlen) [find]
# [A26] -> Intervall-Suche / Werte dazwischen [between]
# [A27] -> Inorder-Nachfolger / Nächstgrößeren Key finden [get_successor]
# [A28] -> Inorder-Vorgänger / Nächstkleineren Key finden [get_predecessor]
# [A29] -> Keys auf einer exakten Ebene sammeln [get_keys_at_level]
#
# --- KAPITEL 5: STRUKTUR-VALIDIERUNG & VERWANDTSCHAFTEN ---
# [A30] -> Rot-Eigenschaft prüfen: Keine zwei roten Knoten in Folge [check_red_property]
# [A31] -> Verwandtschaft: Onkel-Schlüssel eines Keys ermitteln [get_uncle_key]
# [A32] -> Den gesamten Baum leeren / zurücksetzen [clear]
# ==============================================================================

"""
KLAUSUR-HINWEIS: Alle Methoden nutzen 'self._root' und berücksichtigen 'node.is_nil'.
Sie sind so eingerückt, dass sie direkt per Copy-Paste in die Klasse passen.

Für Export: Öffnen der Datei über "Open Folder". In Konsole ./zipUpload.sh eingeben.
"""

# ==============================================================================
# --- KAPITEL 1: DIE TRAVERSIERUNGS-MATRIX ---
# ==============================================================================

    # [A1] Inorder: Liste von Keys
    def inorder_keys(self) -> list:
        def _rec(node, res):
            if node and not node.is_nil:
                _rec(node.left, res)
                res.append(node.key)
                _rec(node.right, res)
        result = []
        _rec(self._root, result)
        return result

    # [A2] Inorder: Callback mit Keys
    def visit_inorder_keys(self, visit) -> None:
        def _rec(node):
            if node and not node.is_nil:
                _rec(node.left)
                visit(node.key)
                _rec(node.right)
        _rec(self._root)

    # [A3] Inorder: Callback mit Values
    def visit_inorder_values(self, visit) -> None:
        def _rec(node):
            if node and not node.is_nil:
                _rec(node.left)
                visit(node.value)
                _rec(node.right)
        _rec(self._root)

    # [A4] Preorder: Liste von Keys
    def preorder_keys(self) -> list:
        def _rec(node, res):
            if node and not node.is_nil:
                res.append(node.key)
                _rec(node.left, res)
                _rec(node.right, res)
        result = []
        _rec(self._root, result)
        return result

    # [A5] Preorder: Liste von Values (Aus Original-PDF)
    def get_values_preorder(self) -> list:
        def _preorder_rec(node, result: list):
            if node and not node.is_nil:
                result.append(node.value)
                _preorder_rec(node.left, result)
                _preorder_rec(node.right, result)
        res = []
        _preorder_rec(self._root, res)
        return res

    # [A6] Preorder: Callback mit Keys
    def visit_preorder_keys(self, visit) -> None:
        def _rec(node):
            if node and not node.is_nil:
                visit(node.key)
                _rec(node.left)
                _rec(node.right)
        _rec(self._root)

    # [A7] Postorder: Liste von Keys (Aus Original-PDF)
    def get_keys_postorder(self) -> list:
        def _postorder_rec(node, result: list):
            if node and not node.is_nil:
                _postorder_rec(node.left, result)
                _postorder_rec(node.right, result)
                result.append(node.key)
        res = []
        _postorder_rec(self._root, res)
        return res

    # [A8] Postorder: Callback mit Keys (Aus Altklausur)
    def visit_post_order(self, visit) -> None:
        def _post_order_rec(node):
            if node and not node.is_nil:
                _post_order_rec(node.left)
                _post_order_rec(node.right)
                visit(node.key)
        _post_order_rec(self._root)

    # [A9] Level-Order: Liste von Keys
    def levelorder_keys(self) -> list:
        if self._root.is_nil:
            return []
        result, queue = [], [self._root]
        while queue:
            curr = queue.pop(0)
            result.append(curr.key)
            if curr.left and not curr.left.is_nil:
                queue.append(curr.left)
            if curr.right and not curr.right.is_nil:
                queue.append(curr.right)
        return result

    # [A10] Level-Order: Callback mit Keys (Aus Altklausur)
    def visit_level_order(self, visit) -> None:
        if self._root.is_nil:
            return
        queue = [self._root]
        while len(queue) > 0:
            current = queue.pop(0)
            visit(current.key)
            if current.left and not current.left.is_nil:
                queue.append(current.left)
            if current.right and not current.right.is_nil:
                queue.append(current.right)


# ==============================================================================
# --- KAPITEL 2: METRIKEN, STATISTIKEN & ZÄHLOPERATIONEN ---
# ==============================================================================

    # [A11] Anzahl aller echten Knoten
    def count_nodes(self) -> int:
        def _count_rec(node):
            if not node or node.is_nil:
                return 0
            return 1 + _count_rec(node.left) + _count_rec(node.right)
        return _count_rec(self._root)

    # [A12] Anzahl aller echten Blätter
    def count_leaves(self) -> int:
        def _count_rec(node) -> int:
            if not node or node.is_nil:
                return 0
            if (not node.left or node.left.is_nil) and (not node.right or node.right.is_nil):
                return 1
            return _count_rec(node.left) + _count_rec(node.right)
        return _count_rec(self._root)

    # [A13] Anzahl aller roten Knoten
    def count_red_nodes(self) -> int:
        def _rec(node) -> int:
            if not node or node.is_nil:
                return 0
            curr = 1 if not node.is_black else 0
            return curr + _rec(node.left) + _rec(node.right)
        return _rec(self._root)

    # [A14] Anzahl aller schwarzen Knoten (exklusive NIL)
    def count_black_nodes(self) -> int:
        def _rec(node) -> int:
            if not node or node.is_nil:
                return 0
            curr = 1 if node.is_black else 0
            return curr + _rec(node.left) + _rec(node.right)
        return _rec(self._root)

    # [A15] Arithmetischer Durchschnitt aller Schlüssel
    def average_key(self) -> float:
        keys = self.inorder_keys()
        if not keys:
            return 0.0
        return sum(keys) / len(keys)

    # [A16] Summe aller Schlüsselwerte
    def sum_keys(self) -> int:
        return sum(self.inorder_keys())


# ==============================================================================
# --- KAPITEL 3: BAUMTIEFEN & ROT-SCHWARZ-HOCHSPEZIFISCHE METRIKEN ---
# ==============================================================================

    # [A17] Maximale Baumtiefe / Gesamthöhe
    def get_max_depth(self) -> int:
        def _depth_rec(node) -> int:
            if not node or node.is_nil:
                return 0
            return 1 + max(_depth_rec(node.left), _depth_rec(node.right))
        return _depth_rec(self._root)

    # [A18] Minimale Baumtiefe (Kürzester Pfad zu einem NIL-Blatt)
    def get_min_depth(self) -> int:
        def _rec(node) -> int:
            if not node or node.is_nil:
                return 0
            return 1 + min(_rec(node.left), _rec(node.right))
        return _rec(self._root)

    # [A19] Schwarzhöhe über den LINKEN Pfad
    def get_black_height(self) -> int:
        height = 0
        current = self._root
        while current is not None:
            if current.is_black:
                height += 1
            if current.is_nil:
                break
            current = current.left
        return height

    # [A20] Schwarzhöhe über den RECHTEN Pfad
    def get_black_height_right(self) -> int:
        height = 0
        current = self._root
        while current is not None:
            if current.is_black:
                height += 1
            if current.is_nil:
                break
            current = current.right
        return height

    # [A21] Validierung: Haben ALLE Pfade dieselbe Schwarzhöhe?
    def validate_black_height(self) -> bool:
        def _check(node):
            if not node or node.is_nil:
                return 1 # Ein NIL-Blatt ist schwarz und zählt als 1
            left_h = _check(node.left)
            right_h = _check(node.right)
            if left_h == -1 or right_h == -1 or left_h != right_h:
                return -1
            return left_h + (1 if node.is_black else 0)
        return _check(self._root) != -1

    # [A22] Rothöhe: Maximale aufeinanderfolgende rote Knoten auf einem Pfad
    def get_max_consecutive_red(self) -> int:
        def _rec(node, current_run):
            if not node or node.is_nil:
                return current_run
            if not node.is_black:
                current_run += 1
            else:
                current_run = 0
            return max(current_run, _rec(node.left, current_run), _rec(node.right, current_run))
        return _rec(self._root, 0)


# ==============================================================================
# --- KAPITEL 4: SUCH- & INTERVALLOPREATIONEN ---
# ==============================================================================

    # [A23] Globales Minimum
    def min(self) -> int:
        if self._root.is_nil:
            raise ValueError("Der Baum ist leer.")
        current = self._root
        while current.left and not current.left.is_nil:
            current = current.left
        return current.key

    # [A24] Globales Maximum
    def max(self) -> int:
        if self._root.is_nil:
            raise ValueError("Der Baum ist leer.")
        current = self._root
        while current.right and not current.right.is_nil:
            current = current.right
        return current.key

    # [A25] Iterative Elementsuche mit exakter Altklausur-Fehlerbehandlung
    def find(self, key: int) -> any:
        current = self._root
        while current and not current.is_nil:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        raise KeyError(f"Key {key} wurde nicht im Baum gefunden.")

    # [A26] Intervall-Suche / Werte dazwischen [low, high]
    def between(self, low: int, high: int) -> list:
        result = []
        def _between_rec(node):
            if not node or node.is_nil:
                return
            if node.key > low:
                _between_rec(node.left)
            if low <= node.key <= high:
                result.append(node.key)
            if node.key < high:
                _between_rec(node.right)
        _between_rec(self._root)
        return result

    # [A27] Symmetrischen Inorder-Nachfolger (Successor) finden
    def get_successor(self, key: int) -> any:
        current = self._root
        successor = None
        while current and not current.is_nil:
            if key < current.key:
                successor = current
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                if current.right and not current.right.is_nil:
                    curr_right = current.right
                    while curr_right.left and not curr_right.left.is_nil:
                        curr_right = curr_right.left
                    return curr_right.key
                break
        return successor.key if successor else None

    # [A28] Symmetrischen Inorder-Vorgänger (Predecessor) finden
    def get_predecessor(self, key: int) -> any:
        current = self._root
        predecessor = None
        while current and not current.is_nil:
            if key < current.key:
                current = current.left
            elif key > current.key:
                predecessor = current
                current = current.right
            else:
                if current.left and not current.left.is_nil:
                    curr_left = current.left
                    while curr_left.right and not curr_left.right.is_nil:
                        curr_left = curr_left.right
                    return curr_left.key
                break
        return predecessor.key if predecessor else None

    # [A29] Schlüssel auf einer exakten Ebene sammeln
    def get_keys_at_level(self, target_level: int) -> list:
        result = []
        def _collect_level_rec(node, current_level):
            if not node or node.is_nil:
                return
            if current_level == target_level:
                result.append(node.key)
                return
            if current_level < target_level:
                _collect_level_rec(node.left, current_level + 1)
                _collect_level_rec(node.right, current_level + 1)
        _collect_level_rec(self._root, 0)
        return result


# ==============================================================================
# --- KAPITEL 5: STRUKTUR-VALIDIERUNG & VERWANDTSCHAFTEN ---
# ==============================================================================

    # [A30] Rot-Schwarz-Eigenschaft prüfen (Red-Property)
    def check_red_property(self) -> bool:
        def _check_rec(node) -> bool:
            if not node or node.is_nil:
                return True
            if not node.is_black:
                if node.left and not node.left.is_nil and not node.left.is_black:
                    return False
                if node.right and not node.right.is_nil and not node.right.is_black:
                    return False
            return _check_rec(node.left) and _check_rec(node.right)
        return _check_rec(self._root)

    # [A31] Struktur-Hilfe: Onkel-Schlüssel eines Keys ermitteln
    def get_uncle_key(self, key: int) -> any:
        current = self._root
        parent = None
        grandparent = None
        while current and not current.is_nil and current.key != key:
            grandparent = parent
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        if not current or current.is_nil or not parent or not grandparent:
            return None
        if grandparent.left == parent:
            uncle = grandparent.right
        else:
            uncle = grandparent.left
        return uncle.key if uncle and not uncle.is_nil else None

    # [A32] Den gesamten Baum leeren / zurücksetzen
    def clear(self) -> None:
        self._root = RBTreeNode.nil()
