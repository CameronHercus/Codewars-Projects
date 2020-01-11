public class ReverseWords {
    public static String reverseWords(final String original)
    {
        String[] words = original.split(" ");
        StringBuilder reverseString = new StringBuilder();
        for (String i: words) {
            reverseString.append(new StringBuilder(i).reverse().toString() + " ");
        }
        return reverseString.toString().trim();
    }
    public static void main(String[] args) {
        System.out.println(reverseWords("This is an example!"));

    }
}
