using NUnit.Framework;
using System;
using System.Collections.Generic;

namespace Your_order__please
{
    public static class Kata
    {

        public static string Order(string words)
        {
            string[] wordsArray = words.Split(" ");
            string[] stringsArray = new String[wordsArray.Length];
            foreach (string i in wordsArray)
            {
                foreach (char j in i)
                {
                    if (Char.IsDigit(j))
                    {
                        stringsArray[((int)Char.GetNumericValue(j)) - 1] = i;
                    }
                }
            }
            return string.Join(" ", stringsArray);
        }
        static void Main(string[] args)
        {
            Assert.AreEqual("Thi1s is2 3a T4est", Kata.Order("is2 Thi1s T4est 3a"));
        }
    }
}
