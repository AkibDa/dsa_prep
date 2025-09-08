class Pen{
  String color;
  String type;

  public void write(){
    System.out.println("Writing something");
  }

  public void printColor(){
    System.out.println(this.color);
  }

  public void printType(){
    System.out.println(this.type);
  }
}


public class OOPs {
  public static void main(String[] args) {
  Pen pen1 = new Pen();
  pen1.color = "Blue";
  pen1.type = "Gel";

  Pen pen2 = new Pen();
  pen2.color = "Black";
  pen2.type = "Ballpoint";

  pen1.write();
  pen1.printColor();
  pen1.printType();

  pen2.write();
  pen2.printColor();
  pen2.printType();
  }
}
