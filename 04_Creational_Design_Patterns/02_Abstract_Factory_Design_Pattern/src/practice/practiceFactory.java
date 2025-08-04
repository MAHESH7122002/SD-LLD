package practice;
public class practiceFactory {
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

    public static class VehicleFactory {
        public Vehicle getVehicleInstance(String vechicleType) throws Exception {

            if (vechicleType == "BMW") {
                return new BMW();
            } else if (vechicleType == "HONDA") {
                return new Honda();
            } else if (vechicleType == "TOYOTA") {
                return new Toyota();
            } else {
                throw new Exception("Invalid vehicle type");
            }

        }
    }

    public static void main(String[] args) {
        VehicleFactory vehicleFactory = new VehicleFactory();
        try {

            Vehicle instance = vehicleFactory.getVehicleInstance("BMW");
            instance.start();
            instance.stop();
        } catch (Exception err) {
            System.out.println(err);
        }

    }
}