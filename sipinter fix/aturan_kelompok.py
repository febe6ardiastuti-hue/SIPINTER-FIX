"""aturan_kelompok.py — Aturan Bisnis SIPINTER"""
import unittest

def cek_batas_pinjaman(jumlah_pinjaman_aktif):
    """
    Aturan Bisnis: Satu anggota maksimal hanya boleh memiliki 1 pinjaman aktif.
    """
    BATAS_MAKSIMAL = 1
    
    if type(jumlah_pinjaman_aktif) is not int or jumlah_pinjaman_aktif < 0:
        raise ValueError("Jumlah pinjaman aktif harus berupa bilangan bulat positif atau nol.")
        
    if jumlah_pinjaman_aktif >= BATAS_MAKSIMAL:
        raise ValueError(
            f"Gagal: Anggota masih memiliki {jumlah_pinjaman_aktif} pinjaman aktif. "
            "Harap kembalikan buku sebelumnya terlebih dahulu."
        )
        
    return True


# ==========================================
# D.4 UJI FUNGSINYA (UNIT TEST)
# ==========================================
class UjiBatasPinjaman(unittest.TestCase):
    def test_tidak_ada_pinjaman(self):
        # Diterima: belum punya pinjaman (0)
        self.assertTrue(cek_batas_pinjaman(0))

    def test_sudah_pinjam_ditolak(self):
        # Ditolak: sudah punya 1 pinjaman aktif
        with self.assertRaises(ValueError):
            cek_batas_pinjaman(1)

    def test_input_negatif_ditolak(self):
        # Ditolak: input tidak masuk akal (misal minus)
        with self.assertRaises(ValueError):
            cek_batas_pinjaman(-1)


# ==========================================
# MENJALANKAN PENGUJIAN
# ==========================================
if __name__ == "__main__":
    unittest.main(verbosity=2)
    