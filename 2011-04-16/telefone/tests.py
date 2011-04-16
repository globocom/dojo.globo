import unittest

from telefone import telefone


class TestTelefone(unittest.TestCase):
    def test_hifen_retorna_hifen(self):
        self.assertEquals(telefone("-"), "-")

    def test_zero_retorna_zero(self):
        self.assertEquals(telefone("0"), "0")

    def test_um_retorna_um(self):
        self.assertEquals(telefone("1"), "1")

    def test_a_ou_b_ou_c_retorna_2(self):
        self.assertEquals(telefone("a"), "2")
        self.assertEquals(telefone("b"), "2")
        self.assertEquals(telefone("c"), "2")
    
    def test_d_ou_e_ou_f_retorna_3(self):
        self.assertEquals(telefone("d"), "3")
        self.assertEquals(telefone("e"), "3")
        self.assertEquals(telefone("f"), "3")

    def test_g_ou_h_ou_i_retorna_4(self):
        self.assertEquals(telefone("g"), "4")
        self.assertEquals(telefone("h"), "4")
        self.assertEquals(telefone("i"), "4")
        
    def test_j_ou_k_ou_l_retorna_5(self):
        self.assertEquals(telefone("j"), "5")
        self.assertEquals(telefone("k"), "5")
        self.assertEquals(telefone("l"), "5")

    def test_m_ou_n_ou_o_retorna_6(self):
        self.assertEquals(telefone("m"), "6")
        self.assertEquals(telefone("n"), "6")
        self.assertEquals(telefone("o"), "6")

    def test_p_ou_q_ou_r_ou_s_retorna_7(self):
        self.assertEquals(telefone("p"), "7")
        self.assertEquals(telefone("q"), "7")
        self.assertEquals(telefone("r"), "7")
        self.assertEquals(telefone("s"), "7")

    def test_t_ou_u_ou_v_retorna_8(self):
        self.assertEquals(telefone("t"), "8")
        self.assertEquals(telefone("u"), "8")
        self.assertEquals(telefone("v"), "8")

    def test_w_ou_x_ou_y_ou_z_retorna_9(self):
        self.assertEquals(telefone("w"), "9")
        self.assertEquals(telefone("x"), "9")
        self.assertEquals(telefone("y"), "9")
        self.assertEquals(telefone("z"), "9")

    def test_tralha_levanta_excecao(self):
        self.assertRaises(ValueError, telefone, "#")

    def test_casa_retorna_2272(self):
        self.assertEquals(telefone("casa"), "2272")


unittest.main()
