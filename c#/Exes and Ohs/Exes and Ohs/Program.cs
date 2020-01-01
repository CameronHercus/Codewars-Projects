using System;

namespace Exes_and_Ohs
{
    public static class Kata
    {
        public static bool XO(string input)
        {
            int oCounter = 0;
            int xCounter = 0;
            foreach (char s in input)
            {
                if (s == 'x' || s =='X') {
                    xCounter += 1;
                }
                else if (s == 'o' || s == 'O')
                {
                    oCounter += 1;
                }
            }
            if (oCounter == xCounter)
            {
                return true;
            }
            return false;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.XO("xxOo"));
        }
    }
}
