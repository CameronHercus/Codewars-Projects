using System;
using System.Collections.Generic;

namespace Get_the_Middle_Character
{
    public class Kata
    {
        public static string GetMiddle(string s)
        {
            List<char> charList = new List<char>();
            if (string.IsNullOrEmpty(s) || s.Length == 0)
            {
                return "";
            }
            if (s.Length % 2 ==0)
            {
                charList.Add(s[(s.Length / 2) - 1]);
                charList.Add(s[s.Length / 2]);
            }
            else
            {
                charList.Add(s[(s.Length-1) / 2]);
            }
            return String.Join("", charList.ToArray());
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.GetMiddle("Hello"));
            Console.WriteLine(Kata.GetMiddle(""));
            Console.WriteLine(Kata.GetMiddle("He"));
            Console.WriteLine(Kata.GetMiddle("H"));
        }
    }
}
