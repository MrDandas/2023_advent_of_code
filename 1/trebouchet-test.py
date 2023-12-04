import unittest
import trebouchet

class MyTestCase(unittest.TestCase):

    def test_complete(self):
        content = [
            (['one'], 0, 11),
            (['12'], 12, 12),
            (['asdasfg7ghedsfrtbhse2b'], 72, 72),
            (['1a2'], 12, 12),
            (['d6'], 66, 66),
            (['1a'], 11, 11),
            (['4kthx2'], 42, 42),
            (['xxxx5'], 55, 55),
            (['14xtwoxfive'], 14, 15),
            (['onefjdsngflkjawf52'], 52, 12),
            (['ktjvrmdjf27five8one'], 28, 21),
            (['94gkvkghfjqpsix'], 94, 96),
            (['4gzstfpbqblqkxqrvd'], 44, 44),
            (['eight1nine'], 11, 89),
            (['8zgpptkqjdglpkssbpgzmn85'], 85, 85),
            (['sixpmfjrdmcj76'], 76, 66),
            (['11234easdasfg1ghedsfivebhse2b531'], 11, 11),
            (['six97'], 97, 67),
            (['three8rjm2'], 82, 32),
            (['88424four1'], 81, 81),
            (['jkgmcm7four63three'], 73, 73),
            (['9twotwo3'], 93, 93),
            (['skzzsfvhnine5dgzvdz'], 55, 95),
            (['eight71l1gthree'], 71, 83),
            (['11234easdasfg1ghedsfrtbhse2b531', 'vadfjdsfourlkjawf12', '22bib5bioub6bnf19\n'], 11+12+29, 11+42+29)
        ]

        for i in content:
            print(f'+++ Testing Tuple: {i} +++')
            self.assertEqual(i[1], trebouchet.Trebouchet.solve(i[0], trebouchet.Part.ONE), f'input value [{i[0]}] was not calculated correctly')
            self.assertEqual(i[2], trebouchet.Trebouchet.solve(i[0], trebouchet.Part.TWO), f'input value [{i[0]}] was not calculated correctly')
            print(f' -- -- -- -- -- -- -- -- -- -- -- -- -- -- --\n')
if __name__ == '__main__':
    unittest.main()
