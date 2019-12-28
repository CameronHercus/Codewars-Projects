using System;
using System.Collections.Generic;
using System.Linq;

namespace Categorize_New_Member
{
    public class Kata
    {
        public static IEnumerable<string> OpenOrSenior(int[][] data)
        {
            string[] stringArray = new string[data.Length];
            for (int i = 0; i < data.Length; i++)
            {
                if (data[i][0] >= 55 && data[i][1] > 7)
                {
                    stringArray[i] = "Senior";
                } 
                else
                {
                    stringArray[i] = "Open";
                }
            }
            return stringArray;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.OpenOrSenior(new[] { new[] { 45, 12 }, new[] { 55, 21 }, new[] { 19, 2 }, new[] { 104, 20 } }));
        }
    }
}
