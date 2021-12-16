import os
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.table import StreamTableEnvironment, DataTypes, EnvironmentSettings
from pyflink.table.descriptors import Schema, Kafka, Json
from pyflink.table.window import Tumble
from datetime import datetime, date, time


def from_kafka_to_kafka_demo():
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
    s_env.set_parallelism(1)

    # use blink table planner
    st_env = StreamTableEnvironment \
        .create(s_env, environment_settings=EnvironmentSettings
                .new_instance()
                .in_streaming_mode()
                .use_blink_planner().build())

    # register source and sink
    register_syslogs_source(st_env)
    register_syslogs_sink(st_env)

    # query
    st_env.from_path("syslog_source").insert_into("syslog_output")

    # execute
    st_env.execute("2-from_kafka_to_kafka")


def register_syslogs_source(st_env):
    st_env \
        .connect(  # declare the external system to connect to (in this case rhe local standalone kafka broker)
        Kafka()
            .version("universal")
            .topic(os.getenv("KAFKA_INPUT_TOPIC"))
            .start_from_earliest()
            .property("zookeeper.connect", os.getenv("KAFKA_ZOOKEEPER_CONNECT"))
            .property("bootstrap.servers", os.getenv("KAFKA_BOOTSTRAP_SERVER"))) \
        .with_format(  # declare a format for this system
        Json()
            .fail_on_missing_field(False)
            .schema(DataTypes.ROW([
            DataTypes.FIELD("time", DataTypes.TIMESTAMP()),
            DataTypes.FIELD("devname", DataTypes.STRING()),
            DataTypes.FIELD("type", DataTypes.STRING()),
            DataTypes.FIELD("srcport", DataTypes.INT()),
            DataTypes.FIELD("dstport", DataTypes.INT()),
            DataTypes.FIELD("service", DataTypes.STRING()),
            DataTypes.FIELD("action", DataTypes.STRING()),
            DataTypes.FIELD("crlevel", DataTypes.STRING()),
            DataTypes.FIELD("srcip", DataTypes.STRING()),
            DataTypes.FIELD("dstip", DataTypes.STRING()),
            DataTypes.FIELD("srccountry", DataTypes.STRING()),
            DataTypes.FIELD("dstcountry", DataTypes.STRING()),
            DataTypes.FIELD("duration", DataTypes.INT()),
            DataTypes.FIELD("sentbyte", DataTypes.INT()),
            DataTypes.FIELD("rcvdbyte", DataTypes.INT()),
            DataTypes.FIELD("sentpkt", DataTypes.INT())]))) \
        .with_schema(  # declare the schema of the table
        Schema()
            .field("time", DataTypes.TIMESTAMP())
            .field("devname", DataTypes.STRING())
            .field("type", DataTypes.STRING())
            .field("srcport", DataTypes.INT())
            .field("dstport", DataTypes.INT())
            .field("service", DataTypes.STRING())
            .field("action", DataTypes.STRING())
            .field("crlevel", DataTypes.STRING())
            .field("srcip", DataTypes.STRING())
            .field("dstip", DataTypes.STRING())
            .field("srccountry", DataTypes.STRING())
            .field("dstcountry", DataTypes.STRING())
            .field("duration", DataTypes.INT())
            .field("sentbyte", DataTypes.INT())
            .field("rcvdbyte", DataTypes.INT())
            .field("sentpkt", DataTypes.INT())) \
        .in_append_mode() \
        .create_temporary_table("syslog_source")


def register_syslogs_sink(st_env):
    st_env \
        .connect(  # declare the external system to connect to
        Kafka()
            .version("universal")
            .topic(os.getenv("KAFKA_OUTPUT_TOPIC"))
            .property("zookeeper.connect", os.getenv("KAFKA_ZOOKEEPER_CONNECT"))
            .property("bootstrap.servers", os.getenv("KAFKA_BOOTSTRAP_SERVER"))) \
        .with_format(  # declare a format for this system
        Json()
            .fail_on_missing_field(True)
            .schema(DataTypes.ROW([
            DataTypes.FIELD("rideId", DataTypes.BIGINT()),
            DataTypes.FIELD("taxiId", DataTypes.BIGINT()),
            DataTypes.FIELD("isStart", DataTypes.BOOLEAN()),
            DataTypes.FIELD("lon", DataTypes.FLOAT()),
            DataTypes.FIELD("lat", DataTypes.FLOAT()),
            DataTypes.FIELD("psgCnt", DataTypes.INT()),
            DataTypes.FIELD("rideTime", DataTypes.STRING())
        ]))) \
        .with_schema(  # declare the schema of the table
        Schema()
            .field("rideId", DataTypes.BIGINT())
            .field("taxiId", DataTypes.BIGINT())
            .field("isStart", DataTypes.BOOLEAN())
            .field("lon", DataTypes.FLOAT())
            .field("lat", DataTypes.FLOAT())
            .field("psgCnt", DataTypes.INT())
            .field("rideTime", DataTypes.STRING())) \
        .in_append_mode() \
        .create_temporary_table("syslog_output")


if __name__ == '__main__':
    print(f"Kafka input topic : {os.getenv('KAFKA_INPUT_TOPIC')}")
    print(f"Kafka output topic : {os.getenv('KAFKA_OUTPUT_TOPIC')}")
    print(f"Kafka Zooekeeper connect : {os.getenv('KAFKA_ZOOKEEPER_CONNECT')}")
    print(f"Kafka Bootstrap server : {os.getenv('KAFKA_BOOTSTRAP_SERVER')}")
    from_kafka_to_kafka_demo()
