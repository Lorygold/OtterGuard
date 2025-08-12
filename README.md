# OtterGuard

**Making analysts’ lives easier by unifying logs from multiple sources into a single, chronologically ordered view.**  
OtterGuard helps security and network analysts quickly consolidate, visualize, and explore their data without the pain of juggling multiple disjointed datasets.

---

## 🚀 Quick Start

Follow these steps to get OtterGuard up and running:

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/OtterGuard.git
cd OtterGuard
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv /home/username/venv_personal/otterguard
source /home/username/venv_personal/otterguard/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Containers (Elasticsearch, Kibana)
```bash
docker compose up -d
```

### 5. Run the Django server
```bash
./manage.py runserver
```

### 6. Access the Upload Interface
Open your browser and go to: `http://localhost:8000/unifier/upload/`.

Select one or more .json files exported from Elasticsearch.

For each file, specify the index name you want the data to be stored in.

Click **Upload** to send the data into Elasticsearch.

### 7. Explore Data in Kibana
Open from your browser: `http://localhost:5601`
Go to **Discover** in Kibana, select the index patterns you created during the upload process.
Build your own views to discover your data::

a. for example, create the `bro` data view for your index: `bro-2025-08-10`:
![unified-view-kibana](/static/images/bro_data_view_kibana_creation_example.png)

b. Then, repeat this step for each index you have, creating new data views:
![unified-view-kibana](/static/images/new_data_view_kibana_creation.png)

c. Create also the view for the default `unified-index` created:
![unified-view-kibana](/static/images/unified_index_kibana_creation.png)

📝 Notes

* The upload interface parses Elasticsearch-style JSON exports and indexes each _source document into your chosen index.

* All uploaded logs are also stored in a unified index for chronological analysis across all data sources.

* Make sure Docker is running before starting the containers.

* The default unified index name is: **unified-index**
