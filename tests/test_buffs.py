import unittest

from buffs import *
from constants import KEY_BUFF_TYPE_ARMOR, KEY_BUFF_TYPE_HEALTH, KEY_BUFF_TYPE_MANA, KEY_BUFF_TYPE_STRENGTH


class StatusEffectTests(unittest.TestCase):
    """
    StatusEffect is the base class for buffs
    """
    def test_init(self):
        test_name = 'testman'
        test_duration = 10
        st_ef = StatusEffect(name=test_name, duration=test_duration)

        self.assertEqual(st_ef.name, test_name)
        self.assertEqual(st_ef.duration, test_duration)

    def test_str(self):
        test_name = 'testman'
        test_duration = 10
        st_ef = StatusEffect(name=test_name, duration=test_duration)
        expected_str = "Default Status Effect"

        self.assertEqual(str(st_ef), "Default Status Effect")


class BeneficialBuffTests(unittest.TestCase):
    def test_init(self):
        name = 'BMW'
        stats_amounts = [('strength', 10), ('armor', 20), ('health', 30)]
        duration = 10

        buff = BeneficialBuff(name=name, buff_stats_and_amounts=stats_amounts, duration=duration)

        self.assertEqual(buff.name, name)
        self.assertEqual(buff.buff_stats_and_amounts, stats_amounts)
        self.assertEqual(buff.duration, duration)
        self.assertEqual(buff.buff_amounts, {
            KEY_BUFF_TYPE_MANA: 0,
            KEY_BUFF_TYPE_STRENGTH: 10,
            KEY_BUFF_TYPE_HEALTH: 30,
            KEY_BUFF_TYPE_ARMOR: 20
        })


if __name__ == '__main__':
    unittest.main()
