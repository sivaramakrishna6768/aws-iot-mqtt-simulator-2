# AWS IoT MQTT Sensor Simulator

This project simulates an environmental IoT device that securely publishes sensor data (temperature, humidity, and CO2 levels) to AWS IoT Core using MQTT. The data is routed via an IoT Rule to an Amazon Kinesis Firehose stream and stored in Amazon S3 in JSON format.

---

## 📦 Features

- Simulates temperature, humidity, and CO2 values.
- Publishes data to AWS IoT Core over TLS-secured MQTT.
- Uses AWS IoT Rules to route messages.
- Streams real-time data into an S3 bucket via Kinesis Firehose.
- Stores sensor data in S3 as structured JSON.

---

## 🔧 Technologies Used

- **Python 3**
- **paho-mqtt**
- **AWS IoT Core**
- **Amazon Kinesis Firehose**
- **Amazon S3**

---

## 📁 Project Structure

```
InClass_Week10/
├── mqtt_aws_simulator.py           # Python script for data simulation and MQTT publishing
├── AmazonRootCA1.pem               # Root CA certificate from AWS
├── device-certificate.pem.crt     # Device certificate (downloaded from AWS IoT)
├── private.pem.key                 # Private key (downloaded from AWS IoT)
└── README.md                       # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sivaramakrishna6768/aws-iot-mqtt-simulator-2
cd aws-iot-mqtt-simulator-2
```

---

### 2. AWS IoT Core Setup

- Create a Thing in AWS IoT Core.
- Generate and download:
  - Device certificate (`*.pem.crt`)
  - Private key (`*.pem.key`)
  - AmazonRootCA1.pem
- Note your AWS IoT **endpoint URL** from the **Settings** tab.

---

### 3. Python Environment Setup

Install the required library:

```bash
pip install paho-mqtt
```

Update `mqtt_aws_simulator.py` with:
- Your AWS IoT endpoint
- Correct file paths to your certificate, key, and root CA

Example:
```python
awshost = "your-iot-endpoint.amazonaws.com"
caPath = "AmazonRootCA1.pem"
certPath = "device-certificate.pem.crt"
keyPath = "private.pem.key"
```

Then run:
```bash
python mqtt_aws_simulator.py
```

---

## 🛰️ MQTT Topic Used

```
update/environment/dht1
```

---

## 🔁 AWS Cloud Pipeline

1. **Create a Kinesis Firehose Delivery Stream**
   - Source: Direct PUT
   - Destination: Amazon S3
   - Prefix: `iot_data/`
   - IAM Role: Auto-created or assigned

2. **Create an AWS IoT Rule**
   - SQL Query:
     ```sql
     SELECT * FROM 'update/environment/dht1'
     ```
   - Action: Send message to Kinesis Firehose stream
   - IAM Role: Auto-generated with Firehose access

3. **Verify Delivery in S3**
   - Navigate to your S3 bucket.
   - Explore folders like `iot_data/YYYY/MM/DD/HH/`.
   - Download and open `.json` or `.gz` files for stored data.

---

## ✅ Example Output

```json
{
  "thingid": "dht1",
  "temperature": 25,
  "humidity": 45,
  "co2": 850,
  "datetime": "2025-04-04T21:23:12Z"
}
```

## 👤 Author

**Venkata Sri Siva Ramakrishna Palaparthy**  
