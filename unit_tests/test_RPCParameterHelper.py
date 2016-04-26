from unittest import TestCase

from broker.APIHelpers import RPCParameterHelper


class TestRPCParameterHelper(TestCase):
    def test_splitParametersShouldReturnAListOfLines(self):
        # try with a well-formed parameter setting
        self.assertEqual(RPCParameterHelper.splitParameters("ElMostrador&ElMostrador"), ['ElMostrador', 'ElMostrador'])
        # try with a bad parameter setting
        self.assertNotEqual(RPCParameterHelper.splitParameters("ElMostradorElMostrador"), ['ElMostrador', 'ElMostrador'])