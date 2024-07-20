from typing import Callable, Iterator, Optional, Union, overload

import numpy as np

class CostEvaluator:
    def __init__(
        self, load_penalty: int, tw_penalty: int, dist_penalty: int
    ) -> None: ...
    def load_penalty(self, load: int, capacity: int) -> int: ...
    def tw_penalty(self, time_warp: int) -> int: ...
    def dist_penalty(self, distance: int, max_distance: int) -> int: ...
    def penalised_cost(self, solution: Solution) -> int: ...
    def cost(self, solution: Solution) -> int: ...

class DynamicBitset:
    def __init__(self, num_bits: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, idx: int) -> bool: ...
    def __setitem__(self, idx: int, value: bool) -> None: ...
    def all(self) -> bool: ...
    def any(self) -> bool: ...
    def none(self) -> bool: ...
    def count(self) -> int: ...
    def __len__(self) -> int: ...
    def __or__(self, other: DynamicBitset) -> DynamicBitset: ...
    def __and__(self, other: DynamicBitset) -> DynamicBitset: ...
    def __xor__(self, other: DynamicBitset) -> DynamicBitset: ...
    def __invert__(self) -> DynamicBitset: ...
    def reset(self) -> DynamicBitset: ...

class Client:
    x: int
    y: int
    delivery: int
    pickup: int
    service_duration: int
    tw_early: int
    tw_late: int
    release_time: int
    prize: int
    required: bool
    group: Optional[int]
    name: str
    def __init__(
        self,
        x: int,
        y: int,
        delivery: int = 0,
        pickup: int = 0,
        service_duration: int = 0,
        tw_early: int = 0,
        tw_late: int = ...,
        release_time: int = 0,
        prize: int = 0,
        required: bool = True,
        group: Optional[int] = None,
        *,
        name: str = "",
    ) -> None: ...

class ClientGroup:
    required: bool
    mutually_exclusive: bool
    def __init__(
        self,
        clients: list[int] = [],
        required: bool = True,
    ) -> None: ...
    @property
    def clients(self) -> list[int]: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def add_client(self, client: int) -> None: ...
    def clear(self) -> None: ...

class Depot:
    x: int
    y: int
    name: str
    def __init__(
        self,
        x: int,
        y: int,
        *,
        name: str = "",
    ) -> None: ...

class VehicleType:
    num_available: int
    start_depot: int
    end_depot: int
    capacity: int
    tw_early: int
    tw_late: int
    max_duration: int
    max_distance: int
    fixed_cost: int
    unit_distance_cost: int
    unit_duration_cost: int
    profile: int
    name: str
    def __init__(
        self,
        num_available: int = 1,
        capacity: int = 0,
        start_depot: int = 0,
        end_depot: int = 0,
        fixed_cost: int = 0,
        tw_early: int = 0,
        tw_late: int = ...,
        max_duration: int = ...,
        max_distance: int = ...,
        unit_distance_cost: int = 1,
        unit_duration_cost: int = 0,
        profile: int = 0,
        *,
        name: str = "",
    ) -> None: ...
    def replace(
        self,
        num_available: Optional[int] = None,
        capacity: Optional[int] = None,
        start_depot: Optional[int] = None,
        end_depot: Optional[int] = None,
        fixed_cost: Optional[int] = None,
        tw_early: Optional[int] = None,
        tw_late: Optional[int] = None,
        max_duration: Optional[int] = None,
        max_distance: Optional[int] = None,
        unit_distance_cost: Optional[int] = None,
        unit_duration_cost: Optional[int] = None,
        profile: Optional[int] = None,
        *,
        name: Optional[str] = None,
    ) -> VehicleType: ...

class ProblemData:
    def __init__(
        self,
        clients: list[Client],
        depots: list[Depot],
        vehicle_types: list[VehicleType],
        distance_matrices: list[np.ndarray[int]],
        duration_matrices: list[np.ndarray[int]],
        groups: list[ClientGroup] = [],
    ) -> None: ...
    def location(self, idx: int) -> Union[Client, Depot]: ...
    def clients(self) -> list[Client]: ...
    def depots(self) -> list[Depot]: ...
    def groups(self) -> list[ClientGroup]: ...
    def vehicle_types(self) -> list[VehicleType]: ...
    def distance_matrices(self) -> list[np.ndarray[int]]: ...
    def duration_matrices(self) -> list[np.ndarray[int]]: ...
    def replace(
        self,
        clients: Optional[list[Client]] = None,
        depots: Optional[list[Depot]] = None,
        vehicle_types: Optional[list[VehicleType]] = None,
        distance_matrices: Optional[list[np.ndarray[int]]] = None,
        duration_matrices: Optional[list[np.ndarray[int]]] = None,
        groups: Optional[list[ClientGroup]] = None,
    ) -> ProblemData: ...
    def centroid(self) -> tuple[float, float]: ...
    def group(self, group: int) -> ClientGroup: ...
    def vehicle_type(self, vehicle_type: int) -> VehicleType: ...
    def distance_matrix(self, profile: int) -> np.ndarray[int]: ...
    def duration_matrix(self, profile: int) -> np.ndarray[int]: ...
    @property
    def num_clients(self) -> int: ...
    @property
    def num_groups(self) -> int: ...
    @property
    def num_depots(self) -> int: ...
    @property
    def num_locations(self) -> int: ...
    @property
    def num_vehicles(self) -> int: ...
    @property
    def num_vehicle_types(self) -> int: ...
    @property
    def num_profiles(self) -> int: ...

class Route:
    def __init__(
        self, data: ProblemData, visits: list[int], vehicle_type: int
    ) -> None: ...
    def __getitem__(self, idx: int) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def is_feasible(self) -> bool: ...
    def has_excess_load(self) -> bool: ...
    def has_excess_distance(self) -> bool: ...
    def has_time_warp(self) -> bool: ...
    def delivery(self) -> int: ...
    def pickup(self) -> int: ...
    def excess_load(self) -> int: ...
    def excess_distance(self) -> int: ...
    def distance(self) -> int: ...
    def distance_cost(self) -> int: ...
    def duration(self) -> int: ...
    def duration_cost(self) -> int: ...
    def visits(self) -> list[int]: ...
    def time_warp(self) -> int: ...
    def start_time(self) -> int: ...
    def end_time(self) -> int: ...
    def slack(self) -> int: ...
    def service_duration(self) -> int: ...
    def travel_duration(self) -> int: ...
    def wait_duration(self) -> int: ...
    def release_time(self) -> int: ...
    def prizes(self) -> int: ...
    def centroid(self) -> tuple[float, float]: ...
    def vehicle_type(self) -> int: ...
    def start_depot(self) -> int: ...
    def end_depot(self) -> int: ...
    def __getstate__(self) -> tuple: ...
    def __setstate__(self, state: tuple, /) -> None: ...

class Solution:
    def __init__(
        self,
        data: ProblemData,
        routes: Union[list[Route], list[list[int]]],
    ) -> None: ...
    @classmethod
    def make_random(
        cls, data: ProblemData, rng: RandomNumberGenerator
    ) -> Solution: ...
    def neighbours(self) -> list[Optional[tuple[int, int]]]: ...
    def routes(self) -> list[Route]: ...
    def has_excess_load(self) -> bool: ...
    def has_excess_distance(self) -> bool: ...
    def has_time_warp(self) -> bool: ...
    def distance(self) -> int: ...
    def distance_cost(self) -> int: ...
    def duration(self) -> int: ...
    def duration_cost(self) -> int: ...
    def excess_load(self) -> int: ...
    def excess_distance(self) -> int: ...
    def fixed_vehicle_cost(self) -> int: ...
    def time_warp(self) -> int: ...
    def prizes(self) -> int: ...
    def uncollected_prizes(self) -> int: ...
    def is_feasible(self) -> bool: ...
    def is_group_feasible(self) -> bool: ...
    def is_complete(self) -> bool: ...
    def num_routes(self) -> int: ...
    def num_clients(self) -> int: ...
    def num_missing_clients(self) -> int: ...
    def __copy__(self) -> Solution: ...
    def __deepcopy__(self, memo: dict) -> Solution: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> tuple: ...
    def __setstate__(self, state: tuple, /) -> None: ...

class PopulationParams:
    generation_size: int
    lb_diversity: float
    min_pop_size: int
    nb_close: int
    nb_elite: int
    ub_diversity: float
    def __init__(
        self,
        min_pop_size: int = 25,
        generation_size: int = 40,
        nb_elite: int = 4,
        nb_close: int = 5,
        lb_diversity: float = 0.1,
        ub_diversity: float = 0.5,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def max_pop_size(self) -> int: ...

class SubPopulation:
    def __init__(
        self,
        diversity_op: Callable[[Solution, Solution], float],
        params: PopulationParams,
    ) -> None: ...
    def add(
        self, solution: Solution, cost_evaluator: CostEvaluator
    ) -> None: ...
    def purge(self, cost_evaluator: CostEvaluator) -> None: ...
    def update_fitness(self, cost_evaluator: CostEvaluator) -> None: ...
    def __getitem__(self, idx: int) -> SubPopulationItem: ...
    def __iter__(self) -> Iterator[SubPopulationItem]: ...
    def __len__(self) -> int: ...

class SubPopulationItem:
    @property
    def fitness(self) -> float: ...
    @property
    def solution(self) -> Solution: ...
    def avg_distance_closest(self) -> float: ...

class DistanceSegment:
    def __init__(
        self,
        idx_first: int,
        idx_last: int,
        distance: int,
    ) -> None: ...
    @overload
    @staticmethod
    def merge(
        distance_matrix: np.ndarray[int],
        first: DistanceSegment,
        second: DistanceSegment,
    ) -> DistanceSegment: ...
    @overload
    @staticmethod
    def merge(
        distance_matrix: np.ndarray[int],
        first: DistanceSegment,
        second: DistanceSegment,
        third: DistanceSegment,
    ) -> DistanceSegment: ...
    def distance(self) -> int: ...

class LoadSegment:
    def __init__(
        self,
        delivery: int,
        pickup: int,
        load: int,
    ) -> None: ...
    @overload
    @staticmethod
    def merge(
        first: LoadSegment,
        second: LoadSegment,
    ) -> LoadSegment: ...
    @overload
    @staticmethod
    def merge(
        first: LoadSegment,
        second: LoadSegment,
        third: LoadSegment,
    ) -> LoadSegment: ...
    def delivery(self) -> int: ...
    def pickup(self) -> int: ...
    def load(self) -> int: ...

class DurationSegment:
    def __init__(
        self,
        idx_first: int,
        idx_last: int,
        duration: int,
        time_warp: int,
        tw_early: int,
        tw_late: int,
        release_time: int,
    ) -> None: ...
    @overload
    @staticmethod
    def merge(
        duration_matrix: np.ndarray[int],
        first: DurationSegment,
        second: DurationSegment,
    ) -> DurationSegment: ...
    @overload
    @staticmethod
    def merge(
        duration_matrix: np.ndarray[int],
        first: DurationSegment,
        second: DurationSegment,
        third: DurationSegment,
    ) -> DurationSegment: ...
    def duration(self) -> int: ...
    def tw_early(self) -> int: ...
    def tw_late(self) -> int: ...
    def time_warp(self, max_duration: int = ...) -> int: ...

class RandomNumberGenerator:
    @overload
    def __init__(self, seed: int) -> None: ...
    @overload
    def __init__(self, state: list[int]) -> None: ...
    @staticmethod
    def max() -> int: ...
    @staticmethod
    def min() -> int: ...
    def rand(self) -> float: ...
    def randint(self, high: int) -> int: ...
    def __call__(self) -> int: ...
    def state(self) -> list[int]: ...
