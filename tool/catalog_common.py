"""Shared helpers for Mechmate catalog compilation."""


def article(
    *,
    id,
    title,
    summary,
    severity,
    locations,
    senses,
    systems,
    symptoms,
    safety,
    tools,
    causes,
    specs=None,
    parts=None,
    sources=None,
    related=None,
    filters=None,
):
    return {
        "id": id,
        "title": title,
        "summary": summary,
        "severity": severity,
        "locations": locations,
        "senses": senses,
        "systems": systems,
        "symptoms": symptoms,
        "safety": safety,
        "tools": tools,
        "causes": causes,
        "specs": specs or [],
        "parts": parts or [],
        "sources": sources or [],
        "related": related or [],
        "filters": filters or [{"universal": True}],
    }


def cause(rank, name, likelihood, why, tests, fix):
    return {
        "rank": rank,
        "name": name,
        "likelihood": likelihood,
        "why": why,
        "tests": tests,
        "fix": fix,
    }


def test(name, how, passed, failed):
    return {"name": name, "how": how, "pass": passed, "fail": failed}


def spec(name, value, note=None):
    item = {"name": name, "value": value}
    if note:
        item["note"] = note
    return item


def source(title, url):
    return {"title": title, "url": url}


COMMON_SAFETY_BAY = [
    "Park on level ground, park brake on, wheels chocked, transmission in park or in gear.",
    "Support the vehicle on rated stands. Never work under a jack only.",
    "Allow exhaust, turbo, and DPF to cool. Regeneration surfaces exceed 500C.",
    "Disconnect the negative 12V earth last when you isolate. On 48V vehicles, treat blue 48V cables as live until the service plug or connector is open and you have measured 0V.",
]


COMMON_SCAN = [
    "OBD2 scan tool that can read manufacturer data, not only generic P-codes",
    "Digital multimeter with min/max",
    "Infrared thermometer",
    "Inspection light and borescope",
]
