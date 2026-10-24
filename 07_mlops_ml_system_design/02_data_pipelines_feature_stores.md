---
domain: mlsd
topic: data_pipelines_feature_stores
title: Data pipelines and feature stores
tags: [data-pipeline, feature-store, spark, kafka]
count: 139
---
# Data pipelines and feature stores

## Warehousing and ETL fundamentals
- [MS02-001] What is a data warehouse, and what are its key characteristics?
- [MS02-002] Walk me through the ETL process and its stages.
- [MS02-003] What is the difference between ETL and ELT, and why has ELT become more common with cloud warehouses?
- [MS02-004] What is a fact table, and how does it differ from a dimension table?
- [MS02-005] How does a data lake differ from a data warehouse, and when would an ML team want each?
- [MS02-006] What is the difference between a full load and an incremental load in ETL, and what are the risks of incremental loads?
- [MS02-007] What is data staging, and why is it an important step in ETL?
- [MS02-008] What are slowly changing dimensions, and how do the common SCD types differ?
- [MS02-009] What are the most common challenges you face when building and operating ETL processes?
- [MS02-010] Compare a star schema with a snowflake schema. When would you pick each?
- [MS02-011] What does it mean for a pipeline task to be idempotent, and how do you make a load job safe to retry or re-run?
- [MS02-012] What does an orchestrator such as Airflow give you over cron scripts: DAGs, retries, backfills, SLAs?
- [MS02-013] What is a data pipeline, and what role does it play in an MLOps workflow?
- [MS02-014] What is DataOps, and how does it relate to MLOps?
- [MS02-015] What do you do when two sources disagree about the same customer or record during a load?
- [MS02-016] Given exports from three customer systems, each with its own customer records, how would you produce one deduplicated set of entities? Walk through your design and the code.
- [MS02-017] Design a system that continuously improves the quality of the data feeding downstream analytics and ML.

## Data lakes, lakehouses and storage formats
- [MS02-018] Why are columnar formats like Parquet preferred over CSV or JSON for analytics and ML datasets?
- [MS02-019] How do you choose a partitioning scheme for a large table, and what goes wrong with over-partitioning or the small-files problem?
- [MS02-020] What do table formats like Delta Lake, Iceberg or Hudi give you that a plain directory of Parquet files cannot?
- [MS02-021] In a Spark Structured Streaming pipeline, what does a Delta transaction log give you that a plain Parquet directory sink cannot?
- [MS02-022] How do you handle schema evolution in a data lake without breaking downstream readers?
- [MS02-023] How do you version and dedupe datasets stored as Parquet?
- [MS02-024] How would you handle large-scale data for model training when it does not fit on one machine?
- [MS02-025] A user loads a 2 TB dataset with the Hugging Face datasets library on a 64 GB RAM machine and it works. How, and when does it stop working?
- [MS02-026] How would you feed 8 training nodes from one hub-hosted dataset without downloading it 8 times?
- [MS02-027] How would you design storage and access so that both batch training and low-latency serving read the same data without drift?

## Hadoop and Spark fundamentals
- [MS02-028] What is Hadoop, and what are its core components?
- [MS02-029] What is Apache Hive, and what types of problems does it solve?
- [MS02-030] Explain HDFS and its architecture, including the roles of the NameNode and DataNodes.
- [MS02-031] How does the MapReduce programming model work, and where does it spend most of its time?
- [MS02-032] What is YARN, and how does it improve Hadoop's resource management?
- [MS02-033] What characteristics differentiate Hadoop from a traditional RDBMS?
- [MS02-034] What is Apache Spark, and what are its main components?
- [MS02-035] Why would you choose Spark over writing plain scripts or using MapReduce?
- [MS02-036] How does Spark differ from Hadoop MapReduce architecturally and in performance?
- [MS02-037] What is an RDD in Spark, and what makes it resilient?
- [MS02-038] What are DataFrames in Spark, and how do they compare to RDDs and Datasets?
- [MS02-039] What is lazy evaluation in Spark, and how does it benefit computations?
- [MS02-040] What are the roles of the Spark driver and the executors?
- [MS02-041] What is a SparkSession, and what is its purpose?
- [MS02-042] What are the ways to run a Spark application (local, client and cluster modes), and how do they differ?
- [MS02-043] How does Spark achieve fault tolerance?
- [MS02-044] How does Spark's DAG scheduler turn a job into stages and tasks?
- [MS02-045] How does Spark integrate with Hadoop components like HDFS and YARN?
- [MS02-046] What data source APIs does Spark provide, and how do you read from and write to external systems?
- [MS02-047] What are accumulators and broadcast variables in Spark, and when would you use each?
- [MS02-048] What does the Catalyst optimizer do in Spark SQL?
- [MS02-049] How does Project Tungsten contribute to Spark's performance?
- [MS02-050] What is the difference between narrow and wide transformations, and why does it matter for performance?

## Spark performance and joins
- [MS02-051] How do you decide how many partitions a Spark job should use, and what happens when there are too few or too many?
- [MS02-052] What is a shuffle in Spark, why is it expensive, and how do you reduce it?
- [MS02-053] In a Spark join of a large fact table to a large dimension table, how does a shuffle-hash join differ from a sort-merge join?
- [MS02-054] In a Spark job that joins a 2 TB fact table to a 50 GB dimension table, when does broadcasting make things worse?
- [MS02-055] One Spark task runs 50 times longer than the rest of its stage. How do you diagnose data skew and fix it?
- [MS02-056] How do salting, adaptive query execution and skew hints each help with a skewed join key?
- [MS02-057] When would you cache or persist a DataFrame in Spark, and when does caching hurt?
- [MS02-058] A Spark job fails with executor out-of-memory errors. What do you check and in what order?
- [MS02-059] Why can a UDF slow down a Spark job compared with built-in functions, and what are the alternatives?
- [MS02-060] You must compute training features over 100 TB of event logs nightly within a 2-hour window. How do you size the cluster and tune the job?
- [MS02-061] Your Spark job produces millions of tiny output files. Why does it happen, and how do you fix it without hurting write throughput?

## Streaming systems and windows
- [MS02-062] What is the difference between batch and stream processing, and when does an ML system need streaming?
- [MS02-063] What is lambda architecture, and what are its drawbacks?
- [MS02-064] How does kappa architecture differ from lambda architecture, and when would you pick it?
- [MS02-065] How does Kafka work at a high level: topics, partitions, consumer groups and offsets?
- [MS02-066] How do you choose a Kafka partition key, and what happens to ordering and hot partitions?
- [MS02-067] Explain at-most-once, at-least-once and exactly-once delivery. How is exactly-once achieved in practice?
- [MS02-068] Why has Apache Flink gained popularity compared with earlier batch and stream processing systems?
- [MS02-069] How do Spark Structured Streaming and Flink differ in their processing model, state handling and latency?
- [MS02-070] What is the difference between event time and processing time, and why does it matter for ML features?
- [MS02-071] What are watermarks and how do they handle late or out-of-order events?
- [MS02-072] Compare tumbling, sliding and session windows, and give a use case for each.
- [MS02-073] How does a stream processor manage large state, and how does checkpointing enable recovery?
- [MS02-074] How do you handle backpressure when a consumer cannot keep up with a Kafka producer?
- [MS02-075] How do you make a streaming job idempotent so that replays and retries do not double-count?
- [MS02-076] What is the purpose of the Replay design pattern in machine learning, and how do you support reprocessing of past events?
- [MS02-077] Design a streaming pipeline that ingests clickstream events and updates user features within seconds. Cover failure handling and late data.
- [MS02-078] Design a data platform that ingests petabytes of events with minute-level latency for ML feature computation.

## Approximate algorithms on streams
- [MS02-079] You have a stream of billions of events and need the top-K most frequent keys with bounded memory. An exact answer is impossible. What do you do?
- [MS02-080] In a streaming top-K frequent keys computation, how do you handle a single key so hot that it skews one partition?
- [MS02-081] What changes in a streaming top-K frequent keys computation for a sliding 5-minute window?
- [MS02-082] When approximating top-K frequent items over an unbounded stream with sketches on 1,000 workers, how do you merge the sketches and what happens to the error bound?
- [MS02-083] When computing approximate stream statistics with sketches, how do you handle a rotating window of the last hour?
- [MS02-084] What are HyperLogLog and Count-Min Sketch, and what questions can each answer in a feature pipeline?
- [MS02-085] When is an approximate aggregate acceptable as a model feature, and what risks does it add?

## Feature stores
- [MS02-086] What is a feature store, and why is it important in MLOps workflows?
- [MS02-087] What are the offline and online stores in a feature store, and why are they separate?
- [MS02-088] Describe the Feature Store design pattern and its advantages, and explain why you would put one between your pipelines and your model.
- [MS02-089] What does a feature store do for feature reuse, discovery and ownership across teams?
- [MS02-090] You need a "number of distinct countries this card was used in over the past hour" feature for fraud scoring. Which pipeline is right, and why?
- [MS02-091] How do batch, streaming and on-demand feature computation differ, and how do you choose among them?
- [MS02-092] How do you materialize features from the offline store to the online store, and how do you keep them consistent?
- [MS02-093] How do you choose an online store (Redis, DynamoDB, Cassandra) for feature serving at a p99 of 10 ms?
- [MS02-094] How do you pre-compute and store embeddings for users and items so that online ranking is fast?
- [MS02-095] How do you set TTLs and handle missing or stale features at serving time?
- [MS02-096] How do you version feature definitions and roll out a changed definition without breaking models that depend on it?
- [MS02-097] Do you always need a feature store? What are the signs a team is too small or too early for one?
- [MS02-098] How do you design a feature store, and what causes training/serving skew inside one?
- [MS02-099] Design a feature platform for a company with 50 models, 500 features and both real-time and batch use cases.

## Training-serving skew and point-in-time correctness
- [MS02-100] What is training-serving skew? How do you detect it and how do you design it out?
- [MS02-101] Where should preprocessing live in an ML training and serving pipeline?
- [MS02-102] How do you keep preprocessing consistent across training, evaluation and inference?
- [MS02-103] Explain the Transformation design pattern and its significance in data preprocessing.
- [MS02-104] What are the typical causes of training-serving skew besides code differences, such as data freshness, defaults and units?
- [MS02-105] How do you monitor for skew in production by comparing logged serving features against training distributions?
- [MS02-106] What is a point-in-time correct join, and why do training sets need one?
- [MS02-107] Give a concrete example of a point-in-time join and show where the naive version leaks.
- [MS02-108] How do you build a training set when a key feature's values get restated 3 days after the fact?
- [MS02-109] Why is log-and-wait (logging features at serving time) sometimes preferable to recomputing features historically?
- [MS02-110] What is training-serving skew, and does it have an equivalent in LLM applications?
- [MS02-111] What is a feature store, and does an LLM application need one?

## Data quality, lineage and versioning
- [MS02-112] What dimensions of data quality do you measure, such as completeness, validity, uniqueness and timeliness?
- [MS02-113] What checks would you put in a pipeline to catch bad data before it reaches training, and where would they sit?
- [MS02-114] How would you use tools like Great Expectations or Deequ in a pipeline, and what do you do when a check fails?
- [MS02-115] How do you detect schema drift and distribution drift in an upstream source before they silently degrade a model?
- [MS02-116] How do you detect a data connector silently missing updates, for example with reconciliation or sampling audits?
- [MS02-117] How do you handle missing values, duplicates and late-arriving records in a pipeline at scale?
- [MS02-118] What role does data versioning play in MLOps, and how does the Data Versioning pattern support model reproducibility?
- [MS02-119] How would you version datasets so that any past model can be retrained exactly? Compare DVC, lakeFS and table-format time travel.
- [MS02-120] Why does the AI team keep asking for lineage, and what does lineage mean for RAG data?
- [MS02-121] A parser bug corrupted some fraction of chunks over three weeks. How does lineage bound the blast radius?
- [MS02-122] What lineage do you attach to LLM-generated (enriched) columns?
- [MS02-123] Where do quality checks belong in a RAG document ingestion pipeline DAG?
- [MS02-124] An AI assistant wrote an incremental model that loads yesterday's orders into a fact table. What do you check before shipping it?
- [MS02-125] You inherit a data pipeline script, and your fix changes historical numbers the customer already reported upstream. What now?
- [MS02-126] In an LLM batch job classifying and summarising 50 million records, the label distribution shifts halfway through the run. Is it a bug or the data?
- [MS02-127] How do you handle PII and GDPR deletion requests in a data lake that feeds model training?

## Freshness, backfills and labeling pipelines
- [MS02-128] How do you define and monitor a data freshness SLA for a pipeline, and what metrics matter?
- [MS02-129] Product wants an assistant to answer from data no older than 15 minutes. How do you design and monitor that freshness SLA?
- [MS02-130] What do you do when one data source cannot meet the freshness SLA of an AI assistant?
- [MS02-131] A source API offers no change feed and rate-limits you to 10 QPS over 20M documents. What is your freshness story?
- [MS02-132] A backfill floods the queue and pushes incremental lag past the SLA. How do you isolate the lanes?
- [MS02-133] How would you safely backfill a feature or table after a logic bug fix, without disturbing live consumers?
- [MS02-134] How do you design pipelines to be observable, and which alerts (freshness, volume, schema, latency) would you set up first?
- [MS02-135] How do you capture changes from an operational database into a pipeline, and what are the tradeoffs of CDC versus periodic snapshots?
- [MS02-136] What does a labeling pipeline look like end to end, from raw data to a versioned training set?
- [MS02-137] How do you measure and improve label quality, for example with inter-annotator agreement, gold sets and audits?
- [MS02-138] How do you combine human labels, weak supervision and model-assisted labeling to cut cost without hurting quality?
- [MS02-139] Design an active-learning data loop in which production predictions, human review and retraining data feed each other.
