from pydantic import BaseModel, Field
from typing import Literal


class Segment(BaseModel):
    segment_id: str
    label: Literal[
        "roof",
        "wall",
        "ground",
        "building",
        "other"
    ]
    confidence: float = Field(ge=0.0, le=1.0)


class Geometry(BaseModel):
    type: Literal["Polygon"]
    coordinates: list


class BuildingFootprint(BaseModel):
    footprint_id: str
    geometry: Geometry


class ClassifiedSegmentPackage(BaseModel):
    package_id: str
    source_package_id: str
    segments: list[Segment]
    building_footprints: list[BuildingFootprint]