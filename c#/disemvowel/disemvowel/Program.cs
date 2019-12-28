using System;
using System.Collections.Generic;

namespace disemvowel
{
    public static class Kata
    {
        public static string Disemvowel(string str)
        {
            List<char> disemvowelStr = new List<char>();
            var vowelsDict = new Dictionary<char, int>()
        {
             { 'a', 1},
            { 'e', 2},
            { 'i', 3},
            { 'o', 4},
            { 'u', 5},
            { 'A', 6},
            { 'E', 7},
            { 'I', 8},
            { 'O', 9},
            { 'U', 10},
        };
            foreach (char i in str)
            {
                if (!vowelsDict.ContainsKey(i))
                {
                    disemvowelStr.Add(i);
                }
            }
            return String.Join("", disemvowelStr.ToArray());
        }
    }
}
