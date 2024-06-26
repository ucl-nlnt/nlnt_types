from typing import TypedDict, List, Union, Optional


FloatList = List[Union[float]]


class LaserscanFrame(TypedDict):
    time_sec: float
    time_nano: float
    angle_min: float
    angle_max: float
    angle_increment: float
    scan_time: float
    range_min: float
    range_max: float
    ranges: FloatList
    intensities: FloatList


class TwistFrame(TypedDict):
    linear: FloatList
    angular: FloatList
    time: Optional[float]


class IMUFrame(TypedDict):
    quarternion_orientation: FloatList
    orientation_covariance: FloatList
    angular_velocity: FloatList
    angular_velocity_covariance: FloatList
    linear_acceleration: FloatList
    linear_acceleration_covariance: FloatList


class OdometryFrame(TypedDict):
    time_sec: int
    time_nano: int
    pose_position: FloatList
    pose_orientation_quarternion: FloatList
    object_covariance: FloatList


class BatteryFrame(TypedDict):
    percentage: float
    voltage: float
    temperature: float
    current: float


class DataframeType(TypedDict):
    laser_scan: Optional[LaserscanFrame]
    twist: TwistFrame
    imu: IMUFrame
    odometry: OdometryFrame
    battery: BatteryFrame
    frame_data: str


StatesList = List[Union[DataframeType]]


class KeyframeType(TypedDict):
    natural_language_prompt: Optional[str]
    start_timestamp: Optional[float]
    end_timestamp: Optional[float]
    step_num: int
    states: StatesList


KeyframesList = List[Union[KeyframeType]]


class DatalogType(TypedDict):
    username: str
    natural_language_prompt: str
    timestamp_s: str
    timestamp_float: float
    states: StatesList
    distance_traveled: float
    radians_rotated: float
    ground_truth: Optional[FloatList]
    simulation: Optional[int]
    keyframes: Optional[KeyframesList]


DatalogsList = List[Union[DatalogType]]
