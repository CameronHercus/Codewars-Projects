using System;
using System.Collections.Generic;
using System.Text;

namespace Duplicate_Encoder
{
    public class Kata
    {
        public static string DuplicateEncode(string word)
        {
            string wordLower = word.ToLower();
            Dictionary<char, char> dict = new Dictionary<char, char>();
            StringBuilder myString = new StringBuilder();
            foreach (char c in wordLower)
            {
                if (dict.ContainsKey(c))
                {
                    dict[c] = ')';
                }
                else
                {
                    dict.Add(c, '(');
                }
            }
            foreach (char c in wordLower)
            {
                myString.Append(dict[c]);
            }
            
            return myString.ToString();
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.DuplicateEncode("recede"));
        }
    }
}
