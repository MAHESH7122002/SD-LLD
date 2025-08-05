package practice;
public class practice {
    public interface Vehicle {
        public void start();

        public void stop();
    }

    public static class BMW implements Vehicle {

        public void start() {
            System.out.println("BMW started...");
        }

        public void stop() {
            System.out.println("BMW stopped");
        }

    }

    public static class Honda implements Vehicle {
        public void start() {
            System.out.println("Honda Started...");
        }

        public void stop() {
            System.out.println("Honda Stopped.");
        }
    }

    public static class Toyota implements Vehicle {
        public void start() {
            System.out.println("Toyota Started...");
        }

        public void stop() {
            System.out.println("TOyota stopped.");
        }
    }

    

    public static void main(String[] args) {
        BMW bmw = new BMW();
        bmw.start();
        bmw.stop();
        Honda honda = new Honda();
        honda.start();
        honda.stop();
    }
}