using System;
using System.Linq;

namespace Grasshopper___Summation
{
    public static class Kata
    {
        public static int summation(int num)
        {
            return Enumerable.Range(1, num).Sum();
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.summation(8));
        }
    }
}
