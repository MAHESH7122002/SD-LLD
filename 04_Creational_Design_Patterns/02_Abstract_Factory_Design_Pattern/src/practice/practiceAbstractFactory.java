package practice;

public class practiceAbstractFactory {
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

    public interface VehicleFactory {
        public Vehicle getVehicleInstance();
    }

    public static class BMWFactory implements VehicleFactory {
        public Vehicle getVehicleInstance() {
            return new BMW();
        }
    }

    public static class HondaFactory implements VehicleFactory {
        public Vehicle getVehicleInstance() {
            return new BMW();
        }
    }

    public static class ToyotaFactory implements VehicleFactory {
        public Vehicle getVehicleInstance() {
            return new BMW();
        }
    }


    public static void main(String[] args) {
        try {
            VehicleFactory instanceFactory = new BMWFactory();
            Vehicle instance = instanceFactory.getVehicleInstance();
            instance.start();
            instance.stop();
        } catch (Exception err) {
            System.out.println(err);
        }

    }
}