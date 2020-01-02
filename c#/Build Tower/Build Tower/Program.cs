using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Build_Tower
{
    public class Kata
    {
        public static string[] TowerBuilder(int nFloors)
        {
            if (nFloors < 1)
            {
                return null;
            }
            List<string> towerList = new List<string>();
            int whiteSpace = nFloors - 1;
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < nFloors; i ++)
            {
                sb.Append(string.Concat(Enumerable.Repeat(" ", whiteSpace)));
                sb.Append(string.Concat(Enumerable.Repeat("*", i+1)));
                sb.Append(string.Concat(Enumerable.Repeat("*", i)));
                sb.Append(string.Concat(Enumerable.Repeat(" ", whiteSpace)));
                towerList.Add(sb.ToString());
                sb.Clear();
                whiteSpace -= 1;
            }
            return towerList.ToArray();
        }
        static void Main(string[] args)
        {
            foreach (string s in Kata.TowerBuilder(5))
            {
                Console.WriteLine(s);
            }
            Console.WriteLine(Kata.TowerBuilder(5));
        }
    }
}
