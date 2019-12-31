using System;

namespace Sum_of_two_lowest_positive_integers
{
    public static class Kata
    {
        public static int sumTwoSmallestNumbers(int[] numbers)
        {
            int first = int.MaxValue;
            int second = int.MaxValue;
            foreach (int i in numbers)
            {
                if (i < first)
                {
                    second = first;
                    first = i;
                }
                else if (i < second && i != first)
                {
                    second = i;
                }
            }
            return first + second;
        }
        static void Main(string[] args)
        {
            int[] numbers = { 5, 4, 12, 19, 22 };
            Console.WriteLine(Kata.sumTwoSmallestNumbers(numbers));
        }
    }
}
