import PyAPI.structures as THUAI7
from PyAPI.Interface import IShipAPI, ITeamAPI, IAI
from PyAPI.utils import AssistFunction
from typing import Union, Final, cast, List
from PyAPI.constants import Constants
import queue
import time


class Setting:
    # 为假则play()期间确保游戏状态不更新，为真则只保证游戏状态在调用相关方法时不更新，大致一帧更新一次
    @staticmethod
    def Asynchronous() -> bool:
        return False

    @staticmethod
    def ShipTypes() -> List[THUAI7.ShipType]:
        return [
            THUAI7.ShipType.CivilianShip,
            THUAI7.ShipType.MilitaryShip,
            THUAI7.ShipType.MilitaryShip,
            THUAI7.ShipType.FlagShip,
        ]


numOfGridPerCell: Final[int] = 1000


class AI(IAI):
    def __init__(self, pID: int):
        self.__playerID = pID

    def ShipPlay(self, api: IShipAPI) -> None:
        # 公共操作
        if self.__playerID == 1:
            api.PrintSelfInfo()
            api.MoveLeft(100)
            time.sleep(1)
            api.MoveRight(100)
            time.sleep(1)
            api.MoveDown(100)
            time.sleep(1)
            api.MoveUp(100)
            time.sleep(1)
            # player1的操作
            return
        elif self.__playerID == 2:
            api.PrintSelfInfo()
            api.MoveLeft(100)
            time.sleep(1)
            api.MoveRight(100)
            time.sleep(1)
            api.MoveDown(100)
            time.sleep(1)
            api.MoveUp(100)
            time.sleep(1)
            # player2的操作
            return
        elif self.__playerID == 3:
            api.PrintSelfInfo()
            api.MoveLeft(100)
            time.sleep(1)
            api.MoveRight(100)
            time.sleep(1)
            api.MoveDown(100)
            time.sleep(1)
            api.MoveUp(100)
            time.sleep(1)
            # player3的操作
            return
        elif self.__playerID == 4:
            # player4的操作
            return
        return

    def TeamPlay(self, api: ITeamAPI) -> None:
        assert self.__playerID == 0, "Team's playerID must be 0"
        api.BuildShip(shipType=THUAI7.ShipType.MilitaryShip,birthIndex=0)
        time.sleep(2)
        # 操作
        return
