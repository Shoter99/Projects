import java.util.Scanner;

public class Hanoi {
    public static void hanoiTower(int towerSize, int startingPoint, int finishingPoint) {
        if (towerSize == 1) {
            System.out.println("Move from " + startingPoint + " to " + finishingPoint+"\n");
        } else {
            int temporaryPoint = 6 - startingPoint - finishingPoint;
            hanoiTower(towerSize - 1, startingPoint, temporaryPoint);
            System.out.println("Move form " + startingPoint + " to " + finishingPoint+"\n");
            hanoiTower(towerSize - 1, temporaryPoint, finishingPoint);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Type the size of tower: ");
        int size = scanner.nextInt();
        hanoiTower(size, 1, 2);
    }
}