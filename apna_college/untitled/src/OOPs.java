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

class Student {
  String name;
  int age;

  public void study(){
    System.out.println(this.name + " is studying");
  }

  public void printAge(){
    System.out.println(this.age);
  }
  public void printName(){
    System.out.println(this.name);
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

  Student student1 = new Student();
  student1.name = "Alice";
  student1.age = 20;

  student1.study();
  student1.printName();
  student1.printAge();

  Student student2 = new Student();
  student2.name = "Bob";
  student2.age = 22;
  
  student2.study();
  student2.printName();
  student2.printAge();
  }
}
