import unittest
from unittest.mock import Mock
from kassapaate import Kassapaate, HINTA


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_positiivinen_summa_ladataan_kortille(self):
        kortti = Mock()

        self.kassa.lataa(kortti, 20)

        kortti.lataa.assert_called_once_with(20)

    def test_negatiivista_summaa_ei_ladata_kortille(self):
        kortti = Mock()

        self.kassa.lataa(kortti, -20)

        kortti.lataa.assert_not_called()