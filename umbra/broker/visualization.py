dashboard_template = {
    # "annotations": {
    #     "list": [
    #         {
    #             "builtIn": 1,
    #             "datasource": "-- Grafana --",
    #             "enable": True,
    #             "hide": True,
    #             "iconColor": "rgba(0, 211, 255, 1)",
    #             "name": "Annotations & Alerts",
    #             "type": "dashboard",
    #         }
    #     ]
    # },
    "editable": True,
    "gnetId": None,
    "graphTooltip": 0,
    "id": None,
    "links": [],
    "panels": [],
    "refresh": "10s",
    "schemaVersion": 16,
    "style": "dark",
    "tags": [],
    "templating": {"list": []},
    "time": {"from": "now-15m", "to": "now"},
    "timepicker": {},
    "timezone": "browser",
    "title": "Umbra",
    "uid": "umbra",
    "version": 0,
}

# {
#     "datasource": None,
#     "fieldConfig": {"defaults": {"custom": {}}, "overrides": []},
#     "gridPos": {"h": 9, "w": 24, "x": 0, "y": 0},
#     "id": 8,
#     "options": {
#         "content": "# Title\n\nFor markdown syntax help: [commonmark.org/help](https://commonmark.org/help/)\n![Image](/public/img/grafanaconline.png)\n        ",
#         "mode": "markdown",
#     },
#     "pluginVersion": "7.1.0",
#     "timeFrom": None,
#     "timeShift": None,
#     "title": "Umbra Topology",
#     "type": "text",
# },

panels_template = [
    {
        "aliasColors": {},
        "bars": False,
        "dashLength": 10,
        "dashes": False,
        "datasource": "",
        "fieldConfig": {"defaults": {"custom": {}}, "overrides": []},
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {"h": 10, "w": 24, "x": 0, "y": 0},
        "hiddenSeries": False,
        "id": 1,
        "legend": {
            "alignAsTable": True,
            "avg": True,
            "current": False,
            "hideEmpty": False,
            "max": True,
            "min": True,
            "rightSide": True,
            "show": True,
            "total": False,
            "values": True,
        },
        "lines": True,
        "linewidth": 1,
        "NonePointMode": "None",
        "options": {"alertThreshold": True},
        "percentage": False,
        "pluginVersion": "7.2.0",
        "pointradius": 2,
        "points": False,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": False,
        "steppedLine": False,
        "targets": [
            {
                "groupBy": [
                    {"params": ["$__interval"], "type": "time"},
                    {"params": ["environment"], "type": "tag"},
                    {"params": ["none"], "type": "fill"},
                ],
                "measurement": "host",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                        {"params": ["mem_percent"], "type": "field"},
                        {"params": [], "type": "mean"},
                    ]
                ],
                "tags": [],
            }
        ],
        "thresholds": [],
        "timeFrom": None,
        "timeRegions": [],
        "timeShift": None,
        "title": "Host Memory Usage - Environment {environment}",
        "tooltip": {"shared": True, "sort": 0, "value_type": "individual"},
        "type": "graph",
        "xaxis": {
            "buckets": None,
            "mode": "time",
            "name": None,
            "show": True,
            "values": [],
        },
        "yaxes": [
            {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
            {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
        ],
        "yaxis": {"align": False, "alignLevel": None},
    },
    {
        "aliasColors": {},
        "bars": False,
        "dashLength": 10,
        "dashes": False,
        "datasource": "",
        "fieldConfig": {"defaults": {"custom": {}}, "overrides": []},
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {"h": 10, "w": 24, "x": 0, "y": 1},
        "hiddenSeries": False,
        "id": 2,
        "legend": {
            "alignAsTable": True,
            "avg": True,
            "current": False,
            "hideEmpty": False,
            "max": True,
            "min": True,
            "rightSide": True,
            "show": True,
            "total": False,
            "values": True,
        },
        "lines": True,
        "linewidth": 1,
        "NonePointMode": "None",
        "options": {"alertThreshold": True},
        "percentage": False,
        "pluginVersion": "7.2.0",
        "pointradius": 2,
        "points": False,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": False,
        "steppedLine": False,
        "targets": [
            {
                "groupBy": [
                    {"params": ["$__interval"], "type": "time"},
                    {"params": ["environment"], "type": "tag"},
                    {"params": ["none"], "type": "fill"},
                ],
                "measurement": "host",
                "orderByTime": "ASC",
                "policy": "default",
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                        {"params": ["cpu_percent"], "type": "field"},
                        {"params": [], "type": "mean"},
                    ]
                ],
                "tags": [],
            }
        ],
        "thresholds": [],
        "timeFrom": None,
        "timeRegions": [],
        "timeShift": None,
        "title": "Host CPU Usage - Environment {environment}",
        "tooltip": {"shared": True, "sort": 0, "value_type": "individual"},
        "type": "graph",
        "xaxis": {
            "buckets": None,
            "mode": "time",
            "name": None,
            "show": True,
            "values": [],
        },
        "yaxes": [
            {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
            {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
        ],
        "yaxis": {"align": False, "alignLevel": None},
    },
    {
        "aliasColors": {},
        "bars": False,
        "dashLength": 10,
        "dashes": False,
        "datasource": "",
        "fieldConfig": {"defaults": {"custom": {}}, "overrides": []},
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {"h": 10, "w": 24, "x": 0, "y": 2},
        "hiddenSeries": False,
        "id": 3,
        "legend": {
            "alignAsTable": True,
            "avg": True,
            "current": False,
            "max": True,
            "min": True,
            "rightSide": True,
            "show": True,
            "total": False,
            "values": True,
        },
        "lines": True,
        "linewidth": 1,
        "NonePointMode": "None",
        "options": {"alertThreshold": False},
        "percentage": False,
        "pluginVersion": "7.2.0",
        "pointradius": 2,
        "points": True,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": False,
        "steppedLine": False,
        "targets": [
            {
                "alias": "",
                "groupBy": [
                    {"params": ["$__interval"], "type": "time"},
                    {"params": ["source"], "type": "tag"},
                    {"params": ["none"], "type": "fill"},
                ],
                "measurement": "container",
                "orderByTime": "ASC",
                "policy": "default",
                "query": 'SELECT mean("mem_usage") FROM "container" WHERE $timeFilter GROUP BY time($__interval), "source" fill(0)',
                "rawQuery": False,
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                        {"params": ["mem_usage"], "type": "field"},
                        {"params": [], "type": "distinct"},
                    ]
                ],
                "tags": [],
            }
        ],
        "thresholds": [],
        "timeFrom": None,
        "timeRegions": [],
        "timeShift": None,
        "title": "Containers Memory Usage - Environment {environment}",
        "tooltip": {"shared": True, "sort": 0, "value_type": "individual"},
        "type": "graph",
        "xaxis": {
            "buckets": None,
            "mode": "time",
            "name": None,
            "show": True,
            "values": [],
        },
        "yaxes": [
            {
                "format": "none",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
            {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
        ],
        "yaxis": {"align": False, "alignLevel": None},
    },
    {
        "aliasColors": {},
        "bars": False,
        "dashLength": 10,
        "dashes": False,
        "datasource": "",
        "fieldConfig": {"defaults": {"custom": {}}, "overrides": []},
        "fill": 1,
        "fillGradient": 0,
        "gridPos": {"h": 10, "w": 24, "x": 0, "y": 3},
        "hiddenSeries": False,
        "id": 4,
        "legend": {
            "alignAsTable": True,
            "avg": True,
            "current": False,
            "max": True,
            "min": True,
            "rightSide": True,
            "show": True,
            "total": False,
            "values": True,
        },
        "lines": True,
        "linewidth": 1,
        "NonePointMode": "None",
        "options": {"alertThreshold": False},
        "percentage": False,
        "pluginVersion": "7.2.0",
        "pointradius": 2,
        "points": True,
        "renderer": "flot",
        "seriesOverrides": [],
        "spaceLength": 10,
        "stack": False,
        "steppedLine": False,
        "targets": [
            {
                "alias": "",
                "groupBy": [
                    {"params": ["$__interval"], "type": "time"},
                    {"params": ["source"], "type": "tag"},
                    {"params": ["none"], "type": "fill"},
                ],
                "measurement": "container",
                "orderByTime": "ASC",
                "policy": "default",
                "query": 'SELECT mean("cpu_percent") FROM "container" WHERE $timeFilter GROUP BY time($__interval), "source" fill(0)',
                "rawQuery": False,
                "refId": "A",
                "resultFormat": "time_series",
                "select": [
                    [
                        {"params": ["cpu_percent"], "type": "field"},
                        {"params": [], "type": "distinct"},
                    ]
                ],
                "tags": [],
            }
        ],
        "thresholds": [],
        "timeFrom": None,
        "timeRegions": [],
        "timeShift": None,
        "title": "Containers CPU Usage - Environment {environment}",
        "tooltip": {"shared": True, "sort": 0, "value_type": "individual"},
        "type": "graph",
        "xaxis": {
            "buckets": None,
            "mode": "time",
            "name": None,
            "show": True,
            "values": [],
        },
        "yaxes": [
            {
                "format": "none",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
            {
                "format": "short",
                "label": None,
                "logBase": 1,
                "max": None,
                "min": None,
                "show": True,
            },
        ],
        "yaxis": {"align": False, "alignLevel": None},
    },
]