public class CompareScores {
    public static int[] compareScores(int[] arrA, int[] arrB) {
        int scoreA = 0;
        int scoreB = 0;

        // Loop through the arrays
        for (int i = 0; i < 3; i++) {
            // Compare values of arrA and arrB
            if (arrA[i] > arrB[i]) {
                scoreA++;
            } else if (arrA[i] < arrB[i]) {
                scoreB++;
            }
        }

        // Create an array to hold scores of arrA and arrB
        int[] scoresArray = {scoreA, scoreB};
        return scoresArray;
    }

    public static void main(String[] args) {
        // Test case 1
        int[] arrA1 = {5, 6, 7};
        int[] arrB1 = {3, 6, 10};
        int[] result1 = compareScores(arrA1, arrB1);
        System.out.println(Arrays.toString(result1));

        // Test case 2
        int[] arrA2 = {17, 28, 30};
        int[] arrB2 = {99, 16, 8};
        int[] result2 = compareScores(arrA2, arrB2);
        System.out.println(Arrays.toString(result2));
    }
}
