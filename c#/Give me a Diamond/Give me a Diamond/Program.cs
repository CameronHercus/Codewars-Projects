using System;
using System.Linq;
using System.Text;

namespace Give_me_a_Diamond
{
    public class Diamond
    {
        public static string print(int n)
        {
            if (n % 2 == 0 || n < 0)
            {
                return null;
            }

            StringBuilder sb = new StringBuilder();
            int whitespace = (n - 1) / 2;
            for (int i = 1; i < n; i += 2)
            {
                sb.Append(string.Concat(Enumerable.Repeat(" ", whitespace)));
                sb.Append(string.Concat(Enumerable.Repeat("*", i)));
                sb.Append("\n");
                whitespace -= 1;
            }
            for (int i = n; i >= 1; i -= 2)
            {
                sb.Append(string.Concat(Enumerable.Repeat(" ", whitespace)));
                sb.Append(string.Concat(Enumerable.Repeat("*", i)));
                sb.Append("\n");
                whitespace += 1;
            }
            return sb.ToString();
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Diamond.print(-1));
            Console.WriteLine(Diamond.print(0));
            Console.WriteLine(Diamond.print(5));
            Console.WriteLine(Diamond.print(3));
            Console.WriteLine(Diamond.print(7));
        }
    }
}
