import test.ship.StarShip;

public class FirstTest {

    public static void main(String[] args) {
        //создаем экземпляр класса корабля
        StarShip ship=new StarShip(215.25);
         displayHeight(ship);

    }
    public static void displayHeight(StarShip ship){
        System.out.println("Высота корабля составляет: " + ship.getShipHeight());
    }

}