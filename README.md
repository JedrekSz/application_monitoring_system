# Application Monitoring System

A Python-based monitoring system for tracking website availability and performance metrics. The application automatically checks configured services, stores monitoring results in a PostgreSQL database, generates reports, and provides a web dashboard for data visualization.

## Features

* Automated website availability monitoring
* Response time measurement
* Error logging and exception handling
* PostgreSQL database integration
* CSV report generation
* Interactive dashboard built with Streamlit
* Configurable monitored services using JSON
* Uptime and performance statistics

## Tech Stack

* Python
* PostgreSQL
* Streamlit

## Project Structure

```text
application-monitoring-system/
│
├── app.py
├── monitor.py
├── database.py
├── reports.py
├── dashboard.py
├── config.json
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd application-monitoring-system
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file based on `.env.example`:

```env
DB_HOST=localhost
DB_NAME=application_monitoring
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

Configure monitored services in `config.json`:

```json
{
  "services": [
    {
      "name": "Google",
      "url": "https://google.com"
    },
    {
      "name": "GitHub",
      "url": "https://github.com"
    }
  ]
}
```

## Running the Application

Start the monitoring service:

```bash
python app.py
```

Launch the dashboard:

```bash
streamlit run dashboard.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

## Database

Monitoring results are stored in PostgreSQL and include:

* Service name
* URL
* HTTP status code
* Response time
* Check timestamp
* Error details

## Example Use Cases

* Website availability monitoring
* Performance tracking
* Basic incident detection
* Service uptime analysis
* Operational reporting

## Author

Jędrzej Szwach
